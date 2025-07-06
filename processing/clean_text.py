import re
import nltk

nltk.download("punkt")
from nltk.tokenize import sent_tokenize


def clean_text(raw_text):

    fillers = ["um", "uh", "like", "you know", "so", "basically"]
    for filler in fillers:
        raw_text = re.sub(r"\b{}\b".format(filler), "", raw_text, flags=re.IGNORECASE)

    raw_text = re.sub(r"\s+", " ", raw_text).strip()

    sentences = sent_tokenize(raw_text)
    return sentences


if __name__ == "__main__":
    with open("outputs/transcript.txt", "r", encoding="utf-8") as f:
        raw_text = f.read()
    cleaned = clean_text(raw_text)
    for line in cleaned:
        print("•", line)
