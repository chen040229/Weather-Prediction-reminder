
from openai import OpenAI
from openai import APIError


api_Key = "fill your key"

class Chatbot:

    def __init__(self, api_key: str) -> None:
        self.name = 'weather bot'
        self.client = OpenAI(api_key=api_key)
    
    def generate_text(self, msg: str, role:str="user") -> str:
        try:
            completion = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": role, "content": "Give me suggestions based on the data below"},
                    {"role": role, "content": msg}
                ]
            )
            return completion.choices[0].message.content
        except APIError as e:
            print(f"Message:e.message")
                



if __name__ == "__main__":
    input = "is UCSD good school?"
    role = "user"
    robot = Chatbot(api_Key)
    print(robot.generate_text(input,role))





                              

    