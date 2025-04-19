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
def chat_health(chat, return_text=False):
    weather_data = get_weather_data("Kolhapur")
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        system_instruction=f"You are a farm advisor chatbot. User will tell about their issues or doubts in farming and you have to provide guidance and suggestions. You can also give answer based on the weather data. Talk in short as if you are chating. Weather data: {weather_data}",
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
        
