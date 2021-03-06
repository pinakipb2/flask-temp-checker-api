#Made with https://www.weatherbit.io/
from flask import Flask, render_template, flash, make_response, url_for, request, redirect,flash
import requests

app = Flask(__name__)
app.secret_key = 'bgc/di.[o;,lyog-/[min06edbh/['

@app.route('/', methods=['GET','POST'])
def index():
    temp = None
    place = None
    if request.method == "POST":
        place = request.form['place']
        r = requests.get('https://api.weatherbit.io/v2.0/current?city='+place+'&key=your_api_key_here')
        try:
            json_object = r.json()
            for item in json_object['data']:
                temp = float(item['app_temp'])
        except:
            flash('Please Enter a Correct Place!','warning')
    return render_template('index.html', temp=temp,place=place)


if __name__ == '__main__':
    app.run(debug=True)
