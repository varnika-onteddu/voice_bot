from deepgram import Deepgram
import asyncio
import aiohttp

class DeepgramSTT:
    def __init__(self, api_key):
        self.api_key = api_key

    def transcribe(self, audio_stream):
        with aiohttp.ClientSession() as session:        
            dg_client = Deepgram(self.api_key)
            source = {'buffer': audio_stream, 'mimetype': 'audio.mp3'}
            response = await dg_client.transcription.prerecorded(source, {'punctuate': True})

    def transcribe_sync(self, audio_stream):
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(self.transcribe(audio_stream))
