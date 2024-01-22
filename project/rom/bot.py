import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api import VkUpload
from datetime import datetime
from vk_api.utils import get_random_id

def botik():
    token = "vk1.a.Jx9Hqyr4HIjGO5QHHrF0bIlTsiNFB2Bv5Jdxm9bNsOBa9dvIUCECnv2cA9SjGyFGhkR8dRojqrHIUjw8gUga8QtACMHNZ656r4HKK_b_hhufu17cUn20XumQ4zll2aetLgFxttiwWx-o1c4Oy-YHdGna1BTxdj9oDOIfAvSAmZqqQ9aIc_ux4rRtL77T2mFAqP0TAuz-aD0ICXRrfdiImQ"
    image = "D:/python/Mihaylov/photo/menu.png"
    
    
    session = vk_api.VkApi(token=token)
    longpoll = VkLongPoll(session)
    upload = VkUpload(session)
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    welcome = ["хай", "привет", "ку", "yo"]
    print("бот запущен", current_time)
    
    def sender(id, text, keyboard=None):
        post = {
                "user_id": id,
                "message": text,
                "random_id": 0,
    
        }
    
        if keyboard != None:
            post["keyboard"] = keyboard.get_keyboard()
        else:
            post = post
    
        session.method("messages.send", post)
    
    
    def sender_photo(id, text ):
        post = {
            "user_id": id,
            "message": text,
            "random_id": 0,
            "attachment": ','.join(attachments)
    
        }
        session.method("messages.send", post)
    
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            text = event.text.lower()
            user_id = event.user_id
    
            if text in welcome:
                attachments = []
                upload_image = upload.photo_messages(photos=image)[0]
                attachments.append('photo{}_{}'.format(upload_image['owner_id'], upload_image['id']))
                sender_photo(user_id, "хай")
    
            elif text == "меню":
    
                keyboard = VkKeyboard()
                #keyboard.add_location_button()
                #keyboard.add_line()
    
                button = ["Что ты умеешь?","blue","red"]
                button_colors = [VkKeyboardColor.POSITIVE,VkKeyboardColor.PRIMARY,VkKeyboardColor.NEGATIVE]
    
                for btn, btn_color in zip(button,button_colors):
                    keyboard.add_button(btn, btn_color)
    
                sender(user_id, "Выберите что вам нужно:", keyboard)
    
            elif text == "что ты умеешь?":
    
                keyboard = VkKeyboard()
    
                button = ["Что 1", "2", "3"]
                button_colors = [VkKeyboardColor.POSITIVE, VkKeyboardColor.PRIMARY, VkKeyboardColor.NEGATIVE]
    
                for btn, btn_color in zip(button,button_colors):
                    keyboard.add_button(btn, btn_color)
    
                sender(user_id, "Я умею..", keyboard)
    
            else:
    
                sender(user_id, "Я вас не понимаю",)



