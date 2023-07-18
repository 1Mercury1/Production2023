from flask import Flask, render_template, request
import requests

# границы импортированных данных
bllat = 59.634 # bottom left latitude
bllon = 29.525

trlat = 60.24 # top right latitude
trlon = 30.798 

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/submit_coordinates', methods=['GET'])
def submit_coordinates():
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')

    lat_num = float(latitude)
    lon_num = float(longitude)

    if(lat_num > trlat or lat_num < bllat or lon_num > trlon or lon_num < bllon):
        return "Заданные координаты за пределами Санкт-Петербурга"

    nominatim_reverse_url = f'http://localhost:80/nominatim/reverse?lat={latitude}&lon={longitude}&format=json&addressdetails=1'
    response = requests.request("Get", nominatim_reverse_url).json()
    
    return response['display_name']

if __name__ == '__main__':
    app.run(debug=True)