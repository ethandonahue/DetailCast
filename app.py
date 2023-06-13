from flask import Flask, render_template, request
from weather import get_weather

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        location = request.form['location']
        forecast, formatted_location = get_weather(location)
        if forecast == "error" or formatted_location == "error":
            error = "Error retrieving weather information"
            return render_template('index.html', error=error)
        return render_template('weather.html', forecast=forecast, location=formatted_location)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()
