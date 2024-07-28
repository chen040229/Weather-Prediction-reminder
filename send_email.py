from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException


# Your Account SID and Auth Token from console.twilio.com
account_sid = "your own sid"
auth_token  = "your own token"




class Sender:

    def __init__(self,sid,token) -> None:
        self.client = Client(sid, token)

    def set_sms(self, number: str):
        self.number = number

    def set_email_addr(self, addr: str):
        self.addr = addr

    def send_message(self, msg: str, receiver: str):
        try:
            if self.number is None or len(self.number) == 0:
                print("The sender number is not set yet!")
                return
            message = self.client.messages.create(
                to  = receiver,
                from_= self.number,
                body= msg)
            pass
            
            
        except TwilioRestException as e:
            print(e)
        
        
        
