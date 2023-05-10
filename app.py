from flask import Flask, render_template, request
from weather import get_weather

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():  # put application's code here
    if request.method == 'POST':
        location = request.form['location']
        temperature = get_weather(location)
        if temperature == "error":
            return render_template('error.html')
        return render_template('result.html', location=location, temperature=temperature)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run()
