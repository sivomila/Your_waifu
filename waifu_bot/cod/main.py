import telebot
import requests
import  random
from cod import  animelist
from cod import  config
from cod import prognoz
from bs4 import BeautifulSoup as BS
from telebot import types

bot = telebot.TeleBot(config.token)

#погода
def weath(message):
    city = message.text
    bot.send_message(message.chat.id, 'Так, что там у нас?')
    bot.send_sticker(message.chat.id, 'CAACAgEAAxkBAAPwXwuKitqwqGhbXDn9JCdqKq_yL3MAAr0AA39Zegfz9u6YUxvWyxoE')
    r = requests.get('https://sinoptik.ua/погода-'+ str(city)+'/')
    html = BS(r.content, 'html.parser')
    for el in html.select('#content'):
        t_min = el.select('.temperature .min')[0].text
        t_max = el.select('.temperature .max')[0].text
        text = el.select('.wDescription .description')[0].text
    bot.send_message(message.chat.id,"На сегодня погода в городе " + str(city)+ " обстоит так:\n" + t_min + ', ' + t_max + '\n' + text)
    bot.send_message(message.chat.id, 'Хозяин, что нибудь еще?')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Слушаю вас, хозяин.')
    bot.send_sticker(message.chat.id, 'CAACAgEAAxkBAAMHXwoZA9xUdCOnZN2wk7eQa08PqzQAAjYBAAJ_WXoHqoTMvvhz4YEaBA')
    bot.send_message(message.chat.id, 'Если не знаете с чего начать, отправьте мне "/help"')

@bot.message_handler(commands=['help'])
def send_text(message):
    bot.send_message(message.chat.id, 'Хозяин, пока что могу ответить на следующие ваши запросы: \n1)аниме. (Выберу из своих любимых)\n2)погода.(Узнаешь погоду в своем городе)\n3)гороскоп.(Узнаешь что тебя ожидает в этом месяце)\nТак же не забывай о вежливости "привет" и "прощай"! ')
    bot.send_sticker(message.chat.id, 'CAACAgEAAxkBAANdXwsqQmaEJoQT4GmOZ_UWsQPNYxMAAtgBAAJ_WXoHZygYUneZJDoaBA')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'аниме':
        msg = animelist.L[random.randint(0,35)]
        bot.send_message(message.chat.id, msg)
        bot.send_message(message.chat.id, 'Приятного просмотра!')
    elif message.text.lower() == 'погода':
        city = bot.send_message(message.chat.id, "В каком городе вам показать погодку?")
        bot.register_next_step_handler(city, weath)
    elif message.text.lower() == 'гороскоп':
        keyboard = types.InlineKeyboardMarkup()
        key_oven = types.InlineKeyboardButton(text='Овен', callback_data='oven')
        keyboard.add(key_oven)
        key_telec = types.InlineKeyboardButton(text='Телец', callback_data='telec')
        keyboard.add(key_telec)
        key_bliznecy = types.InlineKeyboardButton(text='Близнецы', callback_data='blizneci')
        keyboard.add(key_bliznecy)
        key_rak = types.InlineKeyboardButton(text='Рак', callback_data='rak')
        keyboard.add(key_rak)
        key_lev = types.InlineKeyboardButton(text='Лев', callback_data='lev')
        keyboard.add(key_lev)
        key_deva = types.InlineKeyboardButton(text='Дева', callback_data='deva')
        keyboard.add(key_deva)
        key_vesy = types.InlineKeyboardButton(text='Весы', callback_data='vesi')
        keyboard.add(key_vesy)
        key_scorpion = types.InlineKeyboardButton(text='Скорпион', callback_data='skorpion')
        keyboard.add(key_scorpion)
        key_strelec = types.InlineKeyboardButton(text='Стрелец', callback_data='strelec')
        keyboard.add(key_strelec)
        key_kozerog = types.InlineKeyboardButton(text='Козерог', callback_data='kozerog')
        keyboard.add(key_kozerog)
        key_vodoley = types.InlineKeyboardButton(text='Водолей', callback_data='vodoley')
        keyboard.add(key_vodoley)
        key_ryby = types.InlineKeyboardButton(text='Рыбы', callback_data='ribi')
        keyboard.add(key_ryby)
        bot.send_message(message.from_user.id, text='Я забыла ваш знак зодиака... Можете мне напомнить?',reply_markup=keyboard)
    elif message.text.lower() == 'привет':
        bot.send_message(message.chat.id, "Привет. Я рада что вы вернулись!")
        bot.send_sticker(message.chat.id, 'CAACAgEAAxkBAAICRV8Lv6tpgZOsaNHDfSnY7DPxZYUjAAIyAQACf1l6B2LeEZ66E2ceGgQ')
    elif message.text.lower() == 'прощай':
        bot.send_message(message.chat.id, "До встречи.")
        bot.send_sticker(message.chat.id, 'CAACAgEAAxkBAAICTV8Lv9T75Gj2HWBz6N9OX-jGG0UNAAK8AQACf1l6Bz7wIprXdBt0GgQ')
    else:
        bot.send_message(message.from_user.id, 'Простите, я пока еще этого не знаю. Используйте только мои знания.')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIBtF8Lr-sqKTQAASzugq5CDgN7uTNZQwACYAADzGguDgr63zDtxpdOGgQ')

