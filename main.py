import telebot
import requests
from flask import Flask
from threading import Thread

# --- جزء السيرفر الوهمي لإرضاء Koyeb ---
app = Flask('')
@app.route('/')
def home():
    return "I am alive!"

def run():
    app.run(host='0.0.0.0', port=8000)

def keep_alive():
    t = Thread(target=run)
    t.start()
# --------------------------------------

API_TOKEN = '8463740745:AAEywm4g4XHrOXOR7mSqrsN2WFduL6Sog6Q'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك! البوت شغال الآن بنجاح على Koyeb 🚀")

@bot.message_handler(func=lambda message: 'tiktok.com' in message.text)
def handle_tiktok(message):
    url = message.text
    try:
        api_url = f"https://www.tikwm.com/api/?url={url}"
        response = requests.get(api_url).json()
        if response.get('code') == 0:
            video_url = response['data']['play']
            bot.send_video(message.chat.id, video_url)
    except:
        bot.reply_to(message, "حدث خطأ في التحميل.")

if __name__ == "__main__":
    keep_alive() # تشغيل السيرفر الوهمي
    print("البوت بدأ العمل...")
    bot.infinity_polling()
