import streamlit as st
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from processing.transcribe_audio import transcribe_audio
from processing.format_notes import format_with_gemini

st.title("NotesBuddyAI - Voice to Notes")
uploaded_file = st.file_uploader("Upload Audio (.mp3/.wav)", type=["mp3", "wav"])

if uploaded_file is not None:
    path = os.path.join("input", uploaded_file.name)
    with open(path, "wb") as f:
        f.write(uploaded_file.read())
    st.success("Audio Uploaded!")

    if st.button("Transcribe and Format"):
        raw = transcribe_audio(path)
        result = format_with_gemini(raw)
        st.markdown("### 📝 Final Notes")
        st.markdown(result)
