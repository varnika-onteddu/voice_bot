import time
from .stt import DeepgramSTT
from .tts import TTS
from .llm import LLM
from .audio_stream import PyAudioInputStream, PyAudioOutputStream

class VoiceBotSDK:
    def __init__(self, sttcon, ttscon, llmcon):
        self.stt = DeepgramSTT(sttcon['api_key'])
        self.tts = TTS(ttscon['engine'], ttscon['api_key'])
        self.llm = LLM(llmcon['api_key'], llmcon['system_prompt'])

    def stream_conversation(self):
        inp_str = PyAudioInputStream()
        oup_str = PyAudioOutputStream()

        while True:
            audio_chunk = inp_str.read()
            text = self.stt.transcribe_sync(audio_chunk)
            if text:
                print("Username:", text)
                response = self.llm.query(text)
                print(response)
                audio_response = self.tts.synthesize(response)
                oup_str.write(audio_response)
        inp_str.close()
        oup_str.close()
