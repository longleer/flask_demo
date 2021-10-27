from flask import Flask, render_template
import json

app = Flask(__name__,static_url_path='')

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/info')
def json_file():
    file = open(r'C:\Users\lenovo\PycharmProjects\flask_demo\json_dataa.json')
    json_data = json.load(file)
    return json_data



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=4900)
