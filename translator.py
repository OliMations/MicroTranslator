import requests, uuid, logging
logger = logging.getLogger('MicroTranslator')


class TranslatorException(Exception):
    def __init__(self, code, message, *args):
        self.code = code
        self.message = message
        super(TranslatorException, self).__init__('%d-%s' % (self.code, self.message), *args)

class Translator():
    """
    Keyword Arguments:
    ------------------
    * `client_key` -- Your API key, obtained from the azure dashboard
    * `location` -- not required, defaults to global    
    """
    def __init__(self, client_key, location="global"):
        self.auth_token = client_key
        self.location = location

    def translate(self, text, to_lang, from_lang=None):
        """
        Translate from one language to 1+ languages

        Keyword Arguments:
        ------------------
        * `text` -- The text to actually translate
        * `from_lang` -- the language to translate from, dont put anything
        (or put None) to use auto detection
        * `to_lang` -- The languages to translate to, can supply a list
        to return several translations

        Returns 
        -----------------
        A list of dictionary object containing the translations, relevant langauges
        and confidence (if detect language was used)
        """

        params = {
            "api-version": "3.0",
            "to": to_lang
        }
        if from_lang != None: 
            params["from"] = from_lang
        
        constructed_url = "translate"
        return self.sendOff(constructed_url, params, payload=text)
        

    def detect(self, text):
        """
        Detect the language in the string

        Keyword Arguments:
        ------------------
        * `text` -- the string you want to detect

        Returns
        ------------------
        The language detected, the confidence of the detection,
        whether that language can be translated
        """

        constructed_url = 'detect?api-version=3.0'
        return self.sendOff(constructed_url, payload=text)

    def sendOff(self, constructed_url="", params="", payload="", get=False):
        """Not meant to be accessed"""
        baseUrl = "https://api.cognitive.microsofttranslator.com/"
        constructed_url = baseUrl + constructed_url

        headers = {
            'Ocp-Apim-Subscription-Key': self.auth_token,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4()),
            'Ocp-Apim-Subscription-Region': self.location,
        }
        body = [{
            'text' : payload
        }]
        
        if get == True: request = requests.get(constructed_url, headers=headers, params=params, json=body)
        else: request = requests.post(constructed_url, headers=headers, params=params, json=body)
        response = request.json()
        if "error" in response:
            error = response['error']
            raise TranslatorException(error['code'], error['message'])
        return(response)

    def languages(self):
        """
        Get a list of all the languages available

        Returns
        -----------
        A json object of the language codes, paired with the language name
        anglicised and native
        """

        constructed_url = 'languages?api-version=3.0&scope=translation'
        return self.sendOff(constructed_url, get=True)["translation"]
    
    def dictionary(self, word, to_lang, from_lang):
        """
        Gets all possible translations for the word

        Keyword Arguments:
        ------------------
        * `word` -- The word to actually translate. Can not be longer than
        100 characters
        * `from_lang` -- the language to translate from, this system does not
        include built in automatic translation, use the detect function
        for that
        * `to_lang` > The languages to translate to.

        Returns
        -----------------
        A list of possible translations for the word provided,
        as well as whether the translated word is a verb, adjective etc.
        And importantly CONFIDENCE. Although this will return several results
        there is a high chance a load of them are completely wrong so I would
        advise only displaying results with a confidence of 0.7 and over
        """

        path = '/dictionary/lookup?api-version=3.0'
        constructed_url = path + f"&from={from_lang}&to={to_lang}"
        return self.sendOff(constructed_url, payload=word)[0]["translations"]