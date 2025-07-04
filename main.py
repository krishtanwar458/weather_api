from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/API/v1/<station>/<date>')
def about(station, date):
    df = pd.read_csv('data.csv')
    temprature = df.station(date)
    return {'station': station, 
            'date': date, 
            'temprature': temprature}


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)