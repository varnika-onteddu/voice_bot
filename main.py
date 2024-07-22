from voice_bot_sdk.sdk import VoiceBotSDK

if __name__ == "__main__":
    sttcon = {
        'engine': 'deepgram',
        'api_key': '****'
    }

    ttscon = {
        'engine': 'openai',
        'api_key': '****'
    }

    llmcon = {
        'engine': 'openai',
        'api_key': '****'
    }

    sdk = VoiceBotSDK(stt_config, tts_config, llm_config)
    sdk.stream_conversation()
