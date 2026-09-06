from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route('/api/assess-hazard', methods=['GET'])
def assess_hazard():
    lat = float(request.args.get('lat', 0))
    lon = float(request.args.get('lon', 0))
    
    # Generate risk metrics & comparison baselines
    risk_score = round(random.uniform(0.1, 0.95), 2)
    risk_percent = int(risk_score * 100)
    slope_deg = round(random.uniform(5.0, 45.0), 1)
    
    rainfall_mm = round(random.uniform(30.0, 150.0), 1)
    normal_rainfall_mm = 30.0  # Safe baseline
    
    water_depth_cm = round(random.uniform(10.0, 100.0), 1)
    normal_water_depth_cm = 20.0  # Safe baseline
    
    status = "HIGH" if risk_score > 0.5 else "SAFE"
    
    return jsonify({
        "status": status,
        "risk_score": risk_score,
        "risk_percent": risk_percent,
        "slope_deg": slope_deg,
        "rainfall_mm": rainfall_mm,
        "normal_rainfall_mm": normal_rainfall_mm,
        "water_depth_cm": water_depth_cm,
        "normal_water_depth_cm": normal_water_depth_cm,
        "lat": lat,
        "lon": lon
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)