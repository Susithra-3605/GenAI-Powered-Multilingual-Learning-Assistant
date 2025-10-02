from transformers import pipeline

# Load translation models for supported languages
translation_models = {
    "hi": pipeline("translation", model="Helsinki-NLP/opus-mt-en-hi"),
    "ta": pipeline("translation", model="Helsinki-NLP/opus-mt-en-ta"),
    "te": pipeline("translation", model="Helsinki-NLP/opus-mt-en-te"),
    "kn": pipeline("translation", model="Helsinki-NLP/opus-mt-en-kn"),
    "ml": pipeline("translation", model="Helsinki-NLP/opus-mt-en-ml"),
}

qa_pipeline = pipeline("question-answering")
summarizer = pipeline("summarization")

def translate(text, target_lang):
    if target_lang in translation_models:
        return translation_models[target_lang](text)[0]['translation_text']
    return text
