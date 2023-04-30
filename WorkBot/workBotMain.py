import telebot
from datetime import datetime
import os
from telebot import types 
from . import distributionAlgorithm 
from datetime import datetime

def dataChange(basedir, IDforChange, lineNumberToChange, replacementText):

    replacementText = replacementText + str(hex(lineNumberToChange)) +"\n"

    with open(str(basedir) + r'/Storage/workers/' + str(IDforChange)+ ".txt", 'r', encoding='utf-8') as file:              
        for i in range(lineNumberToChange):
            lineToChange = file.readline()
        file.close()
    
    with open (str(basedir) + r'/Storage/workers/' + str(IDforChange)+".txt", 'r', encoding='utf-8') as f:
        old_data = f.read()
    
    new_data = old_data.replace(lineToChange, replacementText)
    
    with open (str(basedir) + r'/Storage/workers/' + str(IDforChange) + ".txt", 'w', encoding='utf-8') as f:
        f.write(new_data)


def dataRecieve(basedir, IDforRecieve, lineNumberToRecieve):

    file = open(str(basedir) + r'/Storage/workers/' + str(IDforRecieve)+".txt", 'r', encoding='utf-8')
    for i in range(lineNumberToRecieve):
        lineToReturn = file.readline()
    file.close()

    lineToReturn = lineToReturn.replace("\n","")
    lineToReturn = lineToReturn.replace(str(hex(lineNumberToRecieve)), "")
    return lineToReturn 


def categoryMenu(basedir, message, bot):

    dataChange(basedir, message.from_user.id, 2, "edit menu")
    dataChange(basedir, message.from_user.id, 4, "неизвестное имя блюда")
    dataChange(basedir, message.from_user.id, 5, "неизвестная граммовка блюда")
    dataChange(basedir, message.from_user.id, 6, "неизвестная цена блюда")

    log  = (str(datetime.now()) + ' Редактируется меню пользователем рабочего бота с ID: ' + str(message.from_user.id) + '\n')

    logs = open(str(basedir) + r'/Storage/logs.txt', 'a')
    logs.write(log)
    logs.close()

    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=False)
    btn1 = types.KeyboardButton("◀ назад")
    keyboard.row(btn1)

    bot.send_message(message.chat.id, text= "..." .format(message.from_user), reply_markup=keyboard)

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    
    #дальше начинается жопа но я хз как сделать по другому)
    
    filenames = []
    amount = 0

    for root, dirs, files in os.walk(basedir + r"/Storage/images"):  
        for dirname in dirs:

            amount += 1
            filenames.append(dirname)

    listPosition = 0
    
    if (amount >= 1):
        add1 = types.InlineKeyboardButton(text=filenames[listPosition], callback_data = filenames[listPosition])
        listPosition += 1
        if (amount == 1):
            keyboard.add(add1)

    if (amount >= 2):
        add2 = types.InlineKeyboardButton(text=filenames[listPosition], callback_data = filenames[listPosition])
        listPosition += 1
        if (amount == 2):
            keyboard.add(add1,add2)

    if (amount >= 3):
        add3 = types.InlineKeyboardButton(text=filenames[listPosition], callback_data = filenames[listPosition])
        listPosition += 1
        if (amount == 3):
            keyboard.add(add1,add2,add3)

    if (amount >= 4):
        add4 = types.InlineKeyboardButton(text=filenames[listPosition], callback_data = filenames[listPosition])
        listPosition += 1
        if (amount == 4):
            keyboard.add(add1,add2,add3,add4)

    if (amount >= 5):
        add5 = types.InlineKeyboardButton(text=filenames[listPosition], callback_data = filenames[listPosition])
        listPosition += 1
        if (amount == 5):
            keyboard.add(add1,add2,add3,add4,add5)

    if (amount >= 6):
        add6 = types.InlineKeyboardButton(text=filenames[listPosition], callback_data = filenames[listPosition])
        listPosition += 1
        if (amount == 6):
            keyboard.add(add1,add2,add3,add4,add5,add6)
    
    if (amount >= 7):
        add7 = types.InlineKeyboardButton(text=filenames[listPosition], callback_data = filenames[listPosition])
        listPosition += 1
        if (amount == 7):
            keyboard.add(add1,add2,add3,add4,add5,add6,add7)

    if (amount >= 8):
        add8 = types.InlineKeyboardButton(text=filenames[listPosition], callback_data = filenames[listPosition])
        listPosition += 1
        if (amount == 8):
            keyboard.add(add1,add2,add3,add4,add5,add6,add7,add8)

    if (amount >= 9):
        add9 = types.InlineKeyboardButton(text=filenames[listPosition], callback_data = filenames[listPosition])
        listPosition += 1
        if (amount == 9):
            keyboard.add(add1,add2,add3,add4,add5,add6,add7,add8,add9)

    if (amount >= 10):
        add10 = types.InlineKeyboardButton(text=filenames[listPosition], callback_data = filenames[listPosition])
        listPosition += 1
        if (amount == 10):
            keyboard.add(add1,add2,add3,add4,add5,add6,add7,add8,add9,add10)

    if (amount >= 11):
        add11 = types.InlineKeyboardButton(text=filenames[listPosition], callback_data = filenames[listPosition])
        listPosition += 1
        if (amount == 11):
            keyboard.add(add1,add2,add3,add4,add5,add6,add7,add8,add9,add10,add11)

    if (amount >= 12):
        add12 = types.InlineKeyboardButton(text=filenames[listPosition], callback_data = filenames[listPosition])
        listPosition += 1
        if (amount == 12):
            keyboard.add(add1,add2,add3,add4,add5,add6,add7,add8,add9,add10,add11,add12)

    if (amount >= 13):
        add13 = types.InlineKeyboardButton(text=filenames[listPosition], callback_data = filenames[listPosition])
        listPosition += 1
        if (amount == 13):
            keyboard.add(add1,add2,add3,add4,add5,add6,add7,add8,add9,add10,add11,add12,add13)

    if (amount >= 14):
        add14 = types.InlineKeyboardButton(text=filenames[listPosition], callback_data = filenames[listPosition])
        listPosition += 1
        if (amount == 14):
            keyboard.add(add1,add2,add3,add4,add5,add6,add7,add8,add9,add10,add11,add12,add13,add14)

    add = types.InlineKeyboardButton(text="➕ Добавить категорию", callback_data = str("create category"))
    keyboard.add(add)

    dataChange(basedir, message.from_user.id, 3, "пункт меню неизвестен")

    bot.send_message(message.chat.id, text= "Категории для редактирования:" .format(message.from_user), reply_markup=keyboard)

