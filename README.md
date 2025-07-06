# 🎙️ NotesBuddyAI – Voice-to-Text Smart Notes App (Indian Accent Focus)

> A smart assistant that transcribes Indian-accented English audio into clean, structured, bullet-formatted notes using Whisper and Gemini — all using free APIs.

---

## 📌 Project Objective

Many Indian users prefer speaking over typing, but typical note apps fail to:
- Accurately transcribe Indian-accented speech
- Structure spoken thoughts into usable notes

**NotesBuddyAI** solves this by:
- Transcribing voice notes using Whisper
- Cleaning the raw transcript
- Formatting structured notes with Gemini (Google Generative AI)

---

## 🧰 Tech Stack (Free Tools)

| Layer              | Tool/Library                         |
|-------------------|--------------------------------------|
| Transcription      | [OpenAI Whisper](https://github.com/openai/whisper) |
| Audio Handling     | `pydub`, `ffmpeg`                    |
| Text Cleaning      | `nltk`, `re`                         |
| Note Formatting    | [Gemini 1.5 Flash (via API)](https://makersuite.google.com/) |
| UI (optional)      | `Streamlit`                          |
| Environment Vars   | `python-dotenv`                     |

---

## 🗂️ Project Structure

notesbuddyai/
├── input/ # Input voice files (.mp3/.wav)
│ └── sample_voice_note.mp3
├── outputs/ # Final output files
│ ├── transcript.txt # Raw transcript from Whisper
│ └── final_notes.md # Formatted smart notes
├── processing/ # Core processing scripts
│ ├── transcribe_audio.py # Transcribes audio to text
│ ├── clean_text.py # Removes fillers, cleans text
│ └── format_notes.py # Uses Gemini to format notes
├── app/ # (Optional) Streamlit UI
│ └── streamlit_ui.py
├── .env # API key for Gemini (not public)
└── README.md


---

## 🚀 How to Run

### ✅ Step 1: Clone and Set Up

```bash
git clone https://github.com/yourusername/notesbuddyai.git
cd notesbuddyai
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate
pip install -r requirements.txt

# If no requirements.txt, install manually:
pip install git+https://github.com/openai/whisper.git faster-whisper pydub nltk streamlit python-dotenv google-generativeai

```
### ✅ Step 2: Add Your Audio File

**input/sample_voice_note.mp3**

### ✅ Step 3: Add Gemini API Key

1.**Go to https://aistudio.google.com/app/apikey**

2.**Copy your API key.**

3.**Create a .env file:**
GEMINI_API_KEY=your_api_key_here

### ✅ Step 4: Run Processing Pipeline
```base
# Step 1: Transcribe audio to text
python processing/transcribe_audio.py

# Step 2: Format and save notes using Gemini
python processing/format_notes.py
```

**Output saved to:**

```base
outputs/final_notes.md
```

### 💻 Optional: Run Streamlit App

```base
streamlit run app/streamlit_ui.py
```
### ✅ Features

* **🎧 Accepts .mp3, .wav, .m4a files**

* **🧠 Accurate transcription of Indian-accented speech**

* **🧹 Cleans filler words (e.g., "um", "like")**

* **✨ Converts to structured bullet notes using Gemini**

* **🏷️ Adds tags like #task, #idea, #reminder**

* **📤 Saves to .md, .txt, and optional .json**

* **🖼️ Optional Streamlit upload interface**

### 🌟 Future Enhancements

* **Add Hindi-English (Hinglish) support**

* **Generate tags.json from LLM**

* **Export to Google Docs or Notion**

* **Build mobile version (Figma or React Native)**