#обработчик кнопок
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "oven":
        msg = prognoz.oven
        bot.send_message(call.message.chat.id, msg)
        bot.send_message(call.message.chat.id, 'Что-нибудь еще? ')
    elif call.data == "telec":
         msg = prognoz.telec
         bot.send_message(call.message.chat.id, msg)
         bot.send_message(call.message.chat.id, 'Что-нибудь еще? ')
    elif call.data == "blizneci":
        msg = prognoz.blizneci
        bot.send_message(call.message.chat.id, msg)
        bot.send_message(call.message.chat.id, 'Что-нибудь еще? ')
    elif call.data == "rak":
         msg = prognoz.rak
         bot.send_message(call.message.chat.id, msg)
         bot.send_message(call.message.chat.id, 'Что-нибудь еще? ')
    elif call.data == "lev":
         msg = prognoz.lev
         bot.send_message(call.message.chat.id, msg)
         bot.send_message(call.message.chat.id, 'Что-нибудь еще? ')
    elif call.data == "deva":
         msg = prognoz.deva
         bot.send_message(call.message.chat.id, msg)
         bot.send_message(call.message.chat.id, 'Что-нибудь еще? ')
    elif call.data == "vesi":
         msg = prognoz.vesi
         bot.send_message(call.message.chat.id, msg)
         bot.send_message(call.message.chat.id, 'Что-нибудь еще? ')
    elif call.data == "skorpion":
         msg = prognoz.skorpion
         bot.send_message(call.message.chat.id, msg)
         bot.send_message(call.message.chat.id, 'Что-нибудь еще? ')
    elif call.data == "strelec":
         msg = prognoz.strelec
         bot.send_message(call.message.chat.id, msg)
         bot.send_message(call.message.chat.id, 'Что-нибудь еще? ')
    elif call.data == "kozerog":
         msg = prognoz.kozerog
         bot.send_message(call.message.chat.id, msg)
         bot.send_message(call.message.chat.id, 'Что-нибудь еще? ')
    elif call.data == "vodoley":
         msg = prognoz.vodoley
         bot.send_message(call.message.chat.id, msg)
         bot.send_message(call.message.chat.id, 'Что-нибудь еще? ')
    elif call.data == "ribi":
        msg = prognoz.ribi
        bot.send_message(call.message.chat.id, msg)
        bot.send_message(call.message.chat.id, 'Что-нибудь еще? ')

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling(none_stop=True, interval=0)