def editCategory(basedir, message, bot):
    log  = (str(datetime.now()) + ' Редактируется категория ' + message.data +' пользователем рабочего бота с ID: ' + str(message.from_user.id) + '\n')

    logs = open(str(basedir) + r'/Storage/logs.txt', 'a', encoding='utf-8')
    logs.write(log)
    logs.close()

    dataChange(basedir, message.from_user.id, 2, "edit category")
    dataChange(basedir, message.from_user.id, 3, message.data)

    dataChange(basedir, message.from_user.id, 4, "неизвестное имя блюда")
    dataChange(basedir, message.from_user.id, 5, "неизвестная граммовка блюда")
    dataChange(basedir, message.from_user.id, 6, "неизвестная цена блюда")

    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=False)

    btn1 = types.KeyboardButton("➕ Добавить блюдо")
    btn2 = types.KeyboardButton("◀ к категориям")
    btn3 = types.KeyboardButton("◀ назад")
    btn4 = types.KeyboardButton("🗑 удалить эту категорию")

    keyboard.row(btn4)
    keyboard.row(btn1,btn2)
    keyboard.row(btn3)

    bot.send_message(message.from_user.id, text="⬇️ Удалите или добавьте блюдо ⬇️", reply_markup=keyboard)
    dirname = message.data

    keyboard = types.InlineKeyboardMarkup(row_width=2)

    for root, dirs, files in os.walk(basedir + r"/Storage/images/" + dirname):  
        for filename in files:

            file = open(str(basedir) + r'/Storage/images/'+ dirname +"/"+ filename , "rb")

            callbackData = filename

            filename = filename.replace(".jpg","")
            name = filename.partition('!') [0]
                                
            filename = filename.partition('!') [2]
            grams = filename.partition('!')[0]
            rubles = filename.partition('!')[2]

            keyboard.add(types.InlineKeyboardButton(text="Удалить: " + name + " " + grams + "Г " + "/ "+ rubles + "РУБ", callback_data = callbackData))

            bot.send_photo(message.from_user.id, file, reply_markup=keyboard)

            keyboard = types.InlineKeyboardMarkup(row_width=2)
            file.close()

def editPromotion(basedir,message,bot):
    dataChange(basedir, message.from_user.id, 2, "edit promotion")

    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=False)
    btn1 = types.KeyboardButton("🗑 удалить акцию")
    btn2 = types.KeyboardButton("◀ назад")
                    
    if (os.path.isfile(str(basedir) + r'/Storage/promotion.txt')) == True:
        keyboard.row(btn1)

    keyboard.row(btn2)

    if (os.path.isfile(str(basedir) + r'/Storage/promotion.txt')) == True:
        with open(str(basedir) + r'/Storage/promotion.txt', 'r', encoding='utf-8') as file:
            promotion = file.read()
            bot.send_message(message.chat.id, text= "Текущая акция: \n\n" + promotion .format(message.from_user), reply_markup=keyboard)
        bot.send_message(message.chat.id, text= "⬇️ Напишите новую акцию ⬇️" .format(message.from_user), reply_markup=keyboard)

    else:
        bot.send_message(message.chat.id, text= "⬇️ Напишите акцию ⬇️" .format(message.from_user), reply_markup=keyboard)

