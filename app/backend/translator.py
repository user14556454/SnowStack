from pygoogletranslation import Translator

translator = Translator()

def translate_text(text: str, target_language: str) -> str:
    """
    Safe translation wrapper.
    Always returns a string.
    Never crashes Streamlit.
    """

    if not text or text.strip() == "":
        return "No OCR text found to translate."

    if not target_language:
        return "No target language selected."

    try:
        result = translator.translate(text, dest=target_language)
        translated_text = result.text

        if not translated_text:
            return "Translation failed: empty output."

        return translated_text

    except Exception as e:
        return f"Translation failed: {str(e)}"
