from voice_bot_sdk.sdk import VoiceBotSDK

if __name__ == "__main__":
    stt_config = {
        'engine': 'deepgram',
        'api_key': '****'
    }

    tts_config = {
        'engine': 'openai',
        'api_key': '****'
    }

    llm_config = {
        'engine': 'openai',
        'api_key': '****',
        'system_prompt': 'This is a Bot'
    }

    sdk = VoiceBotSDK(stt_config, tts_config, llm_config)
    sdk.stream_conversation()
