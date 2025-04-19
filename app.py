from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

# @app.route('/weather')
# def weather():
#     return render_template('weatherPage.html')

@app.route('/agri')
def agri():
    return render_template('agri.html')

@app.route("/weather")
def weather():
    import json
    with open("sample_data.json") as f:
        data = json.load(f)
    return render_template("weatherPage.html", weather_data=data)

if __name__ == '__main__':
    app.run(debug=True)