def editBusinessLunch(basedir, message, bot):
    dataChange(basedir, message.from_user.id, 2, "edit business lunch")

    log  = (str(datetime.now()) + ' Редактируется бизнес-ланч пользователем рабочего бота с ID: ' + str(message.from_user.id) + '\n')

    logs = open(str(basedir) + r'/Storage/logs.txt', 'a')
    logs.write(log)
    logs.close()

    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=False)
    btn1 = types.KeyboardButton("◀ назад")
    btn2 = types.KeyboardButton("🗑 удалить всё")
    keyboard.row(btn1,btn2)

    bot.send_message(message.from_user.id, text= "..." .format(message.from_user), reply_markup=keyboard)
    bot.send_message(message.from_user.id, text= "⬇️ Настройте бизнес-ланч ⬇️" .format(message.from_user), reply_markup=keyboard)

    filenames = []
    for root, dirs, files in os.walk(basedir + r"/Storage/businessLunch/soups"):  
        for filename in files:
            filenames.append(filename)

    keyboard = types.InlineKeyboardMarkup(row_width=1)
    if(len(filenames) == 1):
        btn1 = types.InlineKeyboardButton(text = "Удалить: " + filenames[0], callback_data = r"/soups/" + filenames[0])
        keyboard.add(btn1)
    elif(len(filenames) == 2):
        btn1 = types.InlineKeyboardButton(text = "Удалить: " + filenames[0], callback_data = r"/soups/" + filenames[0])
        btn2 = types.InlineKeyboardButton(text = "Удалить: " + filenames[1], callback_data = r"/soups/" + filenames[1])
        keyboard.add(btn1,btn2)
    if(len(filenames) < 2):
        btn3 = types.InlineKeyboardButton(text = "➕ Добавить суп", callback_data = "addSoups")
        keyboard.add(btn3)
    bot.send_message(message.from_user.id, text= "‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n                        Супы:\n______________________________" .format(message.from_user), reply_markup=keyboard)
    
    filenames = []
    for root, dirs, files in os.walk(basedir + r"/Storage/businessLunch/firstCourse"):  
        for filename in files:
            filenames.append(filename)

    keyboard = types.InlineKeyboardMarkup(row_width=1)
    if(len(filenames) == 1):
        btn1 = types.InlineKeyboardButton(text = "Удалить: " + filenames[0], callback_data = r"/firstCourse/" + filenames[0])
        keyboard.add(btn1)
    elif(len(filenames) == 2):
        btn1 = types.InlineKeyboardButton(text = "Удалить: " + filenames[0], callback_data = r"/firstCourse/" + filenames[0])
        btn2 = types.InlineKeyboardButton(text = "Удалить: " + filenames[1], callback_data = r"/firstCourse/" + filenames[1])
        keyboard.add(btn1,btn2)
    if(len(filenames) < 2):
        btn3 = types.InlineKeyboardButton(text = "➕ Добавить горячее", callback_data = "addFirstCourse")
        keyboard.add(btn3)
    bot.send_message(message.from_user.id, text= "‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n                      Горячее:\n______________________________" .format(message.from_user), reply_markup=keyboard)

    filenames = []
    for root, dirs, files in os.walk(basedir + r"/Storage/businessLunch/garnish"):  
        for filename in files:
            filenames.append(filename)

    keyboard = types.InlineKeyboardMarkup(row_width=1)
    if(len(filenames) == 1):
        btn1 = types.InlineKeyboardButton(text = "Удалить: " + filenames[0], callback_data = r"/garnish/" + filenames[0])
        keyboard.add(btn1)
    elif(len(filenames) == 2):
        btn1 = types.InlineKeyboardButton(text = "Удалить: " + filenames[0], callback_data = r"/garnish/" + filenames[0])
        btn2 = types.InlineKeyboardButton(text = "Удалить: " + filenames[1], callback_data = r"/garnish/" + filenames[1])
        keyboard.add(btn1,btn2)
    if(len(filenames) < 2):
        btn3 = types.InlineKeyboardButton(text = "➕ Добавить гарнир", callback_data = "addGarnish")
        keyboard.add(btn3)
    bot.send_message(message.from_user.id, text= "‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n                      Гарниры:\n______________________________" .format(message.from_user), reply_markup=keyboard)

    filenames = []
    for root, dirs, files in os.walk(basedir + r"/Storage/businessLunch/salad"):  
        for filename in files:
            filenames.append(filename)

    keyboard = types.InlineKeyboardMarkup(row_width=1)
    if(len(filenames) == 1):
        btn1 = types.InlineKeyboardButton(text = "Удалить: " + filenames[0], callback_data = r"/salad/" + filenames[0])
        keyboard.add(btn1)
    elif(len(filenames) == 2):
        btn1 = types.InlineKeyboardButton(text = "Удалить: " + filenames[0], callback_data = r"/salad/" + filenames[0])
        btn2 = types.InlineKeyboardButton(text = "Удалить: " + filenames[1], callback_data = r"/salad/" + filenames[1])
        keyboard.add(btn1,btn2)
    if(len(filenames) < 2):
        btn3 = types.InlineKeyboardButton(text = "➕ Добавить салат", callback_data = "addSalad")
        keyboard.add(btn3)
    bot.send_message(message.from_user.id, text= "‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n                      Салаты:\n______________________________" .format(message.from_user), reply_markup=keyboard)

    filenames = []
    for root, dirs, files in os.walk(basedir + r"/Storage/businessLunch/bread"):  
        for filename in files:
            filenames.append(filename)

    keyboard = types.InlineKeyboardMarkup(row_width=1)
    if(len(filenames) == 1):
        btn1 = types.InlineKeyboardButton(text = "Удалить: " + filenames[0], callback_data = r"/bread/" + filenames[0])
        keyboard.add(btn1)
    elif(len(filenames) == 2):
        btn1 = types.InlineKeyboardButton(text = "Удалить: " + filenames[0], callback_data = r"/bread/" + filenames[0])
        btn2 = types.InlineKeyboardButton(text = "Удалить: " + filenames[1], callback_data = r"/bread/" + filenames[1])
        keyboard.add(btn1,btn2)
    if(len(filenames) < 2):
        btn3 = types.InlineKeyboardButton(text = "➕ Добавить хлеб", callback_data = "addBread")
        keyboard.add(btn3)
    bot.send_message(message.from_user.id, text= "‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n                       Хлеба:\n______________________________" .format(message.from_user), reply_markup=keyboard)

    filenames = []
    for root, dirs, files in os.walk(basedir + r"/Storage/businessLunch/drink"):  
        for filename in files:
            filenames.append(filename)

    keyboard = types.InlineKeyboardMarkup(row_width=1)
    if(len(filenames) == 1):
        btn1 = types.InlineKeyboardButton(text = "Удалить: " + filenames[0], callback_data = r"/drink/" + filenames[0])
        keyboard.add(btn1)
    elif(len(filenames) == 2):
        btn1 = types.InlineKeyboardButton(text = "Удалить: " + filenames[0], callback_data = r"/drink/" + filenames[0])
        btn2 = types.InlineKeyboardButton(text = "Удалить: " + filenames[1], callback_data = r"/drink/" + filenames[1])
        keyboard.add(btn1,btn2)
    if(len(filenames) < 2):
        btn3 = types.InlineKeyboardButton(text = "➕ Добавить напиток", callback_data = "addDrink")
        keyboard.add(btn3)
    bot.send_message(message.from_user.id, text= "‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n                      Напитки:\n______________________________" .format(message.from_user), reply_markup=keyboard)

