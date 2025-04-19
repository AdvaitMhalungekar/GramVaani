from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('map.html')

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

if __name__ == '__main__':
    app.run(debug=True)
