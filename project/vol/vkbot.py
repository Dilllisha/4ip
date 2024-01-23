import random

import vk_api
from vk_api.utils import get_random_id
from vk_api.longpoll import *
from vk_api.keyboard import *
from pyowm.owm import OWM
from datetime import datetime
import openai

def bot():
    print("Volodya")
    session = vk_api.VkApi(token="vk1.a.9wLYO2cuHKbWPZtWC51ssEzH12w-BIa_urRqKMM2E23COzqiWAZK8jOVPBeaVXHcWWDKCINwYg96pl0p_zw6uqMXfiddkTfu_ES7hgHydHfxgYbZrjv6jreK_qGM7Mf0DavzFaZFQIdzObNHPRM4X1pdxmZxu6fcDLvGKlGTperd3inqh6LYY9vHmVBWmwk4zl8Bb4iKYHWqiA-GkCgxYg")
    longpoll = VkLongPoll(session)
    vk = session.get_api()
    openai.api_key = 'sk-zydahm'+'FVX9X6u'+'GG4iFAP'+'T3BlbkFJE'+'yoeKpApu'+'UOWC09ZDej1'
    owm = OWM('d6901b7f0e58a81b6e3b55dc1f85fb1e')
    mgr = owm.weather_manager()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    
    
    def sender(id, msg, keyboard=None):
    
        post = {
            "user_id": id,
            "message": msg,
            "random_id": random_id,
        }
    
        if keyboard != None:
            post["keyboard"] = keyboard.get_keyboard()
        else:
            post = post
    
        session.method("messages.send", post)
    
    
    print("Бот запущен -", current_time)
    
    def gpt(text):
        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {'role': 'user', 'content': text}
                ],
                temperature=0
            )
            sender(user_id, response.choices[0].message.content)
        except:
            sender(user_id, "что-то пошло не так")
    
    
    def weathers(text):
        try:
            observation = mgr.weather_at_place(text)
            w = observation.weather
            temperature = w.temperature('celsius')['temp']
            weather = w.status.lower()
            wind = w.wind()['speed']
            humi = w.humidity
            if weather == "snow":
                weather = "снег"
            elif weather == "clouds":
                weather = "облачно"
            elif weather == "rain":
                weather = "дождь"
    
            ad = (f"По запросу города {text} найдено:\n Температура: {temperature}℃"
                  f"\n Погода: {weather}\n Ветер: {wind} м/с\n Влажность: {humi}%")
            sender(user_id, ad)
        except:
            sender(user_id, "Не получилось найти погоду по вашему городу")
    
    chat_gpt_button = False
    weather_button = False
    
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            text = event.text.lower()
            user_id = event.user_id
            random_id = random.getrandbits(64)
    
            if not chat_gpt_button:
                if text == "привет":
                    sender(user_id, "Здарова")
    
                elif text == "меню":
                    keyboard = VkKeyboard(inline=True)
                    buttons = ["Погода", "gpt"]
                    buttons_colors = [VkKeyboardColor.PRIMARY, VkKeyboardColor.NEGATIVE]
                    for btn, btn_color in zip(buttons, buttons_colors):
                        keyboard.add_button(btn, btn_color)
                    sender(user_id, "Выберите что-то из предложенного списка", keyboard)
    
                elif text == "погода":
                    sender(user_id, "Введите название города")
                    weather_button = True
    
                elif weather_button:
                    if text != 'погода':
                        weathers(text)
                        weather_button = False
    
                elif text == "gpt":
                    sender(user_id, "Здравствуйте, вы можете задать любой вопрос боту chat-gpt. Для завершения диалога с ботом напишите 'стоп' ")
                    chat_gpt_button = True
    
                elif text == "шумерля":
                    weathers(text)
    
                else:
                    sender(user_id, "Не понимаю о чем вы")
    
            if chat_gpt_button:
                if text != "gpt":
                    if text != "стоп":
                        gpt(text)
                if text == "стоп":
                    chat_gpt_button = False
                    sender(user_id, "Вы закончили диалог с ботом chat-gpt")
