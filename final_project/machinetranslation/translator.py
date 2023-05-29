"""
This module provides functions for translating text between English and French.
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

def english_to_french(english_text):
    """
    Translates English text to French using the IBM Watson Language Translator service.

    Parameters:
        english_text (str): The English text to be translated.

    Returns:
        str: The translated French text.

    Raises:
        ValueError: If the input text is null or empty.

    """
    if not english_text:
        raise ValueError("Input text cannot be null or empty.")
    
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    return translation.get("translations")[0].get("translation")

def french_to_english(french_text):
    """
    Translates French text to English using the IBM Watson Language Translator service.

    Parameters:
        french_text (str): The French text to be translated.

    Returns:
        str: The translated English text.

    Raises:
        ValueError: If the input text is null or empty.

    """
    if not french_text:
        raise ValueError("Input text cannot be null or empty.")
    
    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    return translation.get("translations")[0].get("translation")

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERSION = '2018-05-01'
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=VERSION,
    authenticator=authenticator
)

language_translator.set_service_url(url)
#print(english_to_french("hello"))
#print(french_to_english("merci"))
#print(french_to_english(""))