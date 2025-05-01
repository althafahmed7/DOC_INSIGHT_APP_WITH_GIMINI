import os
import google.generativeai as genai
from dotenv import load_dotenv
import google.api_core.exceptions as google_exceptions

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

def extract_fields_from_text(text):
    system_prompt = """
You are a smart assistant that extracts structured fields from contract or invoice text. 
Return your response as JSON in this format:

{
  "party_names": "",
  "payment_terms": "",
  "obligations": "",
  "deadlines": "",
  "risks": ""
}
"""

    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content([system_prompt, text])
        return response.text

    except google_exceptions.DeadlineExceeded:
        return '{"error": "⏱️ Gemini API timed out. Please try again later."}'
    except Exception as e:
        return f'{{"error": "❌ Gemini API failed: {str(e)}"}}'
