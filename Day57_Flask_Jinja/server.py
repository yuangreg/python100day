from flask import Flask, render_template
import requests
from random import randint

app = Flask(__name__)

@app.route('/')
def home():
    number = randint(1,10)
    return render_template('index.html', num=number)

@app.route('/guess/<name>')
def guess(name):
    gender, age = get_value(name)
    return render_template('guess.html', name=name, age=age, gender=gender)

def get_value(name):
    API_LINK = "https://api.genderize.io"
    parameters = {
        "name": name
    }
    response = requests.get(url=API_LINK, params=parameters)
    response.raise_for_status()
    data = response.json()
    gender = data['gender']

    API_LINK = "https://api.agify.io"
    response = requests.get(url=API_LINK, params=parameters)
    response.raise_for_status()
    data = response.json()
    age = data['age']

    return gender, age
if __name__ == "__main__":
    app.run(debug=True)
