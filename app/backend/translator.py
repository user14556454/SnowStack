from pygoogletranslation import Translator

# 1. Instantiate the Translator object
translator = Translator()

original_text = input("Enter the text to translate: ")
c = input("Enter the target language code (e.g., 'es', 'fr', 'en'): ")

try:
    # 2. Call the translate method
    result_object = translator.translate(original_text, dest=c)
    
    # 3. Access the text attribute
    final_result = result_object.text

    print(f"\nThe following is your generated text: {final_result}")

except Exception as e:
    print(f"\nTranslation Failed. Error: {e}")