from gtts import gTTS
import playsound
import os

def text_to_speech(text, lang='en'):
    try:
        # Create TTS object
        tts = gTTS(text=text, lang=lang, slow=False)

        # Save to file
        filename = "output.mp3"
        tts.save(filename)

        # Play the file
        playsound.playsound(filename)

        # Optional: remove the file after playing
        os.remove(filename)
    except Exception as e:
        print("❌ Error:", e)


