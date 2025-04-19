'''
import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("🎤 Speak something...")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

    try:
        # Specify the language code (e.g., 'hi-IN' for Hindi, 'mr-IN' for Marathi)
        text = recognizer.recognize_google(audio, language  ='mr-IN')
        print("📝 You said (in marathi):", text)
    except sr.UnknownValueError:
        print("❌ Could not understand audio")
    except sr.RequestError as e:
        print(f"⚠ Could not request results; {e}")
      
        
        
from deep_translator import GoogleTranslator

src_lang = 'mr'
text ="माझे नाव संध्या आहे"

def translate_text(text, src_lang, tgt_lang):
     if src_lang == tgt_lang:
        print(text)
     try:
        print( GoogleTranslator(source=src_lang, target=tgt_lang).translate(text))
     except:
        print( text)
    
new_text =translate_text(text, src_lang, 'en')
print(new_text)
'''

import pyttsx3
tts_engine = pyttsx3.init()

text='books'

def speak_text(text, lang='mr'):
    for voice in tts_engine.getProperty('voices'):
        if lang in voice.id.lower() or lang in voice.name.lower():
            tts_engine.setProperty('voice', voice.id)
            break
    tts_engine.say(text)
    tts_engine.runAndWait()

speak_text(text)