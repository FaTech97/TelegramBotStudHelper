from Include.Clases.Schedule import Schedule
from Include.Clases.Teacher import Teacher
# import telebot
# from telebot import apihelper
#
# bot = telebot.TeleBot("1092665729:AAFDr9DHOWeqAvavIh2vMhiNEq4RvteMBm0")
#
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	bot.reply_to(message, "Howdy, how are you doing?")
#
# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
# 	bot.reply_to(message, message.text)
#
# bot.polling()
schedule = Schedule()
# teacher = Teacher
schedule.getDataFromJSON()

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	bot.reply_to(message, "Howdy, how are you doing?")
#
# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
    # strSum = ''
    # if(str(message) == 'Олег какие пары'):
    #     strSum = schedule.searchDay().showAllLessons()
# 	bot.reply_to(message, message.text)
#
# bot.polling()
    #
    #     schedule.searchDay().showAllLessons()
    # if(a == 2):
    #     schedule.searchDay().timeBeforeNextLeson()
    # if(a == 3):
    #     name = str(input('Фамилия препода: \n'))
    #     teacher.getTeacherFullName(name)
    # if(a == 4):
    #     break
    # print("\n")

schedule.searchDay().showAllLessons()