# 🌾 GramVaani – Voice-Enabled AI Assistant for Rural India

**GramVaani** (ग्रामवाणी) is a voice-first AI-powered web application designed to empower rural communities in India. It bridges the information gap by offering accessible, multilingual support across essential domains such as agriculture, healthcare, weather, and government schemes.

---

## 🧠 Project Idea

Built under the theme **"Smart Bharat"**, GramVaani is an intelligent assistant tailored for rural users. It integrates voice recognition, image processing, and real-time data APIs to provide seamless access to critical services and knowledge, even for users with limited literacy or internet literacy.

---

## 🌟 Key Features

- 🔊 **Voice Interface** (via Dialogflow) in regional Indian languages.
- 👩‍⚕️ **Healthcare Information** with admin-controlled updates.
- 📜 **Government Scheme Navigator** with eligibility checks.
- ☁️ **Weather Forecasts** using OpenWeatherMap API.
- 🌾 **Agricultural Advisory** based on crop and region.
- 🌿 **Visual Input Analysis**
  - Plant disease identification (via image processing).
  - Document reading and text-to-speech.
- 📱 **Augmented Reality Education** (e.g., medical procedures, farming techniques).

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python Flask
- **AI & NLP**: Dialogflow, Gemini
- **APIs**: OpenWeatherMap, Govt Schemes DB
- **Image Processing**: YOLOv10 / OpenCV
- **Speech**: Google Text-to-Speech / espeak (for embedded devices)
- **Others**: Raspberry Pi (for prototype), Flutter (for mobile interface)

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Flask
- `requests`, `opencv-python`, `speechrecognition`, `pyttsx3`, etc.
- Dialogflow agent setup
- OpenWeatherMap API key

### Installation

```bash
git clone https://github.com/yourusername/GramVaani.git
cd GramVaani
pip install -r requirements.txt
```
