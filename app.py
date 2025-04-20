from flask import Flask, render_template, request, jsonify, url_for
import requests
from health_advisor import chat_health
from news_fetcher import health_news_fetcher
import torch
from PIL import Image
import io
import base64
import os
from transformers import AutoModelForImageClassification, AutoImageProcessor

app = Flask(__name__)

# Initialize plant disease detection model
disease_model = None
disease_processor = None

def load_disease_model():
    global disease_model, disease_processor
    if disease_model is None:
        disease_processor = AutoImageProcessor.from_pretrained("linkanjarad/mobilenet_v2_1.0_224-plant-disease-identification")
        disease_model = AutoModelForImageClassification.from_pretrained("linkanjarad/mobilenet_v2_1.0_224-plant-disease-identification")
        # Move model to GPU if available
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        disease_model.to(device)

@app.route('/map')                      
def index():
    return render_template('map.html')

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/nearby_hospitals', methods=['POST'])
def nearby_hospitals():
    data = request.get_json()
    lat = data.get('lat')
    lon = data.get('lon')

    # Overpass API query for nearby hospitals (5km radius)
    overpass_url = "http://overpass-api.de/api/interpreter"
    query = f"""
    [out:json];
    (
      node["amenity"="hospital"](around:10000,{lat},{lon});
      way["amenity"="hospital"](around:1000,{lat},{lon});
      relation["amenity"="hospital"](around:10000,{lat},{lon});
    );
    out center;
    """
    response = requests.post(overpass_url, data=query)
    hospitals = response.json().get('elements', [])
    # print(hospitals)
    return jsonify(hospitals)


@app.route('/agri')
def agri():
    # Fetch agricultural news
    agri_news = health_news_fetcher(q="farming OR agriculture OR fertilizer OR pesticide OR crop OR soil OR irrigation") 
    
    # Get top 4 news items or fewer if less available
    top_news = agri_news[:4] if agri_news else []
    
    return render_template('agri.html', agri_news=top_news)

@app.route('/health')
def health():
    # Fetch health news data
    health_news = health_news_fetcher(category="health", q="health OR disease OR medicine OR doctor OR hospital OR patient OR treatment OR care OR health-care OR virus OR mental-health")
    
    # Get top 4 news items or fewer if less available
    top_news = health_news[:4] if health_news else []
    
    return render_template('health.html', news=top_news)

@app.route("/weather")
def weather():
    # Get real weather data for Kolhapur
    from weather_fetcher import get_weather_data
    weather_data = get_weather_data("Kolhapur")
    return render_template("weatherPage.html", weather_data=weather_data)

@app.route("/chat_weather", methods=["POST"])
def chat_weather_route():
    from weather_agent import chat_weather
    question = request.form.get("message", "")
    response = chat_weather(question, return_text=True)
    return jsonify({"response": response})

@app.route("/chat_health", methods=["POST"])
def chat_health_route():
    question = request.form.get("message", "")
    response = chat_health(question, return_text=True)
    return jsonify({"response": response})

@app.route("/chat_farm", methods=["POST"])
def chat_farm_route():
    from farm_advisor import chat_health
    question = request.form.get("message", "")
    response = chat_health(question, return_text=True)
    return jsonify({"response": response})

@app.route("/detect_disease", methods=["POST"])
def detect_disease():
    # Load model if not already loaded
    load_disease_model()
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    # Get the uploaded file
    if 'image' not in request.files:
        return jsonify({
            "success": False,
            "error": "No image file provided"
        })
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({
            "success": False,
            "error": "No image selected"
        })
    
    try:
        # Process the image
        image = Image.open(io.BytesIO(file.read()))
        
        # Preprocess the image
        inputs = disease_processor(images=image, return_tensors="pt").to(device)
        
        # Inference
        with torch.no_grad():
            outputs = disease_model(**inputs)
            logits = outputs.logits
            predicted_class = logits.argmax(-1).item()
            
        # Get confidence score
        confidences = torch.nn.functional.softmax(logits, dim=1)
        confidence = confidences[0][predicted_class].item() * 100
        
        # Get label
        label = disease_model.config.id2label[predicted_class]
        
        # Treatment recommendations - could be expanded to a database lookup
        treatments = {
            "Tomato Late Blight": "Apply copper-based fungicide every 7-10 days. Ensure proper air circulation between plants. Remove and destroy infected leaves.",
            "Rice Brown Spot": "Treat seeds with hot water before sowing. Apply propiconazole at 1 ml/liter of water. Maintain proper field drainage.",
            "Potato Early Blight": "Apply chlorothalonil or mancozeb fungicide. Practice crop rotation. Remove volunteer potato plants and nightshade weeds.",
            "Cotton Leaf Curl": "Use resistant varieties. Control whitefly vector with neem-based insecticides. Avoid planting near infected crops.",
            "Tomato Leaf Mold": "Apply fungicide containing chlorothalonil. Improve ventilation in greenhouse. Avoid overhead watering.",
            "Apple Scab": "Apply fungicides containing captan or myclobutanil. Rake and destroy fallen leaves. Prune trees to improve air circulation.",
            "Grape Black Rot": "Apply fungicides containing mancozeb or myclobutanil. Remove mummified fruits. Prune vines for better air circulation.",
            "Corn Northern Leaf Blight": "Plant resistant hybrids. Apply foliar fungicides. Implement crop rotation.",
            "Healthy Plant": "Your plant appears healthy! Continue with regular fertilization and irrigation practices."
        }
        
        # Default treatment if specific one not available
        treatment = treatments.get(label, "Consult a local agricultural expert for specific treatment. General recommendation: Remove affected leaves and consider applying appropriate fungicide or insecticide based on diagnosis.")
        print(label, confidence, treatment)
        return jsonify({
            "success": True,
            "disease": label,
            "confidence": f"{confidence:.1f}%",
            "treatment": treatment
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        })

if __name__ == '__main__':
    app.run(debug=True)