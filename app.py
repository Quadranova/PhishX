from flask import Flask, render_template, request, jsonify
from google import genai
import os

app = Flask(__name__)

# --- CONFIGURATION ---
GEMINI_API_KEY = "ADD YOUR GEMINI API KEY HERE" 
client = genai.Client(api_key=GEMINI_API_KEY)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    user_text = data.get("text", "")
    selected_lang = data.get("language", "EN")

    lang_map = {'EN': 'English', 'HI': 'Hindi', 'KN': 'Kannada'}
    target_lang = lang_map.get(selected_lang, 'English')

    if not user_text.strip():
        return jsonify({"error": "No text provided"}), 400

    try:
        model_id = "gemini-2.5-flash"
        
        # PROMPT: Structured for the new 2-column card layout and Pentagon Graph
        prompt = f"""
        You are 'PhishX AI'. Analyze this text: "{user_text}"
        
        Provide your analysis in this EXACT structure:
        
        🔍 ANALYSIS:
        - [Point 1]
        - [Point 2]
        
        🚩 WARNING SIGNS:
        - [Point 1]
        - [Point 2]
        
        🛡️ PROTECTION:
        - [Point 1]
        - [Point 2]
        
        METRICS:
        Urgency: [0-100]
        Technical: [0-100]
        Social: [0-100]
        Trust: [0-100]
        Intent: [0-100]
        
        SCORE: [0-100]

        INSTRUCTIONS: 
        1. Write the content of ANALYSIS, WARNING SIGNS, and PROTECTION in {target_lang}.
        2. Keep the headers in English.
        3. Be objective. Routine texts = low score.
        """
        
        response = client.models.generate_content(model=model_id, contents=prompt)
        full_output = response.text

        # Extract Metrics for the Pentagon Graph
        metrics = {"urgency": 50, "technical": 50, "social": 50, "trust": 50, "intent": 50}
        try:
            for key in metrics.keys():
                if key.capitalize() + ":" in full_output:
                    val = full_output.split(key.capitalize() + ":")[1].split('\n')[0]
                    metrics[key] = int(''.join(filter(str.isdigit, val)))
        except: pass

        # Extract Score
        score = 50
        if "SCORE:" in full_output:
            try:
                score_str = full_output.split("SCORE:")[1].strip()
                score = int(''.join(filter(str.isdigit, score_str)))
            except: pass

        # Clean analysis for UI display (Removing Metrics and Score lines)
        clean_text = full_output.split("METRICS:")[0].strip()

        return jsonify({
            "score": score, 
            "analysis": clean_text,
            "metrics": metrics
        })

    except Exception as e:
        return jsonify({"score": 60, "analysis": "Error in Analysis.", "metrics": metrics})

if __name__ == '__main__':
    app.run(debug=True)
