import openai

class TTS:
    def __init__(self, engine, api_key):
        self.engine = engine
        self.api_key = api_key
        if engine == "openai":
            openai.api_key = api_key

    def synthesize(self, text):
        if self.engine == "openai":
            response = openai.Audio.create(text=text, model="text-to-speech")
            return response['data']
