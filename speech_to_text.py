import speech_recognition as sr

recognizer = sr.Recognizer()

def speech_to_text(lang='en-IN'):
    with sr.Microphone() as source:
        print("🎤 Speak something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            # Specify the language code (e.g., 'hi-IN' for Hindi, 'mr-IN' for Marathi)
            text = recognizer.recognize_google(audio, language  =lang)
            print("📝 You said (in Hindi):", text)
        except sr.UnknownValueError:
            print("❌ Could not understand audio")
        except sr.RequestError as e:
            print(f"⚠️ Could not request results; {e}")
