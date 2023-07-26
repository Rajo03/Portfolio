from googletrans import Translator

translator = Translator()

translation = translator.translate('Oa mai oe?', dest='en').text

print(translation)