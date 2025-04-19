
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

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

    # Overpass API query for nearby hospitals (1km radius)
    overpass_url = "http://overpass-api.de/api/interpreter"
    query = f"""
    [out:json];
    (
      node["amenity"="hospital"](around:5000,{lat},{lon});
      way["amenity"="hospital"](around:5000,{lat},{lon});
      relation["amenity"="hospital"](around:5000,{lat},{lon});
    );
    out center;
    """
    response = requests.post(overpass_url, data=query)
    hospitals = response.json().get('elements', [])
    print(hospitals)
    return jsonify(hospitals)

# @app.route('/weather')
# def weather():
#     return render_template('weatherPage.html')

@app.route('/agri')
def agri():
    return render_template('agri.html')

@app.route('/health')
def health():
    return render_template('health.html')

@app.route("/weather")
def weather():
    import json
    with open("sample_data.json") as f:
        data = json.load(f)
    return render_template("weatherPage.html", weather_data=data)

if __name__ == '__main__':
    app.run(debug=True)


