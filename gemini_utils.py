import os
import google.generativeai as genai
from dotenv import load_dotenv

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

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content([system_prompt, text])
    return response.text
