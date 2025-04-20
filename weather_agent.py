import os
import google.generativeai as genai
from weather_fetcher import get_weather_data

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
history= []
  

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
def chat_weather(chat, return_text=False):
    weather_data = get_weather_data("Kolhapur")
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        
        system_instruction=f"This is weather forecast for next 3 days :\n{weather_data}\nyou have to answer questions based on this data in short.\n Act as professional weather and agriculture advisor",
    )
    history.append({
        "role": "user",
        "parts": [
            chat
        ],
    })

    chat_session = model.start_chat(
        history=history,
    )

    response = chat_session.send_message(chat)
    
    if return_text:
        return response.text
    else:
        print(response.text)
        return response.text