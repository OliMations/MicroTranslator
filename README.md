![GitHub release (latest by date)](https://img.shields.io/github/v/release/OliMations/MicroTranslator)
![PyPI](https://img.shields.io/pypi/v/MicroTranslator)
![GitHub repo size](https://img.shields.io/github/repo-size/OliMations/MicroTranslator)
![GitHub file size in bytes](https://img.shields.io/github/size/OliMations/MicroTranslator/src/microtranslator/translator.py)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/MicroTranslator)
![PyPI - Downloads](https://img.shields.io/pypi/dm/MicroTranslator)

# Microsoft Translate Wrapper
A lightweight, simple to use wrapper for the microsoft translate API that simply does the API call and returns the raw, unmanipulated result.

## Why Should I Use This?
It saves you time whilst adding no more code to your project than necessary

## Installation
Just run `pip install MicroTranslator` in your command prompt of choice (Eg. Windows CMD or Powershell)

## Setup
```python
from microtranslator import Translator

tr = Translator(client_key="key")
```

## Translate
```python
tr.translate("Hello World!", "de")
# [{'detectedLanguage': {'language': 'en', 'score': 1.0}, 'translations': [{'text': 'Hallo Welt!', 'to': 'de'}]}]
```

## Detect
```python
tr.detect("Hallo Welt!")
#[{'language': 'de', 'score': 1.0, 'isTranslationSupported': True, 'isTransliterationSupported': False}]
```

## Dictionary
```python
tr.dictionary("test", "it", "en")
# text, to lang, from lang

# [{'normalizedTarget': 'fuoco', 'displayTarget': 'fuoco', 'posTag': 'OTHER', 'confidence': 0.8043, 'prefixWord': '', 'backTranslations': 
#   [{'normalizedText': 'fire', 'displayText': 'fire', 'numExamples': 1, 'frequencyCount': 33741}, 
#    {'normalizedText': 'firing', 'displayText': 'firing', 'numExamples': 0, 'frequencyCount': 559}
#   ]
# }]
# etc...
```

## Languages
```python
tr.languages()

# {'af': {'name': 'Afrikaans', 'nativeName': 'Afrikaans', 'dir': 'ltr'}, 
#   'am': {'name': 'Amharic', 'nativeName': 'አማርኛ', 'dir': 'ltr'}}
# etc...
```

## See it in the wild
[View my discord bot](https://jakebot.co.uk) which uses this exact package for all the free translations!

## Have something to contribute?
Go ahead and make a pull request! I should always be around to review them!

## Issues?
[Make an issue!](https://github.com/OliMations/MicroTranslator/issues)
Try to add as much detail as possible, including screenshots and tracebacks are super useful
