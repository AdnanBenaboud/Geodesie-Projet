from flask import Flask, render_template, url_for, request, jsonify
from Operations import GeoPosition, WGS84, Clarke_1880, CartPosition
import math as m

clarke80 = Clarke_1880()
wgs84 = WGS84()

def minTodeg(min):
    return min / 60

def secTodeg(sec):
    return sec / 3600

def degTorad(ang):
    return ang*(m.pi/180)

def radTodeg(ang):
    return ang*(180/m.pi)

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.get_json()
        if 'formType' in data:
            form_Type = data['formType']

            if form_Type == 'GeoToCart':
                phi_degree = float(data['phiDegree'])
                phi_min = float(data['phiMin'])
                phi_sec = float(data['phiSec'])
                phi_direction = str(data['phiDirection'])
                lambda_degree = float(data['lambdaDegree'])
                lambda_min = float(data['lambdaMin'])
                lambda_sec = float(data['lambdaSec'])
                lambda_direction = str(data['lambdaDirection'])
                h = float(data['hValue'])
                ellipsoide = str(data['ellipsoide'])

                phiFinal = degTorad(phi_degree + minTodeg(phi_min) + secTodeg(phi_sec))
                lambdaFinal = degTorad(lambda_degree + minTodeg(lambda_min) + secTodeg(lambda_sec))

                if phi_direction == 'S':
                    phiFinal = -phiFinal

                if lambda_direction == 'W':
                    lambdaFinal = -lambdaFinal 

                geoposition = GeoPosition(phiFinal, lambdaFinal, h)

                if ellipsoide == 'Clarke 1880':
                    X, Y, Z = clarke80.geoToCart(geoposition)
                    return jsonify({'X': X, 'Y': Y, 'Z': Z})
                
                else :
                    X, Y, Z = wgs84.geoToCart(geoposition)
                    print(X,Y,Z)
                    return jsonify({'X': X, 'Y': Y, 'Z': Z})
                
            elif form_Type == 'CartToGeo':
                X_input = float(data['xInput'])
                Y_input = float(data['yInput'])
                Z_input = float(data['zInput'])
                ellipsoide = str(data['ellipsoide'])

                cartposition = CartPosition(X_input,Y_input,Z_input)
                if ellipsoide == 'Clarke 1880':
                    phi_result, lambda_result, h_result = clarke80.CartToGeo(cartposition)
                    return jsonify({'phiResult': phi_result, 'lambdaResult': lambda_result, 'hResult': h_result})
                
                else :
                    phi_result, lambda_result, h_result = wgs84.CartToGeo(cartposition)
                    return jsonify({'phiResult': phi_result, 'lambdaResult': lambda_result, 'hResult': h_result})



    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run()
