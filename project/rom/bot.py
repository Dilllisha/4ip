import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api import VkUpload
from datetime import datetime
from vk_api.utils import get_random_id

def botik():
    print("Romik")
    vk_token = "vk1.a.Jx9Hqyr4HIjGO5QHHrF0bIlTsiNFB2Bv5Jdxm9bNsOBa9dvIUCECnv2cA9SjGyFGhkR8dRojqrHIUjw8gUga8QtACMHNZ656r4HKK_b_hhufu17cUn20XumQ4zll2aetLgFxttiwWx-o1c4Oy-YHdGna1BTxdj9oDOIfAvSAmZqqQ9aIc_ux4rRtL77T2mFAqP0TAuz-aD0ICXRrfdiImQ"
    
    
    ssession = vk_api.VkApi(token=vk_token)
    longpolll = VkLongPoll(ssession)
    noww = datetime.now()
    cur = noww.strftime("%H:%M")
    print("бот запущен", cur)
    
    def send(user, textt, keyb=None):
        post = {
                "user_id": user,
                "message": textt,
                "random_id": 0,
    
        }
    
        if keyb != None:
            post["keyboard"] = keyb.get_keyboard()
        else:
            post = post
    
        ssession.method("messages.send", post)
    for event in longpolll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            textt = event.text.lower()
            user = event.user_id
    
            if textt == "привет":
                # attachments = []
                # upload_image = upload.photo_messages(photos=image)[0]
                # attachments.append('photo{}_{}'.format(upload_image['owner_id'], upload_image['id']))
                send(user, "хай")
    
            elif textt == "меню":
    
                keyboard = VkKeyboard()
                #keyboard.add_location_button()
                #keyboard.add_line()
    
                button = ["Что ты умеешь?","blue","red"]
                button_colors = [VkKeyboardColor.POSITIVE,VkKeyboardColor.PRIMARY,VkKeyboardColor.NEGATIVE]
    
                for btn, btn_color in zip(button,button_colors):
                    keyboard.add_button(btn, btn_color)
    
                send(user, "Выберите что вам нужно:", keyboard)
    
            elif textt == "что ты умеешь?":
    
                keyb = VkKeyboard()
    
                button = ["Что 1", "2", "3"]
                button_colors = [VkKeyboardColor.POSITIVE, VkKeyboardColor.PRIMARY, VkKeyboardColor.NEGATIVE]
    
                for bt, bt_color in zip(button,button_colors):
                    keyb.add_button(bt, bt_color)
    
                send(user, "Я умею..", keyb)
    
            else:
    
                send(user, "Я вас не понимаю",)



