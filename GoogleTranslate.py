import os
import requests
import pandas as pd

class Translator():
    def __init__(self):
        self.api_key = os.environ['GOOGLE_API_KEY']
        self.base_url = "https://translation.googleapis.com/language/translate/v2"
        self.language_codes = {'Afrikaans': 'af','Albanian': 'sq','Amharic': 'am','Arabic': 'ar','Armenian': 'hy','Assamese': 'as','Aymara': 'ay','Azerbaijani': 'az','Bambara': 'bm','Basque': 'eu','Belarusian': 'be','Bengali': 'bn','Bhojpuri': 'bho','Bosnian': 'bs','Bulgarian': 'bg','Catalan': 'ca','Cebuano': 'ceb','Chinese (Simplified)': 'zh-CN or zh (BCP-47)','Chinese (Traditional)': 'zh-TW (BCP-47)','Corsican': 'co','Croatian': 'hr','Czech': 'cs','Danish': 'da','Dhivehi': 'dv','Dogri': 'doi','Dutch': 'nl','English': 'en','Esperanto': 'eo','Estonian': 'et','Ewe': 'ee','Filipino (Tagalog)': 'fil','Finnish': 'fi','French': 'fr','Frisian': 'fy','Galician': 'gl','Georgian': 'ka','German': 'de','Greek': 'el','Guarani': 'gn','Gujarati': 'gu','Haitian Creole': 'ht','Hausa': 'ha','Hawaiian': 'haw','Hebrew': 'he or iw','Hindi': 'hi','Hmong': 'hmn','Hungarian': 'hu','Icelandic': 'is','Igbo': 'ig','Ilocano': 'ilo','Indonesian': 'id','Irish': 'ga','Italian': 'it','Japanese': 'ja','Javanese': 'jv or jw','Kannada': 'kn','Kazakh': 'kk','Khmer': 'km','Kinyarwanda': 'rw','Konkani': 'gom','Korean': 'ko','Krio': 'kri','Kurdish': 'ku','Kurdish (Sorani)': 'ckb','Kyrgyz': 'ky','Lao': 'lo','Latin': 'la','Latvian': 'lv','Lingala': 'ln','Lithuanian': 'lt','Luganda': 'lg','Luxembourgish': 'lb','Macedonian': 'mk','Maithili': 'mai','Malagasy': 'mg','Malay': 'ms','Malayalam': 'ml','Maltese': 'mt','Maori': 'mi','Marathi': 'mr','Meiteilon (Manipuri)': 'mni-Mtei','Mizo': 'lus','Mongolian': 'mn','Myanmar (Burmese)': 'my','Nepali': 'ne','Norwegian': 'no','Nyanja (Chichewa)': 'ny','Odia (Oriya)': 'or','Oromo': 'om','Pashto': 'ps','Persian': 'fa','Polish': 'pl','Portuguese (Portugal, Brazil)': 'pt','Punjabi': 'pa','Quechua': 'qu','Romanian': 'ro','Russian': 'ru','Samoan': 'sm','Sanskrit': 'sa','Scots Gaelic': 'gd','Sepedi': 'nso','Serbian': 'sr','Sesotho': 'st','Shona': 'sn','Sindhi': 'sd','Sinhala (Sinhalese)': 'si','Slovak': 'sk','Slovenian': 'sl','Somali': 'so','Spanish': 'es','Sundanese': 'su','Swahili': 'sw','Swedish': 'sv','Tagalog (Filipino)': 'tl','Tajik': 'tg','Tamil': 'ta','Tatar': 'tt','Telugu': 'te','Thai': 'th','Tigrinya': 'ti','Tsonga': 'ts','Turkish': 'tr','Turkmen': 'tk','Twi (Akan)': 'ak','Ukrainian': 'uk','Urdu': 'ur','Uyghur': 'ug','Uzbek': 'uz','Vietnamese': 'vi','Welsh': 'cy','Xhosa': 'xh','Yiddish': 'yi','Yoruba': 'yo','Zulu': 'zu'}

    def detect_language(self, query):
        url = f"{self.base_url}/detect"
        payload = {
            'q' : query,
            'key' : self.api_key
        }
        response = requests.post(url = url, data = payload)
        if response.status_code == 200:
            result = response.json()['data']
            languages = [detection[0]['language'] for detection in result['detections'] if detection]
            return ",".join(languages)
        else:
            print("No response from the API, check if service is enabled on https://console.developers.google.com/apis/api/translate.googleapis.com/overview?project=<project_id>")

    def code_to_language(self,lang_code):
        for k,v in self.language_codes.items():
            if v.lower() == lang_code.lower():
                return k
            else:
                pass

    def language_to_code(self,language):
        for k,v in self.language_codes.items():
            if k.lower() == language.lower():
                return v
            else:
                pass

    def translate(self,string,target):
        url = self.base_url
        payload = {
            'q' : string,
            'key' : self.api_key,
            'target' : target
        }
        response = requests.post(url = url, data = payload)
        if response.status_code == 200:
            data = response.json()['data']
            translations_info = [(translation['translatedText'], translation['detectedSourceLanguage']) for translation in data.get('translations', [])]
            return translations_info

