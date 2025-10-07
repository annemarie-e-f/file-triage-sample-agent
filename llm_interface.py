from transformers import pipeline

# Build a simple text classification LLM interface using Hugging Face's free models
class LLMInterface:
    def __init__(self):
        # Using distilbert-base-uncased-finetuned-sst-2-english for demonstration (intent classification)
        self.classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

    def parse_intent(self, user_input):
        # For a real agent, you'd fine-tune or use a multi-label classifier for intents
        # Here we'll just demonstrate sentiment as a placeholder
        result = self.classifier(user_input)
        return result[0]["label"]
