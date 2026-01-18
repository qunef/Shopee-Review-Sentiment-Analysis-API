import re
import json

class TextPreprocessor:
    def __init__(self, slang_path='data/slang_dict.json'):
        # Contoh sederhana kamus slang
        self.slang_dict = {
            "bgt": "banget",
            "gk": "tidak",
            "jg": "juga",
            "mantap": "bagus"
        } 

    def clean_text(self, text):
        # 1. Lowercase
        text = text.lower()
        # 2. Hapus URL, Mention (@), dan Hashtag (#)
        text = re.sub(r'http\S+|@\S+|#\S+', '', text)
        # 3. Hapus karakter non-alfabet
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        # 4. Normalisasi kata slang
        words = text.split()
        normalized_words = [self.slang_dict.get(w, w) for w in words]
        return " ".join(normalized_words)