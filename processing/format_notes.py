import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load .env and get API key
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("❌ Gemini API key not found. Please check your .env file.")

genai.configure(api_key=API_KEY)


def format_with_gemini(raw_text):
    try:
        model = genai.GenerativeModel("models/gemini-1.5-flash")
        prompt = f"""
You are a smart AI note formatter. Convert this transcript into:
- Bullet points
- Tag each item like #idea, #task, #reminder

Transcript:
\"\"\"{raw_text}\"\"\"
"""
        response = model.generate_content(prompt)

        # Get the actual content from Gemini
        if hasattr(response, "text") and response.text:
            return response.text
        elif hasattr(response, "parts") and response.parts:
            return response.parts[0].text
        else:
            return ""

    except Exception as e:
        print("❌ Gemini API Error:", e)
        return ""


if __name__ == "__main__":
    with open("outputs/transcript.txt", "r", encoding="utf-8") as f:
        raw_text = f.read().strip()

    if not raw_text:
        print("❌ transcript.txt is empty. Please transcribe the audio first.")
    else:
        result = format_with_gemini(raw_text)

        if result.strip():
            with open("outputs/final_notes.md", "w", encoding="utf-8") as f:
                f.write(result.strip())
            print("✅ Final Notes saved to outputs/final_notes.md")
        else:
            print("⚠️ No output received from Gemini or response was empty.")
