import weather as wt
import chatgpt as cg
import send_email as se
import json



if __name__ == "__main__":
    # get tomorrow's weather forcast
    weather = wt.Weather(wt.api_key, wt.base_url)
    tmr_weather = weather.get_ith_day_weather(1)  
    tmr_weather_str = json.dumps(tmr_weather)

    # ask chatgpt to give us tips of wearing clothes
    chat = cg.Chatbot(cg.api_Key)
    rec = chat.generate_text(tmr_weather_str)
    sender = se.Sender(se.account_sid,se.auth_token)
    sender.set_sms("+sender-phonenumber")
    sender.send_message(rec, "+receiver-phonenumber")

    