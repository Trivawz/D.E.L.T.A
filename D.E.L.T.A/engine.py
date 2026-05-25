import os
from groq import Groq
import json

# Replace 'YOUR_NEW_KEY_HERE' with your actual new gsk_... key
client = Groq(api_key="API_KEY_HERE") 

def get_coordinates_from_description(description):
    prompt = f"""
    ANALYSIS TASK: Geospatial Signature Extraction.
    TARGET: {description}
    
    Extract the most probable Latitude and Longitude. 
    If a specific city is mentioned, use its center. 
    If a 'vibe' is described (e.g., 'hidden valley'), use coordinates for a known real-world analog.
    
    OUTPUT ONLY VALID JSON:
    {{
        "lat": float,
        "lng": float,
        "confidence": int,
        "analysis": "Provide a brief tactical reason for this match."
    }}
    """
    
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile",
        response_format={"type": "json_object"}
    )
    
    return json.loads(chat_completion.choices[0].message.content)