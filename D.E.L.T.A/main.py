from flask import Flask, render_template, request, jsonify
from engine import get_coordinates_from_description
from reporter import generate_delta_report
import os

app = Flask(__name__)

# Ensure static folder exists for PDF storage
if not os.path.exists('static'):
    os.makedirs('static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    user_query = request.json.get('description')
    
    # Brain: Extract coords via Groq
    geo_data = get_coordinates_from_description(user_query)
    
    # Document: Generate the PDF
    pdf_filename = generate_delta_report(geo_data)
    
    return jsonify({
        "coords": {"lat": geo_data['lat'], "lng": geo_data['lng']},
        "pdf_url": pdf_filename
    })

if __name__ == '__main__':
    app.run(port=5000, debug=True)