from gtts import gTTS
import uuid
import os

AUDIO_DIR = "app/audio"

os.makedirs(AUDIO_DIR, exist_ok=True)

def generate_tts(text: str):
    """
    Generates TTS audio file and returns the path.
    """

    if not text or text.strip() == "":
        return None

    filename = f"{uuid.uuid4()}.mp3"
    filepath = os.path.join(AUDIO_DIR, filename)

    tts = gTTS(text=text, lang="en")
    tts.save(filepath)

    return filepath
