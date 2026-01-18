from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

class SentimentModel:
    def __init__(self):
        model_name = "crypter70/IndoBERT-Sentiment-Analysis" 

        self.nlp = pipeline(
            "sentiment-analysis",
            model=model_name,
            tokenizer=model_name
        )

    def predict(self, text):
        result = self.nlp(text)
        # result contoh: [{'label': 'positive', 'score': 0.99}]
        return result[0]