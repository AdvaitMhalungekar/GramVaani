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
def chat_weather(chat):
  weather_data = get_weather_data("Kolhapur")
  model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction=f"This is weather forecast for next 3 days :\n{weather_data}\nyou have to asnwer  questions based on this data in short",
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

  print(response.text)
  
while True:
  chat = input("Enter your question: ")
  chat_weather(chat)