def workBot(basedir):
    
    password = ""
    print("Рабочий бот запущен")
    userDataLayout = "статус неизвестен\nдействие неизвестно\nпункт меню неизвестен\nнеизвестное имя блюда\nнеизвестная граммовка блюда\nнеизвестная цена блюда\n"


    workToken = ""
    bot = telebot.TeleBot(workToken)

    userToken = ""
    userBot = telebot.TeleBot(userToken)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    @bot.message_handler(commands='start')
    def start_message(message):
        
        print("Рабочий | " + str(datetime.now())+ " | " + str(message.from_user.id) + " | "+ str(message.text))
        
        log  = (str(datetime.now()) + ' Нажат старт пользователем с ID: ' + str(message.from_user.id) + '\n')

        logs = open(str(basedir) + r'/Storage/logs.txt', 'a')
        logs.write(log)
        logs.close()

        if (os.path.isfile(str(basedir) + r'/Storage/workers/' + str(message.from_user.id) + ".txt")) != True:

            file = open(str(basedir) + r'/Storage/workers/' + str(message.from_user.id) + ".txt", 'a', encoding='utf-8')
            file.write(userDataLayout)
            file.close()
            
            dataChange(basedir, message.from_user.id, 1, "noname")

            log  = (str(datetime.now()) + ' Создан пользователь рабочего бота с ID: ' + str(message.from_user.id) + '\n')

            logs = open(str(basedir) + r'/Storage/logs.txt', 'a')
            logs.write(log)
            logs.close()

        if (dataRecieve(basedir, message.from_user.id, 1) != "admin"):
            bot.send_message(message.chat.id, text= "❗️ Введите пароль для доступа ❗️" .format(message.from_user), reply_markup=markup)
            dataChange(basedir, message.from_user.id, 2, "enters password")

    @bot.message_handler(content_types=['text'])
    def main(message):
        
        print("Рабочий | " + str(datetime.now())+ " | " + str(message.from_user.id) + " | "+ str(message.text))
        
        if (os.path.isfile(str(basedir) + r'/Storage/workers/' + str(message.from_user.id) + ".txt")) != True:
            bot.send_message(message.chat.id, text= "❗️ Неидентифицированный пользователь ❗️" .format(message.from_user), reply_markup=markup)
            bot.send_message(message.chat.id, text= "❗️ Нажмите /start для идентификации ❗️" .format(message.from_user), reply_markup=markup)

            log  = (str(datetime.now()) + ' Неидентифицированый пользователь с ID: ' + str(message.from_user.id) + '\n')

            logs = open(str(basedir) + r'/Storage/logs.txt', 'a')
            logs.write(log)
            logs.close()

        else:
            if (dataRecieve(basedir, message.from_user.id, 1) == "admin"):

                if(message.text == "◀ назад" and dataRecieve(basedir, message.from_user.id, 2) != "main page"):

                    dataChange(basedir, message.from_user.id, 2, "main page")
                    dataChange(basedir, message.from_user.id, 3, "пункт меню неизвестен")

                    dataChange(basedir, message.from_user.id, 4, "неизвестное имя блюда")
                    dataChange(basedir, message.from_user.id, 5, "неизвестная граммовка блюда")
                    dataChange(basedir, message.from_user.id, 6, "неизвестная цена блюда")

                    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=False)

                    btn1 = types.KeyboardButton("Статистика")
                    btn2 = types.KeyboardButton("Бизнес-ланч")
                    btn3 = types.KeyboardButton("Меню")
                    btn4 = types.KeyboardButton("Создать рассылку")
                    btn5 = types.KeyboardButton("Акции")

                    keyboard.row(btn1)
                    keyboard.row(btn2,btn3)
                    keyboard.row(btn4)
                    keyboard.row(btn5)

                    bot.send_message(message.chat.id, text= "⬇ используйте кнопки ⬇" .format(message.from_user), reply_markup=keyboard)

                elif(message.text == "◀ к категориям" and (dataRecieve(basedir, message.from_user.id, 2) == "edit category" 
                      or dataRecieve(basedir, message.from_user.id, 2) =="create name" 
                      or dataRecieve(basedir, message.from_user.id, 2) =="create gramm"
                      or dataRecieve(basedir, message.from_user.id, 2) =="create ruble"
                      or dataRecieve(basedir, message.from_user.id, 2) =="create image")):
                    categoryMenu(basedir,message,bot)

                elif(message.text == "🗑 удалить эту категорию" and (dataRecieve(basedir, message.from_user.id, 2) == "edit category"
                    or dataRecieve(basedir, message.from_user.id, 2) =="create name" 
                    or dataRecieve(basedir, message.from_user.id, 2) =="create gramm"
                    or dataRecieve(basedir, message.from_user.id, 2) =="create ruble"
                    or dataRecieve(basedir, message.from_user.id, 2) =="create image")):

                    folderName = dataRecieve(basedir, message.from_user.id, 3)

                    for root, dirs, files in os.walk(basedir + r"/Storage/images/" + folderName):  
                        for filename in files:
                            os.remove(basedir + r"/Storage/images/" + folderName + "/" + filename)

                    os.rmdir(basedir + r"/Storage/images/" + folderName)

                    distributionAlgorithm.distribution(basedir,folderName)
                    os.rmdir(basedir + r"/Storage/imagesForClients/" + folderName)

                    log  = (str(datetime.now()) + ' Удалена категория '+ folderName +' пользователем рабочего бота с ID: ' + str(message.from_user.id) + '\n')

                    logs = open(str(basedir) + r'/Storage/logs.txt', 'a', encoding='utf-8')
                    logs.write(log)
                    logs.close()

                    categoryMenu(basedir,message,bot)

                elif(message.text == "🗑 удалить всё" and (dataRecieve(basedir, message.from_user.id, 2) == "edit business lunch")):
                     
                    for root, dirs, files in os.walk(basedir + r"/Storage/businessLunch/soups"):  
                        for filename in files:
                            os.remove(basedir + r"/Storage/businessLunch/soups/" + filename)

                    for root, dirs, files in os.walk(basedir + r"/Storage/businessLunch/firstCours"):  
                        for filename in files:
                            os.remove(basedir + r"/Storage/businessLunch/firstCours/" + filename)

                    for root, dirs, files in os.walk(basedir + r"/Storage/businessLunch/garnish"):  
                        for filename in files:
                            os.remove(basedir + r"/Storage/businessLunch/garnish/" + filename)

                    for root, dirs, files in os.walk(basedir + r"/Storage/businessLunch/salad"):  
                        for filename in files:
                            os.remove(basedir + r"/Storage/businessLunch/salad/" + filename)
                    
                    for root, dirs, files in os.walk(basedir + r"/Storage/businessLunch/bread"):  
                        for filename in files:
                            os.remove(basedir + r"/Storage/businessLunch/bread/" + filename)
                    
                    for root, dirs, files in os.walk(basedir + r"/Storage/businessLunch/drink"):  
                        for filename in files:
                            os.remove(basedir + r"/Storage/businessLunch/drink/" + filename)
                            
                    editBusinessLunch(basedir, message, bot)
                 
                elif(message.text == "✅ отправить" and dataRecieve(basedir, message.from_user.id, 2) == "waiting for confirmation"):
                    dataChange(basedir, message.from_user.id, 2, "after mailing")
                    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=False)
                    
                    with open(str(basedir) + r'/Storage/mailing.txt', "r", encoding='utf-8') as document:
                        mailing = document.read()

                    amount = 0
                    for root, dirs, files in os.walk(basedir + r"/Storage/users"):  
                        for filename in files:
                            id = filename.replace(".txt","")
                            try:
                                userBot.send_message(id, text = mailing .format(message.from_user), reply_markup=keyboard)
                                amount += 1
                            except:
                                continue
                    
                    btn1 = ("◀ назад")
                    keyboard.row(btn1)

                    bot.send_message(message.chat.id, text= ("✅ Отправлено: " + str(amount) + " сообщений ✅") .format(message.from_user), reply_markup=keyboard)

                elif(dataRecieve(basedir, message.from_user.id, 2) == "edit mailing"):
                    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=False)

                    dataChange(basedir, message.from_user.id, 2, "waiting for confirmation")

                    with open(str(basedir) + r'/Storage/mailing.txt', "w", encoding='utf-8') as document:
                        document.write(message.text)

                    with open(str(basedir) + r'/Storage/mailing.txt', "r", encoding='utf-8') as document:
                        textToReturn = document.read()

                    btn1 = ("◀ назад")
                    btn2 = ("✅ отправить")
                    keyboard.row(btn1,btn2)

                    bot.send_message(message.chat.id, text= ("Рассылка: \n\n" + textToReturn) .format(message.from_user), reply_markup=keyboard)
                    bot.send_message(message.chat.id, text= ("⬇️ подтвердите отправку ⬇️") .format(message.from_user), reply_markup=keyboard)

                elif(message.text == "Статистика" and dataRecieve(basedir, message.from_user.id, 2) == "main page"):
                    current_datetime = datetime.now()
                    text = ''
                    numberUsers = 0
                    for root, dirs, files in os.walk(basedir + r"/Storage/users"):  
                            for file in files:
                                numberUsers += 1
                    text += "< Общая статистика >\n"+"Число пользователей: " + str(numberUsers)
                    #
                    with open(str(basedir) + r'/Storage/statistics/evaluations.txt', 'r', encoding='utf-8') as file:              
                        reviews = file.read()
                    
                    averageRating = 0
                    if(reviews != ""):
                        reviews = reviews.split()
                        for i in range(len(reviews)):
                            averageRating += int(reviews[i])

                        averageRating = float(averageRating / len(reviews))
                        averageRating = round(averageRating, 2)

                        text += "\nСредняя оценка: " + str(averageRating)
                    else:
                        text += "\nСредняя оценка неизвестна" 

                    #
                    
                    if(current_datetime.month < 10):
                        mouth = "0"+str(current_datetime.month)
                    else:
                        mouth = str(current_datetime.month)

                    text += "\n\n< Статистика за " + mouth + "/" + str(current_datetime.year)+" >"
                    with open(str(basedir) + r'/Storage/statistics/users.txt', 'r', encoding='utf-8') as file:              
                        newUsers = file.read()
                    
                    text += "\nНовых пользователей: " + str(newUsers)

                    #

                    with open(str(basedir) + r'/Storage/statistics/numberOrderLastMouth.txt', 'r', encoding='utf-8') as file:              
                        numberOrderLastMouth = file.read()

                    text +="\nКоличество заказов: " + numberOrderLastMouth
                    
                    #

                    with open(str(basedir) + r'/Storage/statistics/averageCheckLastMouth.txt', 'r', encoding='utf-8') as file:              
                        averageOrderLastMouth = file.read()

                    text +="\nСредний чек: " + averageOrderLastMouth + "руб"
                    
                    #

                    with open(str(basedir) + r'/Storage/statistics/amountsDiscont.txt', 'r', encoding='utf-8') as file:              
                        amountsDisconts = file.read()
                    
                    with open(str(basedir) + r'/Storage/minimumOrderAmount.txt', 'r', encoding='utf-8') as file:              
                        minimumOrderAmount = file.read()

                    text +="\nПользователей заказавших меньше чем на " + minimumOrderAmount+ "руб. " + str(amountsDisconts) + " из " + str(numberUsers)

                    #
                    
                    bot.send_message(message.chat.id, text = text .format(message.from_user))

                elif(message.text == "Создать рассылку" and dataRecieve(basedir, message.from_user.id, 2) == "main page"):
                    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=False)
                    dataChange(basedir, message.from_user.id, 2, "edit mailing")

                    btn1 = ("◀ назад")
                    keyboard.row(btn1)
                    bot.send_message(message.chat.id, text= ("⬇️ Напишите рассылку ⬇️") .format(message.from_user), reply_markup=keyboard)

                elif(message.text == "✏ изменить цену" and dataRecieve(basedir, message.from_user.id, 2) == "edit business lunch"):
                    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=False)
                    dataChange(basedir, message.from_user.id, 2, "edit business lunch prise")

                    with open(str(basedir) + r'/Storage/businessLunchPrise.txt', "r", encoding='utf-8') as document:
                        textToReturn = document.read()
                    
                    btn1 = ("◀ назад")
                    keyboard.row(btn1)
                    
                    bot.send_message(message.chat.id, text= ("Текущая цена: " + textToReturn + "руб") .format(message.from_user), reply_markup=keyboard)
                    bot.send_message(message.chat.id, text= ("⬇️ Напишите новую цену ⬇️") .format(message.from_user), reply_markup=keyboard)

                elif(message.text == "➕ Добавить блюдо"and (dataRecieve(basedir, message.from_user.id, 2) == "edit category"
                    or dataRecieve(basedir, message.from_user.id, 2) =="create name" 
                    or dataRecieve(basedir, message.from_user.id, 2) =="create gramm"
                    or dataRecieve(basedir, message.from_user.id, 2) =="create ruble"
                    or dataRecieve(basedir, message.from_user.id, 2) =="create image")):

                    dataChange(basedir, message.from_user.id, 2, "create name")
                    bot.send_message(message.chat.id, text= "1⃣ Напишите название блюда." .format(message.from_user))

                elif(dataRecieve(basedir, message.from_user.id, 2) == "create category"):

                    if (os.path.exists(basedir + "/Storage/images/" + message.text) != True):
                        amount = 0
                        for root, dirs, files in os.walk(basedir + r"/Storage/images"):  
                            for dirname in dirs:
                                amount += 1
                                
                        if (amount < 14):
                            os.mkdir(basedir + "/Storage/images/" + message.text)
                            os.mkdir(basedir + "/Storage/imagesForClients/" + message.text)

                            log  = (str(datetime.now()) + ' Создана новая категория меню пользователем рабочего бота с ID: ' + str(message.from_user.id) + '\n')

                            logs = open(str(basedir) + r'/Storage/logs.txt', 'a')
                            logs.write(log)
                            logs.close()

                            categoryMenu(basedir, message, bot)

                        else:
                            keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=False)
                            bot.send_message(message.chat.id, text= "🚫 Превышен лимит категорий(14) 🚫" .format(message.from_user), reply_markup=keyboard)

                    else:
                        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=False)
                        bot.send_message(message.chat.id, text= "🚫 Категория уже существует 🚫" .format(message.from_user), reply_markup=keyboard)
                        bot.send_message(message.chat.id, text= "⬇️ Напишите новую категорию ⬇️" .format(message.from_user), reply_markup=keyboard)

                elif(message.text == "Бизнес-ланч" and dataRecieve(basedir, message.from_user.id, 2) == "main page"):
                    editBusinessLunch(basedir, message, bot)
                    

                elif(message.text == "Меню" and dataRecieve(basedir, message.from_user.id, 2) == "main page"):
                    categoryMenu(basedir,message,bot)

                elif(message.text == "Акции" and dataRecieve(basedir, message.from_user.id, 2) == "main page"):
                    editPromotion(basedir,message,bot)

                elif(message.text == "🗑 удалить акцию" and dataRecieve(basedir, message.from_user.id, 2) == "edit promotion"):
                    os.remove(str(basedir) + r'/Storage/promotion.txt')
                    bot.send_message(message.chat.id, text= "Акция удалена" .format(message.from_user))

                    log  = (str(datetime.now()) + ' Удалена акция пользователем рабочего бота с ID: ' + str(message.from_user.id) + '\n')

                    logs = open(str(basedir) + r'/Storage/logs.txt', 'a')
                    logs.write(log)
                    logs.close()

                    editPromotion(basedir,message,bot)

                elif(dataRecieve(basedir, message.from_user.id, 2) == "edit promotion"):

                    log  = (str(datetime.now()) + ' Изменена акция пользователем рабочего бота с ID: ' + str(message.from_user.id) + '\n')

                    logs = open(str(basedir) + r'/Storage/logs.txt', 'a')
                    logs.write(log)
                    logs.close()

                    with open (str(basedir) + r'/Storage/promotion.txt', 'w', encoding='utf-8') as file:
                        file.write(message.text)
                    editPromotion(basedir,message,bot)

                elif(dataRecieve(basedir, message.from_user.id, 2) == "create name"):
                    dataChange(basedir, message.from_user.id, 2, "create gramm")
                    dataChange(basedir, message.from_user.id, 4, message.text)
                    bot.send_message(message.chat.id, text= "2⃣ Напишите граммовку блюда." .format(message.from_user))

                elif(dataRecieve(basedir, message.from_user.id, 2) == "create gramm"):
                    dataChange(basedir, message.from_user.id, 2, "create ruble")
                    dataChange(basedir, message.from_user.id, 5, message.text)
                    bot.send_message(message.chat.id, text= "3⃣ Напишите цену блюда." .format(message.from_user))

                elif(dataRecieve(basedir, message.from_user.id, 2) == "create ruble"):
                    dataChange(basedir, message.from_user.id, 2, "create image")
                    dataChange(basedir, message.from_user.id, 6, message.text)
                    bot.send_message(message.chat.id, text= "4⃣ Отправьте фотографию блюда." .format(message.from_user))

                elif(dataRecieve(basedir, message.from_user.id, 2) == "addSoups"):
                    with open(str(basedir) + r'/Storage/businessLunch/soups/' + message.text, 'w', encoding='utf-8') as file:
                        editBusinessLunch(basedir, message, bot)

                elif(dataRecieve(basedir, message.from_user.id, 2) == "addFirstCourse"):
                    with open(str(basedir) + r'/Storage/businessLunch/firstCourse/' + message.text, 'w', encoding='utf-8') as file:
                        editBusinessLunch(basedir, message, bot)

                elif(dataRecieve(basedir, message.from_user.id, 2) == "addGarnish"):
                    with open(str(basedir) + r'/Storage/businessLunch/garnish/' + message.text, 'w', encoding='utf-8') as file:
                        editBusinessLunch(basedir, message, bot)

                elif(dataRecieve(basedir, message.from_user.id, 2) == "addSalad"):
                    with open(str(basedir) + r'/Storage/businessLunch/salad/' + message.text, 'w', encoding='utf-8') as file:
                        editBusinessLunch(basedir, message, bot)

                elif(dataRecieve(basedir, message.from_user.id, 2) == "addBread"):
                    with open(str(basedir) + r'/Storage/businessLunch/bread/' + message.text, 'w', encoding='utf-8') as file:
                        editBusinessLunch(basedir, message, bot)

                elif(dataRecieve(basedir, message.from_user.id, 2) == "addDrink"):
                    with open(str(basedir) + r'/Storage/businessLunch/drink/' + message.text, 'w', encoding='utf-8') as file:
                        editBusinessLunch(basedir, message, bot)

            elif (dataRecieve(basedir, message.from_user.id, 2) == "enters password" and message.text == password):

                dataChange(basedir, message.from_user.id, 1, "admin")
                dataChange(basedir, message.from_user.id, 2, "main page")

                keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=False)

                btn1 = types.KeyboardButton("Статистика")
                btn2 = types.KeyboardButton("Бизнес-ланч")
                btn3 = types.KeyboardButton("Меню")
                btn4 = types.KeyboardButton("Создать рассылку")
                btn5 = types.KeyboardButton("Акции")

                keyboard.row(btn1)
                keyboard.row(btn2,btn3)
                keyboard.row(btn4)
                keyboard.row(btn5)

                bot.send_message(message.chat.id, text= "✅ Вход выполнен успешно ✅" .format(message.from_user), reply_markup=keyboard)
                bot.send_message(message.chat.id, text= "⬇️ используйте кнопки ⬇️" .format(message.from_user), reply_markup=keyboard)
                
                log  = (str(datetime.now()) + ' Выполнен вход пользователем в рабочего бота с ID: ' + str(message.from_user.id) + '\n')

                logs = open(str(basedir) + r'/Storage/logs.txt', 'a')
                logs.write(log)
                logs.close()

            elif (dataRecieve(basedir, message.from_user.id, 2) == "enters password" and message.text != password):

                bot.send_message(message.chat.id, text= "❌ Неверный пароль ❌" .format(message.from_user), reply_markup=markup)

                log  = (str(datetime.now()) + ' Введен неверный пароль пользователем рабочего бота с ID: ' + str(message.from_user.id) + '\n')

                logs = open(str(basedir) + r'/Storage/logs.txt', 'a')
                logs.write(log)
                logs.close()

    @bot.callback_query_handler(func=lambda call: True)
    def menu_inline(message):
        print("Рабочий | " + str(datetime.now())+ " | " + str(message.from_user.id) + " | "+ str(message.data))
        if (message.data == "create category" and dataRecieve(basedir, message.from_user.id, 2) == "edit menu"):

            keyboard = types.InlineKeyboardMarkup(row_width=2)
            dataChange(basedir, message.from_user.id, 2, "create category")
            bot.send_message(message.from_user.id, text= "⬇️ Напишите новую категорию ⬇️" .format(message.from_user), reply_markup=keyboard)

            log  = (str(datetime.now()) + ' Создаётся новая категория меню пользователем рабочего бота с ID: ' + str(message.from_user.id) + '\n')

            logs = open(str(basedir) + r'/Storage/logs.txt', 'a')
            logs.write(log)
            logs.close()

        elif(dataRecieve(basedir, message.from_user.id, 2) == "edit menu"):
            editCategory(basedir, message, bot)
        
        elif(dataRecieve(basedir, message.from_user.id, 2) == "edit category"):

            folderName = dataRecieve(basedir, message.from_user.id, 3)
            os.remove(basedir + r"/Storage/images/" + folderName + "/" + message.data)

            log  = (str(datetime.now()) + ' Удален файл ' + message.data + ' пользователем рабочего бота с ID: ' + str(message.from_user.id) + '\n')

            logs = open(str(basedir) + r'/Storage/logs.txt', 'a', encoding='utf-8')
            logs.write(log)
            logs.close()

            message.data = folderName

            distributionAlgorithm.distribution(basedir, folderName)

            bot.send_message(message.from_user.id, text= "Блюдо удалено" .format(message.from_user))

            editCategory(basedir, message, bot)

        elif(dataRecieve(basedir, message.from_user.id, 2) == "edit business lunch"):

            if(message.data == "addSoups"):
                dataChange(basedir, message.from_user.id, 2, "addSoups")
                bot.send_message(message.from_user.id, text= "⬇️ Напишите суп ⬇️" .format(message.from_user))

            elif(message.data == "addFirstCourse"):
                dataChange(basedir, message.from_user.id, 2, "addFirstCourse")
                bot.send_message(message.from_user.id, text= "⬇️ Напишите горячее ⬇️" .format(message.from_user))

            elif(message.data == "addGarnish"):
                dataChange(basedir, message.from_user.id, 2, "addGarnish")
                bot.send_message(message.from_user.id, text= "⬇️ Напишите гарнир ⬇️" .format(message.from_user))

            elif(message.data == "addSalad"):
                dataChange(basedir, message.from_user.id, 2, "addSalad")
                bot.send_message(message.from_user.id, text= "⬇️ Напишите салат ⬇️" .format(message.from_user))

            elif(message.data == "addBread"):
                dataChange(basedir, message.from_user.id, 2, "addBread")
                bot.send_message(message.from_user.id, text= "⬇️ Напишите хлеб ⬇️" .format(message.from_user))

            elif(message.data == "addDrink"):
                dataChange(basedir, message.from_user.id, 2, "addDrink")
                bot.send_message(message.from_user.id, text= "⬇️ Напишите напиток ⬇️" .format(message.from_user))
            
            else:
                os.remove(basedir + r"/Storage/businessLunch" + message.data)
                editBusinessLunch(basedir, message, bot)

    @bot.message_handler(content_types=['photo'])
    def get_user_pics(message):
        if(dataRecieve(basedir, message.from_user.id, 2) == "create image"):

            name = dataRecieve(basedir, message.from_user.id, 4)
            gramm = dataRecieve(basedir, message.from_user.id, 5)
            ruble = dataRecieve(basedir, message.from_user.id, 6)

            fileID = message.photo[-1].file_id   
            file_info = bot.get_file(fileID)
            downloaded_file = bot.download_file(file_info.file_path)
            with open(str(basedir) + r'/Storage/images/' + dataRecieve(basedir, message.from_user.id, 3) + "/" + name + "!" + gramm + "!" + ruble + ".jpg", 'wb') as new_file:
                new_file.write(downloaded_file)
            
            message.data = dataRecieve(basedir, message.from_user.id, 3)

            distributionAlgorithm.distribution(basedir, dataRecieve(basedir, message.from_user.id, 3))

            editCategory(basedir, message, bot)

    bot.remove_webhook()
    bot.infinity_polling()
    
