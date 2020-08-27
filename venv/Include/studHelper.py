from Include.Clases.Schedule import Schedule
from Include.Clases.Teacher import Teacher
import telebot
from telebot import apihelper
from telebot import types

bot = telebot.TeleBot("1092665729:AAFDr9DHOWeqAvavIh2vMhiNEq4RvteMBm0")
schedule = Schedule()
teacher = Teacher
schedule.getDataFromJSON()

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are doing?")


@bot.message_handler(commands=['олег'])
def echo_all(message):
	addKeyboard(message)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == 'олег':
	    addKeyboard(message)

def addKeyboard(message):
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Узнать рассписание', callback_data='rasp');
    keyboard.add(key_yes);
    key_next = types.InlineKeyboardButton(text='Что и через сколько пара?', callback_data='para');
    keyboard.add(key_next);
    key_day = types.InlineKeyboardButton(text='Какие пары сегодня?', callback_data='day');
    keyboard.add(key_day);
    key_no = types.InlineKeyboardButton(text='Имя преподавателя', callback_data='prep');
    keyboard.add(key_no);
    bot.send_message(message.chat.id, text='Что вы хотите?', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):

    if call.data == "day":
        text = '@{0}\n{1} {2}, сегодня следующие пары:\n {3}'.format(
            call.from_user.username, call.from_user.first_name, call.from_user.last_name, schedule.searchDay().showAllLessons())
        bot.send_message(call.message.chat.id, text);
    elif call.data == "rasp":
        text = '@{0}\n{1} {2}, ваше расписание:\n {3}'.format(
            call.from_user.username, call.from_user.first_name, call.from_user.last_name,schedule.getAllRaps());
        bot.send_message(call.message.chat.id, text );
    elif call.data == "para":
        text = '@{0}\n{1} {2}, {3}'.format(
            call.from_user.username, call.from_user.first_name, call.from_user.last_name,schedule.searchDay().timeBeforeNextLeson());
        bot.send_message(call.message.chat.id, text);
    elif call.data == "prep":
        bot.send_message(call.message.chat.id, 'Пока не умею((((((');

bot.polling()

# print(schedule.getAllRaps())