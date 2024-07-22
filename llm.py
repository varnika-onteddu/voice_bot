import openai

class LLM:
    def __init__(self, api_key, sys_prmpt):
        openai.api_key = api_key
        self.sys_prmpt = sys_prmpt

    def query(self, user_input):
        response = openai.Completion.create(
            engine="davinci",
            prompt=self.sys_prmpt + user_input + "\n",
            max_tokens=150
        )
        return response.choices[0].text.strip()
