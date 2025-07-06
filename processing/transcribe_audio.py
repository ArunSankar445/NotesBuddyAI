import whisper
import os


def transcribe_audio(audio_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    with open("outputs/transcript.txt", "w", encoding="utf-8") as f:
        f.write(result["text"])
    return result["text"]


if __name__ == "__main__":
    audio_path = "input/sample_voice_note.mp3"
    text = transcribe_audio(audio_path)
    print("Transcription Complete!")
