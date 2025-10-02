def cultural_example(language: str) -> str:
    examples = {
        "hi": "एकता में बल है (Unity is strength)",
        "ta": "கற்றது கைமண் அளவு (What we know is a handful of sand)",
        "te": "నిద్రపోతే పాము కాటు (If you sleep, a snake may bite)",
        "kn": "ಹಣ್ಣು ಹಣ್ಣಿಗೆ ರುಚಿ (Each fruit has its own taste)",
        "ml": "അറിവിന് അതിരുകളില്ല (Knowledge has no boundaries)"
    }
    return examples.get(language, "Learning makes you wise!")
