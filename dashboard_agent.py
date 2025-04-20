import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
    system_instruction="You are a AI assitant name GamVaani who helps to automate tasks performed on a website which helps rural people.Now you have to return 'healthcare', 'agriculture' and 'weather'.Only answer in single word and output should be in english only. ",
    )

def generate_text(prompt):
    response = model.generate_content([
        "input: I want to know about the weather",
        "output: weather",
        "input: open weather",
        "output: weather",
        "input: मला हवामानाचा अंदाज द्या",
        "output: weather",
        "input: हवामान कसा आहे",
        "output: weather",
        "input: what is weather",
        "output: weather",
        "input: open healthcare",
        "output: health",
        "input: आरोग्य विभाग उघडा",
        "output: health",
        "input: मला आरोग्य बद्दल बोलायचा आहे",
        "output: health",
        "input: I want to know about hospitals",
        "output: health",
        "input: Open agriculture advisor",
        "output: agri",
        "input: मला कृषी सल्लागार उघडायचा आहे",
        "output: agri",
        "input: agriculture advisor",
        "output: agri",
        "input: कृषि विभाग उघडा",
        "output: agri",
        "input: कृषि बद्दल माहिती हवी आहे",
        "output: agri",
        "input: कृषि बद्दल बोलायचं आहे",
        "output: agri",
        f"input: {prompt}",
        "output: ",
        ])
    return response.text
