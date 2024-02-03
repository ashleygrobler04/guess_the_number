import json


class Translator:
    def __init__(self):
        self.cache = {}

    def load(self, lang):
        if lang in self.cache:
            return self.cache[lang]

        try:
            with open(f"{lang}.json") as f:
                translation_data = json.load(f)
                self.cache[lang] = translation_data
                return translation_data
        except FileNotFoundError as e:
            raise FileNotFoundError(
                f"Error: Translation file '{lang}.json' not found.")

    def translate(self, key, lang, **kwargs):
        translation_data = self.load(lang)
        phrase_translated = translation_data.get(
            key, f"{key} not available in {lang}")

        try:
            phrase_translated = phrase_translated.format(**kwargs)
            return phrase_translated
        except KeyError as e:
            raise KeyError(
                f"Error: Missing placeholder value for {e} in the translation of '{key}' ({lang}).")
        except IndexError as e:
            raise IndexError(
                f"Error: Index out of range in the translation of '{key}' ({lang}). Check placeholder count.")
