import requests
import os
from dotenv import load_dotenv

load_dotenv()
GOOGLE_TRANSLATE_API_KEY = os.getenv("GOOGLE_TRANSLATE_API_KEY")

def translate_text(text, target_language='en', source_language=None):
    """
    Translate text using Google Translate API v2 with API Key.
    
    :param text: Text to translate
    :param target_language: Target language code (e.g., 'en', 'hi')
    :param source_language: Source language code (or None to auto-detect)
    :return: Translated text
    """
    url = "https://translation.googleapis.com/language/translate/v2"
    
    params = {
        'q': text,
        'target': target_language,
        'key': GOOGLE_TRANSLATE_API_KEY
    }
    
    # Only add 'source' if it's explicitly provided
    if source_language:
        params['source'] = source_language

    response = requests.post(url, data=params)

    if response.status_code == 200:
        result = response.json()
        return result['data']['translations'][0]['translatedText']
    else:
        print("Error:", response.status_code, response.text)
        return None


print(translate_text("Hello, how are you?", target_language="hi"))  # English to Hindi
print(translate_text("तू कसा आहेस?", target_language="en"))        # Marathi to English