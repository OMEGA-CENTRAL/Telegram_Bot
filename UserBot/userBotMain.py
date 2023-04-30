import telebot
from datetime import datetime
import os
from telebot import types 


def dataChange(basedir, IDforChange, lineNumberToChange, replacementText):

    replacementText = replacementText + str(hex(lineNumberToChange)) +"\n"

    with open(str(basedir) + r'/Storage/users/' + str(IDforChange)+ ".txt", 'r', encoding='utf-8') as file:              
        for i in range(lineNumberToChange):
            lineToChange = file.readline()
        file.close()
    
    with open (str(basedir) + r'/Storage/users/' + str(IDforChange)+".txt", 'r', encoding='utf-8') as f:
        old_data = f.read()
    
    new_data = old_data.replace(lineToChange, replacementText)
    
    with open (str(basedir) + r'/Storage/users/' + str(IDforChange) + ".txt", 'w', encoding='utf-8') as f:
        f.write(new_data)


def dataRecieve(basedir, IDforRecieve, lineNumberToRecieve):

    file = open(str(basedir) + r'/Storage/users/' + str(IDforRecieve)+".txt", 'r', encoding='utf-8')
    for i in range(lineNumberToRecieve):
        lineToReturn = file.readline()
    file.close()

    lineToReturn = lineToReturn.replace("\n","")
    lineToReturn = lineToReturn.replace(str(hex(lineNumberToRecieve)), "")
    return lineToReturn


def mainPage(basedir, message, bot):
    dataChange(basedir, message.from_user.id, 1, "main page")

    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)

    btn1 = types.KeyboardButton("Акции")
    btn2 = types.KeyboardButton("Бизнес-ланч")
    btn3 = types.KeyboardButton("Меню")
    btn4 = types.KeyboardButton("Корзина")
    btn5 = types.KeyboardButton("Оценить нас")

    bot.set_my_commands([
        telebot.types.BotCommand("/help", "ℹ Информация"),
        telebot.types.BotCommand("/start", "🔄 Перезапустить бота"),
    ])

    if (os.path.isfile(str(basedir) + r'/Storage/promotion.txt')) == True:
        keyboard.row(btn1)
    keyboard.row(btn2,btn3)
    keyboard.row(btn4)
    if (dataRecieve(basedir, message.from_user.id, 2) == "yes"):
        keyboard.row(btn5)
            
    bot.send_message(message.from_user.id, text = "⬇️ используйте кнопки ⬇️" .format(message.from_user),reply_markup=keyboard)

def pageBusinessLunch(basedir, message, bot):
    keyboard = types.InlineKeyboardMarkup(row_width=1)

    if(dataRecieve(basedir, message.from_user.id,3) == "soups"):
        

        filenames = []
        for root, dirs, files in os.walk(basedir + r"/Storage/businessLunch/soups"):  
            for filename in files:
                filenames.append(filename)
        
        if(len(filenames) == 1):
            btn1 = types.InlineKeyboardButton(text = "➕ " + filenames[0] + " ("+"0"+") ", callback_data = filenames[0])
            keyboard.add(btn1)

        elif(len(filenames) == 2):
            btn1 = types.InlineKeyboardButton(text = "➕ " + filenames[0] + " ("+"0"+") ", callback_data = filenames[0])
            btn2 = types.InlineKeyboardButton(text = "➕ " + filenames[1] + " ("+"0"+") ", callback_data = filenames[1])
            keyboard.add(btn1,btn2)

        btn3 = types.InlineKeyboardButton(text = "◀", callback_data = "back")
        btn4 = types.InlineKeyboardButton(text = "1/6", callback_data = "none")
        btn5 = types.InlineKeyboardButton(text = "▶", callback_data = "further")
        
        keyboard.row(btn3,btn4,btn5)
        bot.send_message(message.from_user.id, text= "⠀                           ⠀\n⠀                      Супы:                      ⠀\n⠀                           ⠀" .format(message.from_user), reply_markup=keyboard)

def counting(basedir, message, numberLine, text):
    line = dataRecieve(basedir, message.from_user.id, numberLine)
    line = line.replace(" ",";")
    line = line.replace("  ",";")
    line = line.replace(":"," ")
    line = line.split()

    text = text.replace(" ",";")
    text = text.replace("  ",";")
    
    return str(line.count(text))

def removeDish(basedir, message, numberLine, text):
    line = dataRecieve(basedir, message.from_user.id, numberLine)
    line = line.replace(" ",";")
    line = line.replace("  ",";")
    line = line.replace(":"," ")
    line = line.split()

    text = text.replace(" ",";")
    text = text.replace("  ",";")

    line.remove(text)

    textToReturn = ""

    for i in range(len(line)):
        textToReturn = textToReturn + line[i] + ":"

    textToReturn = textToReturn.replace(";"," ")
    return(textToReturn)

def countingPrise(basedir, message, bot):
    filenames = dataRecieve(basedir, message.from_user.id,25)

    prise = 0

    if(filenames != "" and filenames != "меню неизвестно"):

        filenames = filenames.replace(".jpg","")
        filenames = filenames.replace(" ",";")
        filenames = filenames.replace(":"," ")
        filenames = filenames.split()

        
    
        for i in range(len(filenames)):
            prise = prise + int(filenames[i].partition("!")[2].partition("!")[2])

    for o in range(100):
        line = dataRecieve(basedir, message.from_user.id, 27 + o)
        if(counting(basedir, message, 27 + o, "none")) != "1":
            prise = prise + int(line.partition("!")[2].partition("!")[0]) * int(line.partition("!")[2].partition("!")[2])
        else:
            break

    return str(prise)

def basket(basedir, message, bot):
    
    if((dataRecieve(basedir, message.from_user.id,25) == "меню неизвестно" or dataRecieve(basedir, message.from_user.id,25) == "") and counting(basedir, message, 27, "none") == "1"):

        bot.send_message(message.chat.id, text = "Ваша корзина пуста!" .format(message.from_user))

    else:
        if(dataRecieve(basedir, message.from_user.id,1) == "basket"):
            if("--" in message.data or "++" in message.data):
                
                message.data = message.data.replace("-- ","")
                message.data = message.data.replace("++ ","")
                keyboard = types.InlineKeyboardMarkup(row_width=4)
                if("$" in message.data):
                    message.data = str(message.data.replace("$",""))

                    lunch = dataRecieve(basedir, message.from_user.id,int(message.data))
                    count = lunch.partition("!")[2].partition("!")[2]
                    
                    if(count == "1"):
                        btn1 = types.InlineKeyboardButton(text = "-", callback_data ="delete$" + message.data)
                    else:
                        btn1 = types.InlineKeyboardButton(text = "-", callback_data = "$-- "+ message.data)
                    btn2 = types.InlineKeyboardButton(text = count, callback_data = "none")
                    btn3 = types.InlineKeyboardButton(text = "+", callback_data = "$++ "+ message.data)
                    btn4 = types.InlineKeyboardButton(text = "❌", callback_data = "delete$" + message.data)

                    keyboard.row(btn1,btn2,btn3,btn4)
                    
                    bot.edit_message_reply_markup(chat_id = message.from_user.id, message_id = message.message.id, reply_markup = keyboard)

    

                else:
                    if(counting(basedir,message,25,message.data) == "1"):
                        btn1 = types.InlineKeyboardButton(text = "-", callback_data = "delete" + message.data)
                    else:
                        btn1 = types.InlineKeyboardButton(text = "-", callback_data = "-- " + message.data)

                    btn2 = types.InlineKeyboardButton(text = counting(basedir,message,25,message.data), callback_data = "none")
                    btn3 = types.InlineKeyboardButton(text = "+", callback_data = "++ " + message.data)
                    btn4 = types.InlineKeyboardButton(text = "❌", callback_data = "delete" + message.data)

                    keyboard.row(btn1,btn2,btn3,btn4)
                    
                    bot.edit_message_reply_markup(chat_id = message.from_user.id, message_id = message.message.id, reply_markup = keyboard)

                bot.edit_message_text(chat_id = message.from_user.id, message_id = int(dataRecieve(basedir, message.from_user.id,18)), text = "Итого: " + countingPrise(basedir,message,bot) + "руб")

        elif(dataRecieve(basedir, message.from_user.id,1) != "basket"):
            dataChange(basedir, message.from_user.id, 1, "basket")
            
            keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=False)

            btn1 = types.KeyboardButton("◀ назад")
            btn2 = types.KeyboardButton("✅ оформить заказ")
            btn3 = types.KeyboardButton("Меню") 
            keyboard.row(btn1,btn3)
            keyboard.row(btn2)
            bot.send_message(message.chat.id, text= "Ваша корзина:" .format(message.from_user), reply_markup=keyboard)

            if(dataRecieve(basedir, message.from_user.id,25) != "меню неизвестно" and dataRecieve(basedir, message.from_user.id,25) != ""):
                filenames = dataRecieve(basedir, message.from_user.id,25) 
                filenames = filenames.replace(" ",";")
                filenames = filenames.replace(":"," ")
                filenames = filenames.split()

                textNoRepetition = []
                textNoRepetition.extend(set(filenames))

                for i in range(len(textNoRepetition)):
                    keyboard = types.InlineKeyboardMarkup(row_width=4)
                    filename = str(textNoRepetition[i]).replace(";"," ")
                    if(counting(basedir,message,25,textNoRepetition[i]) == "1"):
                        btn1 = types.InlineKeyboardButton(text = "-", callback_data ="delete" + filename)
                    else:
                        btn1 = types.InlineKeyboardButton(text = "-", callback_data = "-- " + filename)
                    btn2 = types.InlineKeyboardButton(text = counting(basedir,message,25,textNoRepetition[i]), callback_data = "none")
                    btn3 = types.InlineKeyboardButton(text = "+", callback_data = "++ " + filename)
                    btn4 = types.InlineKeyboardButton(text = "❌", callback_data = "delete" + filename)

                    keyboard.row(btn1,btn2,btn3,btn4)

                    text = textNoRepetition[i]
                    text = text.replace(".jpg", "")
                    text = text.replace(";", " ")
                    name = text.partition("!")[0]
                    text = text.partition("!")[2]
                    gramm = text.partition("!")[0]
                    ruble = text.partition("!")[2]
                    caption = str(name + " " + gramm +"г/" + ruble + "руб")
                    
                    bot.send_message(message.chat.id, text = caption .format(message.from_user), reply_markup=keyboard)

            for i in range(100):
                if(counting(basedir, message, i + 27, "none") != "1"):
                    keyboard = types.InlineKeyboardMarkup(row_width=4)
                    
                    lunch = dataRecieve(basedir, message.from_user.id,i + 27)
                    count = lunch.partition("!")[2].partition("!")[2]
                    
                    dishs = lunch.partition("!")[0]
                    prise = lunch.partition("!")[2].partition("!")[0]

                    dishs = dishs.replace(" ",";")
                    dishs = dishs.replace(":"," ")
                    dishs = dishs.split()

                    textNoRepetition = []
                    textNoRepetition.extend(set(dishs))
                    
                    text = "Бизнес-ланч: \n"

                    for o in range(len(textNoRepetition)):
                        
                        text = text + "\n" + textNoRepetition[o] + " (" + counting(basedir, message, i + 27, textNoRepetition[o]) + ")"
                        

                    text = text.replace(";"," ")
                    text = text + "\n\n" + prise + "руб"

                    if(count == "1"):
                        btn1 = types.InlineKeyboardButton(text = "-", callback_data ="delete$" + str(i + 27))
                    else:
                        btn1 = types.InlineKeyboardButton(text = "-", callback_data = "$-- "+ str(i + 27))
                    btn2 = types.InlineKeyboardButton(text = count, callback_data = "none")
                    btn3 = types.InlineKeyboardButton(text = "+", callback_data = "$++ "+ str(i + 27))
                    btn4 = types.InlineKeyboardButton(text = "❌", callback_data = "delete$" + str(i + 27))

                    keyboard.row(btn1,btn2,btn3,btn4)
                    bot.send_message(message.chat.id, text = text .format(message.from_user), reply_markup=keyboard)
                else:
                    break
            
            priseMessage = bot.send_message(message.chat.id, text = "Итого: " + countingPrise(basedir,message,bot) + "руб" .format(message.from_user))
            dataChange(basedir, message.from_user.id, 18, str(priseMessage.message_id))

def editPageBusinessLunch(basedir, message, bot):
    keyboard = types.InlineKeyboardMarkup(row_width=3)

    if(dataRecieve(basedir, message.from_user.id,3) == "soups"):

        filenames = []
        for root, dirs, files in os.walk(basedir + r"/Storage/businessLunch/soups"):  
            for filename in files:
                filenames.append(filename)
        
        if(len(filenames) == 1):
            btn1 = types.InlineKeyboardButton(text = "➕ " + filenames[0]+ " ("+counting(basedir,message,4,filenames[0])+") ", callback_data = filenames[0])
            keyboard.row(btn1)

        elif(len(filenames) == 2):
            btn1 = types.InlineKeyboardButton(text = "➕ " + filenames[0]+ " ("+counting(basedir,message,4,filenames[0])+") ", callback_data = filenames[0])
            btn2 = types.InlineKeyboardButton(text = "➕ " + filenames[1]+ " ("+counting(basedir,message,4,filenames[1])+") ", callback_data = filenames[1])
            keyboard.row(btn1)
            keyboard.row(btn2)
        
        btn3 = types.InlineKeyboardButton(text = "◀", callback_data = "back")
        btn4 = types.InlineKeyboardButton(text = "1/6", callback_data = "none")
        btn5 = types.InlineKeyboardButton(text = "▶", callback_data = "further")
        
        keyboard.row(btn3,btn4,btn5)
        bot.edit_message_text(text= "⠀                           ⠀\n⠀                      Супы:                      ⠀\n⠀                           ⠀" .format(message.from_user),  chat_id = message.from_user.id, message_id = message.message.id,reply_markup=keyboard)
        
    elif(dataRecieve(basedir, message.from_user.id,3) == "firstCourse"):
        filenames = []
        for root, dirs, files in os.walk(basedir + r"/Storage/businessLunch/firstCourse"):  
            for filename in files:
                filenames.append(filename)
        
        if(len(filenames) == 1):
            btn1 = types.InlineKeyboardButton(text = "➕ " + filenames[0]+ " ("+counting(basedir,message,5,filenames[0])+") ", callback_data = filenames[0])
            keyboard.row(btn1)

        elif(len(filenames) == 2):
            btn1 = types.InlineKeyboardButton(text = "➕ " + filenames[0]+ " ("+counting(basedir,message,5,filenames[0])+") ", callback_data = filenames[0])
            btn2 = types.InlineKeyboardButton(text = "➕ " + filenames[1]+ " ("+counting(basedir,message,5,filenames[1])+") ", callback_data = filenames[1])
            keyboard.row(btn1)
            keyboard.row(btn2)
        
        btn3 = types.InlineKeyboardButton(text = "◀", callback_data = "back")
        btn4 = types.InlineKeyboardButton(text = "2/6", callback_data = "none")
        btn5 = types.InlineKeyboardButton(text = "▶", callback_data = "further")
        
        keyboard.row(btn3,btn4,btn5)
        bot.edit_message_text(text= "⠀                           ⠀\n⠀                    Горячее:                   ⠀\n⠀                           ⠀" .format(message.from_user),  chat_id = message.from_user.id, message_id = message.message.id,reply_markup=keyboard)

    elif(dataRecieve(basedir, message.from_user.id,3) == "garnish"):
        filenames = []
        for root, dirs, files in os.walk(basedir + r"/Storage/businessLunch/garnish"):  
            for filename in files:
                filenames.append(filename)
        
        if(len(filenames) == 1):
            btn1 = types.InlineKeyboardButton(text = "➕ " + filenames[0]+ " ("+counting(basedir,message,6,filenames[0])+") ", callback_data = filenames[0])
            keyboard.row(btn1)

        elif(len(filenames) == 2):
            btn1 = types.InlineKeyboardButton(text = "➕ " + filenames[0]+ " ("+counting(basedir,message,6,filenames[0])+") ", callback_data = filenames[0])
            btn2 = types.InlineKeyboardButton(text = "➕ " + filenames[1]+ " ("+counting(basedir,message,6,filenames[1])+") ", callback_data = filenames[1])
            keyboard.row(btn1)
            keyboard.row(btn2)
        
        btn3 = types.InlineKeyboardButton(text = "◀", callback_data = "back")
        btn4 = types.InlineKeyboardButton(text = "3/6", callback_data = "none")
        btn5 = types.InlineKeyboardButton(text = "▶", callback_data = "further")
        
        keyboard.row(btn3,btn4,btn5)
        bot.edit_message_text(text= "⠀                           ⠀\n⠀                   Гарниры:                   ⠀\n⠀                           ⠀" .format(message.from_user),  chat_id = message.from_user.id, message_id = message.message.id,reply_markup=keyboard)

    elif(dataRecieve(basedir, message.from_user.id,3) == "salad"):
        filenames = []
        for root, dirs, files in os.walk(basedir + r"/Storage/businessLunch/salad"):  
            for filename in files:
                filenames.append(filename)
        
        if(len(filenames) == 1):
            btn1 = types.InlineKeyboardButton(text = "➕ " + filenames[0]+ " ("+counting(basedir,message,7,filenames[0])+") ", callback_data = filenames[0])
            keyboard.row(btn1)

        elif(len(filenames) == 2):
            btn1 = types.InlineKeyboardButton(text = "➕ " + filenames[0]+ " ("+counting(basedir,message,7,filenames[0])+") ", callback_data = filenames[0])
            btn2 = types.InlineKeyboardButton(text = "➕ " + filenames[1]+ " ("+counting(basedir,message,7,filenames[1])+") ", callback_data = filenames[1])
            keyboard.row(btn1)
            keyboard.row(btn2)
        
        btn3 = types.InlineKeyboardButton(text = "◀", callback_data = "back")
        btn4 = types.InlineKeyboardButton(text = "4/6", callback_data = "none")
        btn5 = types.InlineKeyboardButton(text = "▶", callback_data = "further")
        
        keyboard.row(btn3,btn4,btn5)
        bot.edit_message_text(text= "⠀                           ⠀\n⠀                    Салаты:                    ⠀\n⠀                           ⠀" .format(message.from_user),  chat_id = message.from_user.id, message_id = message.message.id,reply_markup=keyboard)
    
    elif(dataRecieve(basedir, message.from_user.id,3) == "bread"):
        filenames = []
        for root, dirs, files in os.walk(basedir + r"/Storage/businessLunch/bread"):  
            for filename in files:
                filenames.append(filename)
        
        if(len(filenames) == 1):
            btn1 = types.InlineKeyboardButton(text = "➕ " + filenames[0]+ " ("+counting(basedir,message,8,filenames[0])+") ", callback_data = filenames[0])
            keyboard.row(btn1)

        elif(len(filenames) == 2):
            btn1 = types.InlineKeyboardButton(text = "➕ " + filenames[0]+ " ("+counting(basedir,message,8,filenames[0])+") ", callback_data = filenames[0])
            btn2 = types.InlineKeyboardButton(text = "➕ " + filenames[1]+ " ("+counting(basedir,message,8,filenames[1])+") ", callback_data = filenames[1])
            keyboard.row(btn1)
            keyboard.row(btn2)
        
        btn3 = types.InlineKeyboardButton(text = "◀", callback_data = "back")
        btn4 = types.InlineKeyboardButton(text = "5/6", callback_data = "none")
        btn5 = types.InlineKeyboardButton(text = "▶", callback_data = "further")
        
        keyboard.row(btn3,btn4,btn5)
        bot.edit_message_text(text= "⠀                           ⠀\n⠀                      Хлеба:                     ⠀\n⠀                           ⠀" .format(message.from_user),  chat_id = message.from_user.id, message_id = message.message.id,reply_markup=keyboard)

    elif(dataRecieve(basedir, message.from_user.id,3) == "drink"):
        filenames = []
        for root, dirs, files in os.walk(basedir + r"/Storage/businessLunch/drink"):  
            for filename in files:
                filenames.append(filename)
        
        if(len(filenames) == 1):
            btn1 = types.InlineKeyboardButton(text = "➕ " + filenames[0]+ " ("+counting(basedir,message,9,filenames[0])+") ", callback_data = filenames[0])
            keyboard.row(btn1)

        elif(len(filenames) == 2):
            btn1 = types.InlineKeyboardButton(text = "➕ " + filenames[0]+ " ("+counting(basedir,message,9,filenames[0])+") ", callback_data = filenames[0])
            btn2 = types.InlineKeyboardButton(text = "➕ " + filenames[1]+ " ("+counting(basedir,message,9,filenames[1])+") ", callback_data = filenames[1])
            keyboard.row(btn1)
            keyboard.row(btn2)
        
        btn3 = types.InlineKeyboardButton(text = "◀", callback_data = "back")
        btn4 = types.InlineKeyboardButton(text = "6/6", callback_data = "none")
        btn5 = types.InlineKeyboardButton(text = "▶", callback_data = "further")
        
        keyboard.row(btn3,btn4,btn5)
        bot.edit_message_text(text= "⠀                           ⠀\n⠀                   Напитки:                   ⠀\n⠀                           ⠀" .format(message.from_user),  chat_id = message.from_user.id, message_id = message.message.id,reply_markup=keyboard)


def categoryMenu(basedir,message,bot):

    dataChange(basedir, message.from_user.id, 1, "looking the category")
    dataChange(basedir, message.from_user.id, 10, "категория меню неизестна")
    dataChange(basedir, message.from_user.id, 11, "страница неизвестна")

    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=False)
    btn1 = types.KeyboardButton("◀ назад")
    keyboard.row(btn1)

    bot.send_message(message.chat.id, text= "..." .format(message.from_user), reply_markup=keyboard)

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    
    #дальше начинается жопа но я хз как сделать по другому)
    
    filenames = []
    amount = 0

    for root, dirs, files in os.walk(basedir + r"/Storage/imagesForClients"):  
        for dirname in dirs:

            amount += 1
            filenames.append(dirname)

    listPosition = 0
    
    if (amount >= 1):
        add1 = types.InlineKeyboardButton(text=filenames[listPosition], callback_data = filenames[listPosition] + "@")
        listPosition += 1
        if (amount == 1):
            keyboard.add(add1)

    if (amount >= 2):
        add2 = types.InlineKeyboardButton(text=filenames[listPosition], callback_data = filenames[listPosition]+ "@")
        listPosition += 1
        if (amount == 2):
            keyboard.add(add1,add2)

    if (amount >= 3):
        add3 = types.InlineKeyboardButton(text=filenames[listPosition], callback_data = filenames[listPosition]+ "@")
        listPosition += 1
        if (amount == 3):
            keyboard.add(add1,add2,add3)

    if (amount >= 4):
        add4 = types.InlineKeyboardButton(text=filenames[listPosition], callback_data = filenames[listPosition]+ "@")
        listPosition += 1
        if (amount == 4):
            keyboard.add(add1,add2,add3,add4)

    if (amount >= 5):
        add5 = types.InlineKeyboardButton(text=filenames[listPosition], callback_data = filenames[listPosition]+ "@")
        listPosition += 1
        if (amount == 5):
            keyboard.add(add1,add2,add3,add4,add5)

    if (amount >= 6):
        add6 = types.InlineKeyboardButton(text=filenames[listPosition], callback_data = filenames[listPosition]+ "@")
        listPosition += 1
        if (amount == 6):
            keyboard.add(add1,add2,add3,add4,add5,add6)
    
    if (amount >= 7):
        add7 = types.InlineKeyboardButton(text=filenames[listPosition], callback_data = filenames[listPosition]+ "@")
        listPosition += 1
        if (amount == 7):
            keyboard.add(add1,add2,add3,add4,add5,add6,add7)
 
    if (amount >= 8):
        add8 = types.InlineKeyboardButton(text=filenames[listPosition], callback_data = filenames[listPosition]+ "@")
        listPosition += 1
        if (amount == 8):
            keyboard.add(add1,add2,add3,add4,add5,add6,add7,add8)

    if (amount >= 9):
        add9 = types.InlineKeyboardButton(text=filenames[listPosition], callback_data = filenames[listPosition]+ "@")
        listPosition += 1
        if (amount == 9):
            keyboard.add(add1,add2,add3,add4,add5,add6,add7,add8,add9)

    if (amount >= 10):
        add10 = types.InlineKeyboardButton(text=filenames[listPosition], callback_data = filenames[listPosition]+ "@")
        listPosition += 1
        if (amount == 10):
            keyboard.add(add1,add2,add3,add4,add5,add6,add7,add8,add9,add10)

    if (amount >= 11):
        add11 = types.InlineKeyboardButton(text=filenames[listPosition], callback_data = filenames[listPosition]+ "@")
        listPosition += 1
        if (amount == 11):
            keyboard.add(add1,add2,add3,add4,add5,add6,add7,add8,add9,add10,add11)

    if (amount >= 12):
        add12 = types.InlineKeyboardButton(text=filenames[listPosition], callback_data = filenames[listPosition]+ "@")
        listPosition += 1
        if (amount == 12):
            keyboard.add(add1,add2,add3,add4,add5,add6,add7,add8,add9,add10,add11,add12)

    if (amount >= 13):
        add13 = types.InlineKeyboardButton(text=filenames[listPosition], callback_data = filenames[listPosition]+ "@")
        listPosition += 1
        if (amount == 13):
            keyboard.add(add1,add2,add3,add4,add5,add6,add7,add8,add9,add10,add11,add12,add13)

    if (amount >= 14):
        add14 = types.InlineKeyboardButton(text=filenames[listPosition], callback_data = filenames[listPosition]+ "@")
        listPosition += 1
        if (amount == 14):
            keyboard.add(add1,add2,add3,add4,add5,add6,add7,add8,add9,add10,add11,add12,add13,add14)

    bot.send_message(message.chat.id, text= "Выберите раздел меню:" .format(message.from_user), reply_markup=keyboard)

def pageMenu(basedir,message,bot,page):
    
    if(dataRecieve(basedir, message.from_user.id, 10) == "категория меню неизестна"):
        dirname = message.data
    else:
        dirname = dataRecieve(basedir, message.from_user.id, 10)

    filenames = []
    amount = 0

    for root, dirs, files in os.walk(basedir + r"/Storage/images/" + dirname):  
        for filename in files:
            amount += 1
            filenames.append(filename)

    if(amount != 0):
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=False)

        btn1 = types.KeyboardButton("◀ к категориям")
        btn2 = types.KeyboardButton("🛒 корзина")
        keyboard.row(btn1,btn2)
                    

        if(dataRecieve(basedir, message.from_user.id, 10) == "категория меню неизестна" and dataRecieve(basedir, message.from_user.id, 1) == "looking the category"):
            
            bot.send_message(message.from_user.id, text="⬇️ выберите блюда ⬇️", reply_markup=keyboard)

            keyboard = types.InlineKeyboardMarkup(row_width=3)

            dataChange(basedir, message.from_user.id, 10, message.data)
            dataChange(basedir, message.from_user.id, 1, "looking the menu")
            dataChange(basedir, message.from_user.id, 11, str(page))
            
            with open(str(basedir) + r'/Storage/images/'+ dirname +"/"+ str(filenames[page - 1]) , "rb") as file:

                count = counting(basedir,message,25,filenames[page - 1])
                
                if (count == "0"):
                    btn1 = types.InlineKeyboardButton(text = "Добавить в корзину", callback_data = filenames[page - 1])
                    keyboard.row(btn1)

                else:
                    btn1 = types.InlineKeyboardButton(text = "-", callback_data = "-- " + filenames[page - 1])
                    btn2 = types.InlineKeyboardButton(text = count + "шт.", callback_data = "none")
                    btn3 = types.InlineKeyboardButton(text = "+", callback_data = "++ " + filenames[page - 1])

                    keyboard.row(btn1,btn2,btn3)

                btn4 = types.InlineKeyboardButton(text = "◀", callback_data = "back")
                btn5 = types.InlineKeyboardButton(text = str(page)+"/"+str(amount), callback_data = "0")
                btn6 = types.InlineKeyboardButton(text = "▶", callback_data = "further")

                
                keyboard.row(btn4,btn5,btn6)

                text = filenames[page - 1]
                text = text.replace(".jpg", "")
                name = text.partition("!")[0]
                text = text.partition("!")[2]
                gramm = text.partition("!")[0]
                ruble = text.partition("!")[2]
                
                caption = str(name + "\n" + gramm +"г/" + ruble + "руб")

                bot.send_photo(message.from_user.id, file, reply_markup=keyboard, caption = caption)

        elif(dataRecieve(basedir, message.from_user.id, 1) == "looking the menu"):
            if(page > 0 and page <= amount):

                keyboard = types.InlineKeyboardMarkup(row_width=3)
                
                with open(str(basedir) + r'/Storage/images/'+ dirname +"/"+ str(filenames[page - 1]) , "rb") as file:
                    
                    count = counting(basedir,message,25,filenames[page - 1])
                
                    if (count == "0"):
                        btn1 = types.InlineKeyboardButton(text = "Добавить в корзину", callback_data = filenames[page - 1])
                        keyboard.row(btn1)

                    else:
                        btn1 = types.InlineKeyboardButton(text = "-", callback_data = "-- " + filenames[page - 1])
                        btn2 = types.InlineKeyboardButton(text = count + "шт.", callback_data = "none")
                        btn3 = types.InlineKeyboardButton(text = "+", callback_data = "++ " + filenames[page - 1])

                        keyboard.row(btn1,btn2,btn3)

                    btn4 = types.InlineKeyboardButton(text = "◀", callback_data = "back")
                    btn5 = types.InlineKeyboardButton(text = str(page)+"/"+str(amount), callback_data = "none")
                    btn6 = types.InlineKeyboardButton(text = "▶", callback_data = "further")

                    
                    keyboard.row(btn4,btn5,btn6)

                    text = filenames[page - 1]
                    text = text.replace(".jpg", "")
                    name = text.partition("!")[0]
                    text = text.partition("!")[2]
                    gramm = text.partition("!")[0]
                    ruble = text.partition("!")[2]
                   
                    caption = str(name + "\n" + gramm +"г/" + ruble + "руб")

                    with open(str(basedir) + r'/Storage/images/'+ dirname +"/"+ filenames[page - 1] , "rb") as file:
                        photo = types.InputMediaPhoto(media = file)

                        
                        if(dataRecieve(basedir, message.from_user.id, 11) != str(page)):
                            bot.edit_message_media(chat_id = message.from_user.id, message_id = message.message.id, media = photo, reply_markup = keyboard, )
                            bot.edit_message_caption(chat_id = message.from_user.id, message_id = message.message.id, caption = caption, reply_markup = keyboard)
                            dataChange(basedir, message.from_user.id, 11, str(page))

                        else:
                            bot.edit_message_reply_markup(chat_id = message.from_user.id, message_id = message.message.id, reply_markup = keyboard)

def showOrder(basedir,message,bot):
    textToReturn = ''

    textToReturn += "\n\n" + "1) Номер телефона:\n- " + dataRecieve(basedir, message.from_user.id, 12)
    if(dataRecieve(basedir, message.from_user.id, 19) == "доставка"):
        textToReturn += "\n\n" + "2) Адрес доставки:\n- " + dataRecieve(basedir, message.from_user.id, 13)
    if(dataRecieve(basedir, message.from_user.id, 19) == "самовывоз"):
        textToReturn += "\n\n" + "2) Самовывоз из:\n- " + dataRecieve(basedir, message.from_user.id, 20)
    textToReturn += "\n\n" + "3) Способ оплаты:\n- " + dataRecieve(basedir, message.from_user.id, 14)
    if(dataRecieve(basedir, message.from_user.id, 15) != ''):
        textToReturn += "\n\n" + "4) Комментарий к заказу:\n- " + dataRecieve(basedir, message.from_user.id, 15)

    textToReturn += "\n\nЗаказ:"

    textToReturn += dataRecieve(basedir, message.from_user.id, 17).replace(";","\n")

    prise = int(dataRecieve(basedir, message.from_user.id, 16))
    discont = dataRecieve(basedir, message.from_user.id, 22)
    if(discont != "неизвестна скидка" and discont != ""):
        prise = prise - (prise / 100 * int(discont))

    if(prise < 600 and dataRecieve(basedir, message.from_user.id, 19) != "самовывоз"):
        prise += 100
        if(discont != "неизвестна скидка" and discont != ""):
            textToReturn += "\n\nСкидка "+ discont +"%"
            textToReturn += "\nДоставка 100руб"
            textToReturn += ("\n" + "Итого: "+ dataRecieve(basedir, message.from_user.id, 16)+" - " + discont + "% " + " + 100 = " + str(int(prise)) + "руб")
        else:  
            textToReturn += "\n\nДоставка 100руб."
            textToReturn += ("\n" + "Итого: "+ dataRecieve(basedir, message.from_user.id, 16) + " + 100 = " + str(prise) + "руб")
    
    else:
        if(discont != "неизвестна скидка" and discont != ""):
            textToReturn += "\n\nСкидка "+ discont +"%"
            textToReturn += ("\n" + "Итого: "+ dataRecieve(basedir, message.from_user.id, 16)+" - " + discont + "% " + " = " + str(int(prise)) + "руб")
        else:
            textToReturn += "\n\n" + "Итого: "+ str(int(prise)) + "руб"

    return textToReturn

def userBot(basedir):

    textToInsert = "Корзина:\nМеню:\nменю неизвестно\nБизнес-ланчи:\n"
    for i in range(100):
        textToInsert = str(textToInsert + "none:" + str(i) + "\n")
    userDataLayout = "действие неизвестно\nналичие неоцененного заказа неизвестно\nкатегория бизнес-ланча неизвестен\nсуп неизвестен\nгорячее неизвестно\nгарнир неизвестен\nсалат неизвестен\nхлеб неизвестен\nнапиток неизвестен\nкатегория меню неизвестна\nстраница неизвестна\nномер неизвестен\nадрес доставки неизвестен\nспособ оплаты неизвестен\nкомментарий к заказу неизвестен\nсумма заказа неизвестна\nзаказ неизвестен\nномер сообщения цены неизвестен\nспособ получения неизвестен\nпункт самовывоза неизвестен\nнеизвестна сумма заказа за месяц\nнеизвестна скидка\n" + textToInsert

    workToken = "6248869227:AAGPNfOpjhIEgYC4opEpUwOouCSpVKEAAEc"
    workbot = telebot.TeleBot(workToken)

    userToken = "5778968531:AAEmYXnNrWlfz4qpdmS8kfO0bgKavtuF-Kk"
    bot = telebot.TeleBot(userToken)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    @bot.message_handler(commands='help')
    def help_message(message):
        print("Клиентский | " + str(datetime.now())+ " | " + str(message.from_user.id) + " | "+ str(message.text))

        file = open(str(basedir) + r'/Storage/help.txt', 'r', encoding='utf-8')
        bot.send_message(message.chat.id, text = file.read() .format(message.from_user))
        file.close()

    @bot.message_handler(commands='start')
    def start_message(message):

        print("Клиентский | " + str(datetime.now())+ " | " + str(message.from_user.id) + " | "+ str(message.text))
        
        if (os.path.isfile(str(basedir) + r'/Storage/users/' + str(message.from_user.id) + ".txt")) != True:

            file = open(str(basedir) + r'/Storage/users/' + str(message.from_user.id) + ".txt", 'a', encoding='utf-8')
            file.write(userDataLayout)
            file.close()

        else:

            file = open(str(basedir) + r'/Storage/users/' + str(message.from_user.id) + ".txt", 'w', encoding='utf-8')
            file.write(userDataLayout)
            file.close()

        keyboard = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton(text = "❌ нет", callback_data = "education-no")
        btn2 = types.InlineKeyboardButton(text = "✅ да", callback_data = "education-yes")
        keyboard.add(btn1,btn2)
        bot.send_message(message.chat.id, text= "Желаете узнать информацию о боте и его функциях?" .format(message.from_user), reply_markup=keyboard)

        dataChange(basedir, message.from_user.id, 1, "chooses answer")
    
    @bot.message_handler(content_types=['text'])
    def main(message):

        print("Клиентский | " + str(datetime.now())+ " | " + str(message.from_user.id) + " | "+ str(message.text))

        if (os.path.isfile(str(basedir) + r'/Storage/users/' + str(message.from_user.id) + ".txt")) != True:
            file = open(str(basedir) + r'/Storage/users/' + str(message.from_user.id) + ".txt", 'a', encoding='utf-8')
            file.write(userDataLayout)
            file.close()

            keyboard = types.InlineKeyboardMarkup(row_width=2)
            btn1 = types.InlineKeyboardButton(text = "❌ нет", callback_data = "education-no")
            btn2 = types.InlineKeyboardButton(text = "✅ да", callback_data = "education-yes")
            keyboard.add(btn1,btn2)
            bot.send_message(message.chat.id, text= "Желаете узнать информацию о боте и его функциях?" .format(message.from_user), reply_markup=keyboard)

            dataChange(basedir, message.from_user.id, 1, "chooses answer")
        
        else:
            
            if (message.text == "Бизнес-ланч" and dataRecieve(basedir, message.from_user.id,1) == "main page"):
                keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)

                btn1 = types.KeyboardButton("🚫 отменить")
                btn2 = types.KeyboardButton("➕ добавить в корзину")

                keyboard.add(btn1,btn2)

                bot.send_message(message.from_user.id, text = "Выберите нужные блюда и добавьте бизнес-ланч в корзину." .format(message.from_user),reply_markup=keyboard)

                dataChange(basedir, message.from_user.id, 1, "business-lunch")
                dataChange(basedir, message.from_user.id, 3, "soups")

                pageBusinessLunch(basedir, message, bot)
            
            elif(message.text == "🚫 отменить" ): 

                dataChange(basedir, message.from_user.id, 3, "категория бизнес-ланча неизвестен")
                dataChange(basedir, message.from_user.id, 4, "суп неизвестен")
                dataChange(basedir, message.from_user.id, 5, "горячее неизвестно")
                dataChange(basedir, message.from_user.id, 6, "гарнир неизвестен")
                dataChange(basedir, message.from_user.id, 7, "салат неизвестен")
                dataChange(basedir, message.from_user.id, 8, "хлеб неизвестен")
                dataChange(basedir, message.from_user.id, 9, "напиток неизвестен") 

                mainPage(basedir, message, bot)

            elif(message.text == "◀ назад" and dataRecieve(basedir, message.from_user.id, 1) != "main page"):
                mainPage(basedir, message, bot)

            elif(message.text == "◀ к категориям" and dataRecieve(basedir, message.from_user.id, 1) == "looking the menu"):
                categoryMenu(basedir,message,bot)

            elif(dataRecieve(basedir, message.from_user.id, 1) == "2 - order"):
                dataChange(basedir, message.from_user.id, 12, message.text)
                dataChange(basedir, message.from_user.id, 1, "2 - order")
            
                keyboard = types.InlineKeyboardMarkup(row_width=1)
                btn1 = types.InlineKeyboardButton(text = "Доставка", callback_data = "2 - order (D)")
                btn2 = types.InlineKeyboardButton(text = "Самовывоз", callback_data = "2 - order (S)")
                keyboard.add(btn1,btn2)

                bot.send_message(message.from_user.id, text = "Выберите способ получения" .format(message.from_user), reply_markup=keyboard)

            elif(dataRecieve(basedir, message.from_user.id, 1) == "2 - order (D)"):   
                dataChange(basedir, message.from_user.id, 1, "3 - order")

                keyboard = types.InlineKeyboardMarkup(row_width=1)
                address = dataRecieve(basedir, message.from_user.id,13)
                if(address != "адрес доставки неизвестен"):
                    
                    btn1 = types.InlineKeyboardButton(text = "Использовать: " + address, callback_data = "3 - order")
                    keyboard.add(btn1)

                bot.send_message(message.from_user.id, text = "2⃣ Напишите адрес доставки:" .format(message.from_user), reply_markup=keyboard)

            elif(dataRecieve(basedir, message.from_user.id, 1) == "3 - order"):
                dataChange(basedir, message.from_user.id, 13, message.text)
                dataChange(basedir, message.from_user.id, 1, "4 - order")
            
                keyboard = types.InlineKeyboardMarkup(row_width=1)
                btn1 = types.InlineKeyboardButton(text = "Переводом", callback_data = "3 - order (P)")
                btn2 = types.InlineKeyboardButton(text = "Наличными", callback_data = "3 - order (N)")
                keyboard.add(btn1,btn2)

                bot.send_message(message.from_user.id, text = "3⃣ Выберите способ оплаты:" .format(message.from_user), reply_markup=keyboard)

            elif(dataRecieve(basedir, message.from_user.id, 1) == "4 - order"):
                dataChange(basedir, message.from_user.id, 15, message.text)
                dataChange(basedir, message.from_user.id, 1, "5 - order")
                
                keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=False)
                btn2 = types.KeyboardButton("🚫 отменить")
                btn1 = types.KeyboardButton("✅ заказать")
                keyboard.row(btn2, btn1)

                order = showOrder(basedir,message,bot)
                bot.send_message(message.from_user.id, text = order .format(message.from_user),reply_markup=keyboard)
                
            elif(dataRecieve(basedir, message.from_user.id, 1) == "5 - order" and message.text == "✅ заказать"):
                order = "❗ новый заказ ❗"
                order += showOrder(basedir,message,bot)
                dataChange(basedir, message.from_user.id, 2, "yes")

                for root, dirs, files in os.walk(basedir + r"/Storage/workers"):  
                        for filename in files:
                            id = filename.replace(".txt","")
                            try:
                                workbot.send_message(id, text = order .format(message.from_user))
                                
                            except:
                                continue
                
                dataChange(basedir, message.from_user.id, 25, "")
                for i in range(100):
                    if(counting(basedir,message,27 + i,"none") != "1"):
                        dataChange(basedir, message.from_user.id, 27 + i, "none")
                    else:
                        break
                
                orderPrise = dataRecieve(basedir, message.from_user.id, 16)
                orderPriseForMounth = dataRecieve(basedir, message.from_user.id, 21)
                if(orderPriseForMounth == "неизвестна сумма заказа за месяц"):
                    orderPriseForMounth = 0
                dataChange(basedir, message.from_user.id, 21, str(int(orderPrise) + int(orderPriseForMounth)))
                
                amountDiscont = dataRecieve(basedir, message.from_user.id, 22)
                if(amountDiscont != "неизвестна скидка" and amountDiscont != ""):
                    dataChange(basedir, message.from_user.id, 22, "")

                with open (str(basedir) + r'/Storage/statistics/numberOrder.txt', 'r', encoding='utf-8') as file:
                    numberOrder = int(file.read())

                numberOrder += 1

                with open (str(basedir) + r'/Storage/statistics/numberOrder.txt', 'w', encoding='utf-8') as file:
                    file.write(str(numberOrder))

                order = " " + dataRecieve(basedir, message.from_user.id, 16)
                with open (str(basedir) + r'/Storage/statistics/orderAmounts.txt', 'a', encoding='utf-8') as file:
                    file.write(order)

                bot.send_message(message.from_user.id, text = "✅ заказ оформлен ✅" .format(message.from_user))             
                bot.send_message(message.from_user.id, text = "В течении 10 минут с вами свяжется оператор для уточнения заказа." .format(message.from_user))
                mainPage(basedir,message,bot)

            elif(message.text == "Акции" and dataRecieve(basedir, message.from_user.id, 1) == "main page" and os.path.isfile(str(basedir) + r'\\Storage\\promotion.txt') == True):
                
                with open (str(basedir) + r'/Storage/promotion.txt', 'r', encoding='utf-8') as file:
                    promotion = file.read()

                bot.send_message(message.from_user.id, text = promotion .format(message.from_user),reply_markup = markup)

            elif(message.text == "Меню" and (dataRecieve(basedir, message.from_user.id, 1) == "main page" or dataRecieve(basedir, message.from_user.id, 1) == "basket")):
                
                categoryMenu(basedir,message,bot)

            elif(message.text == "Оценить нас" and dataRecieve(basedir, message.from_user.id, 2) == "yes"):
                dataChange(basedir, message.from_user.id, 1, "evaluates")

                keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=False)
                btn1 = types.KeyboardButton("◀ назад")
                keyboard.row(btn1)
                             
                bot.send_message(message.from_user.id, text = "Вам понравился последний заказ?" .format(message.from_user),reply_markup=keyboard)

                keyboard = types.InlineKeyboardMarkup(row_width=5)
                btn1 = types.InlineKeyboardButton(text = "1⭐", callback_data = "1")
                btn2 = types.InlineKeyboardButton(text = "2⭐", callback_data = "2")
                btn3 = types.InlineKeyboardButton(text = "3⭐", callback_data = "3")
                btn4 = types.InlineKeyboardButton(text = "4⭐", callback_data = "4")
                btn5 = types.InlineKeyboardButton(text = "5⭐", callback_data = "5")

                keyboard.row(btn1,btn2,btn3,btn4,btn5)

                bot.send_message(message.from_user.id, text = "Оцените его по 5-бальной шкале:" .format(message.from_user),reply_markup=keyboard)

            elif(message.text == "Оценить нас" and dataRecieve(basedir, message.from_user.id, 2) != "yes"):
                mainPage(basedir,message,bot)

            elif(message.text == "➕ добавить в корзину" and dataRecieve(basedir, message.from_user.id, 1) == "business-lunch"):
                businessLunch = ""
                prise = 0
                if(dataRecieve(basedir, message.from_user.id, 4) != "суп неизвестен"):
                    text = dataRecieve(basedir, message.from_user.id, 4)
                    businessLunch = businessLunch + text 
                    
                    file = open(str(basedir) + r'/Storage/businessLunch/prise.txt', "r", encoding='utf-8')
                    for i in range(1):
                        prise1 = file.readline()
                        
                    file.close()
                    
                    prise1 = prise1.replace("\n","")
                    prise1 = prise1.partition(":")[2]
                    prise = int(text.count(":")) * int(prise1)

                if(dataRecieve(basedir, message.from_user.id, 5) != "горячее неизвестно"):
                    text = dataRecieve(basedir, message.from_user.id, 5)
                    businessLunch = businessLunch + text

                    file = open(str(basedir) + r'/Storage/businessLunch/prise.txt', "r",encoding='utf-8')
                    for i in range(2):
                        prise2 = file.readline()
                    file.close()
                    prise2 = prise2.replace("\n","")
                    
                    prise2 = prise2.partition(":")[2]
                    prise = prise +(int(text.count(":")) * int(prise2))

                if(dataRecieve(basedir, message.from_user.id, 6) != "гарнир неизвестен"):
                    text = dataRecieve(basedir, message.from_user.id, 6)
                    businessLunch = businessLunch + text 

                    with open(str(basedir) + r'/Storage/businessLunch/prise.txt', "r",encoding='utf-8') as file3:
                        for i in range(3):
                            prise3 = file3.readline()

                    prise3 = prise3.replace("\n","")
                    prise3 = prise3.partition(":")[2]
                    prise = prise +(int(text.count(":")) * int(prise3))

                if(dataRecieve(basedir, message.from_user.id, 7) != "салат неизвестен"):
                    text = dataRecieve(basedir, message.from_user.id, 7)
                    businessLunch = businessLunch + text 

                    with open(str(basedir) + r'/Storage/businessLunch/prise.txt', "r",encoding='utf-8') as file4:
                        for i in range(4):
                            prise4 = file4.readline()
                    
                    prise4 = prise4.replace("\n","")
                    prise4 = prise4.partition(":")[2]
                    prise = prise +(int(text.count(":")) * int(prise4))

                if(dataRecieve(basedir, message.from_user.id, 8) != "хлеб неизвестен"):
                    text = dataRecieve(basedir, message.from_user.id, 8)
                    businessLunch = businessLunch + text

                    with open(str(basedir) + r'/Storage/businessLunch/prise.txt', "r",encoding='utf-8') as file5:
                        for i in range(5):
                            prise5 = file5.readline()

                    prise5 = prise5.replace("\n","")
                    prise5 = prise5.partition(":")[2]
                    prise = prise +(int(text.count(":")) * int(prise5))

                if(dataRecieve(basedir, message.from_user.id, 9) != "напиток неизвестен"):
                    text = dataRecieve(basedir, message.from_user.id, 9)
                    businessLunch = businessLunch + text 

                    with open(str(basedir) + r'/Storage/businessLunch/prise.txt', "r",encoding='utf-8') as file6:
                        for i in range(6):
                            prise6 = file6.readline()

                    prise6 = prise6.replace("\n","")
                    prise6 = prise6.partition(":")[2]
                    prise = prise +(int(text.count(":")) * int(prise6))

                if(businessLunch != ""):
                    businessLunch = businessLunch + "!" + str(prise) + "!1"
                    for i in range(100):
                        if (counting(basedir,message,27 + i,"none") == "1"):
                            dataChange(basedir, message.from_user.id, 27 + i, businessLunch)
                            bot.send_message(message.from_user.id, text = "Бизнес-ланч добавлен в корзину" .format(message.from_user))
                            break
                    
                    dataChange(basedir, message.from_user.id, 3, "категория бизнес-ланча неизвестен")
                    dataChange(basedir, message.from_user.id, 4, "суп неизвестен")
                    dataChange(basedir, message.from_user.id, 5, "горячее неизвестно")
                    dataChange(basedir, message.from_user.id, 6, "гарнир неизвестен")
                    dataChange(basedir, message.from_user.id, 7, "салат неизвестен")
                    dataChange(basedir, message.from_user.id, 8, "хлеб неизвестен")
                    dataChange(basedir, message.from_user.id, 9, "напиток неизвестен")

                    mainPage(basedir,message,bot)

                else:
                    mainPage(basedir,message,bot)

            elif(message.text == "Корзина" or message.text == "🛒 корзина"):
                basket(basedir, message, bot)

            elif(message.text == "✅ оформить заказ" and dataRecieve(basedir, message.from_user.id, 1) == "basket"):
                keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
                dataChange(basedir, message.from_user.id, 1, "1 - order")

                text = ""

                filenames = dataRecieve(basedir, message.from_user.id,25)
                if(filenames != "меню неизвестно"): 
                    filenames = filenames.replace(" ",";")
                    filenames = filenames.replace(":"," ")
                    filenames = filenames.split()

                    textNoRepetition = []
                    textNoRepetition.extend(set(filenames))
                    
                    for i in range(len(textNoRepetition)):
                        filename = str(textNoRepetition[i]).replace(";"," ")
                        count = counting(basedir,message,25,filename)

                        filename = filename.partition("!")[0]
                        text += ";" + filename + " (" + count + ")" 

                for i in range(100):
                    if(counting(basedir, message, i + 27, "none") != "1"):
                        lunch = dataRecieve(basedir, message.from_user.id,i + 27)
                        count = lunch.partition("!")[2].partition("!")[2]
                        
                        dishs = lunch.partition("!")[0]

                        dishs = dishs.replace(" ",";")
                        dishs = dishs.replace(":"," ")
                        dishs = dishs.split()

                        textNoRepetition = []
                        textNoRepetition.extend(set(dishs))
                        
                        text += ";;Бизнес-ланч:"

                        for o in range(len(textNoRepetition)):
                            
                            text = text + ";" + textNoRepetition[o].replace(";"," ") + " (" + counting(basedir, message, i + 27, textNoRepetition[o]) + ")"
                        
                dataChange(basedir, message.from_user.id, 17, text)
                dataChange(basedir, message.from_user.id, 16, countingPrise(basedir,message,bot))

                text = "Ваш заказ:\n" + text.replace(";","\n")
                
                keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
                dataChange(basedir, message.from_user.id, 1, "2 - order")
                
                btn1 = types.KeyboardButton("🚫 отменить")
                keyboard.add(btn1)

                bot.send_message(message.from_user.id, text = "...", reply_markup=keyboard)

                keyboard = types.InlineKeyboardMarkup(row_width=1)
                
                number = dataRecieve(basedir, message.from_user.id,12)

                if(number != "номер неизвестен"):
                    
                    btn1 = types.InlineKeyboardButton(text = "Использовать: " + number, callback_data = "2 - order")
                    keyboard.row(btn1)

                bot.send_message(message.from_user.id, text = "1⃣ Напишите номер телефона:", reply_markup=keyboard)

    @bot.callback_query_handler(func=lambda call: True)
    def inline(message):
        print("Клиентский | " + str(datetime.now())+ " | " + str(message.from_user.id) + " | "+ str(message.data))

        if (os.path.isfile(str(basedir) + r'/Storage/users/' + str(message.from_user.id) + ".txt")) != True:

            file = open(str(basedir) + r'/Storage/users/' + str(message.from_user.id) + ".txt", 'a', encoding='utf-8')
            file.write(userDataLayout)
            file.close()
            
            with open (str(basedir) + r'/Storage/startInfo/1-page.txt', 'r', encoding = "utf-8") as f:
                infoToReturn = str(f.read())
                infoToReturn = infoToReturn.replace(r"\n", "\n")
                infoToReturn = infoToReturn.replace(r"/n", "\n")
                
                keyboard = types.InlineKeyboardMarkup(row_width=1)
                btn1 = types.InlineKeyboardButton(text = "Продолжить ➡️", callback_data = "education-continue")
                keyboard.add(btn1)
                bot.send_message(message.from_user.id, text = infoToReturn .format(message.from_user),reply_markup=keyboard)

            dataChange(basedir, message.from_user.id, 1, "chooses answer")

        elif(dataRecieve(basedir, message.from_user.id, 1) == "chooses answer"):
            if(message.data == "education-yes" or message.data == "education-continue" or message.data == "education-continue_2"):
                if(message.data == "education-yes"):

                    with open (str(basedir) + r'/Storage/startInfo/1-page.txt', 'r', encoding = "utf-8") as f:
                        infoToReturn = str(f.read())
                        infoToReturn = infoToReturn.replace(r"\n", "\n")
                        infoToReturn = infoToReturn.replace(r"/n", "\n")

                        keyboard = types.InlineKeyboardMarkup(row_width=1)
                        btn1 = types.InlineKeyboardButton(text = "Продолжить ➡️", callback_data = "education-continue")
                        keyboard.add(btn1)
                        bot.send_message(message.from_user.id, text = infoToReturn .format(message.from_user),reply_markup=keyboard)

                elif(message.data == "education-continue"):
                    with open (str(basedir) + r'/Storage/startInfo/2-page.txt', 'r', encoding = "utf-8") as f:
                        infoToReturn = str(f.read())
                        infoToReturn = infoToReturn.replace(r"\n", "\n")
                        infoToReturn = infoToReturn.replace(r"/n", "\n")
        
                        keyboard = types.InlineKeyboardMarkup(row_width=1)
                        btn1 = types.InlineKeyboardButton(text = "Продолжить ➡️", callback_data = "education-continue_2")
                        keyboard.add(btn1)
                        bot.send_message(message.from_user.id, text = infoToReturn .format(message.from_user),reply_markup=keyboard)

                elif(message.data == "education-continue_2"):
                    with open (str(basedir) + r'/Storage/startInfo/3-page.txt', 'r', encoding = "utf-8") as f:
                        infoToReturn = str(f.read())
                        infoToReturn = infoToReturn.replace(r"\n", "\n")
                        infoToReturn = infoToReturn.replace(r"/n", "\n")

                        keyboard = types.InlineKeyboardMarkup(row_width=1)
                        btn1 = types.InlineKeyboardButton(text = "Продолжить ➡️", callback_data = "education-no")
                        keyboard.add(btn1)
                        bot.send_message(message.from_user.id, text = infoToReturn .format(message.from_user),reply_markup=keyboard)

            elif(message.data == "education-no"):
                mainPage(basedir, message, bot)

        elif(message.data == "none"):
            ...
        
        elif(message.data == "2 - order"):
            dataChange(basedir, message.from_user.id, 1, "2 - order")
            
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            btn1 = types.InlineKeyboardButton(text = "Доставка", callback_data = "2 - order (D)")
            btn2 = types.InlineKeyboardButton(text = "Самовывоз", callback_data = "2 - order (S)")
            keyboard.add(btn1,btn2)

            bot.send_message(message.from_user.id, text = "Выберите способ получения" .format(message.from_user), reply_markup=keyboard)

        elif(message.data == "2 - order (D)"):
            dataChange(basedir, message.from_user.id, 1, "3 - order")
            dataChange(basedir, message.from_user.id, 19, "доставка")

            address = dataRecieve(basedir, message.from_user.id,13)
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            if(address != "адрес доставки неизвестен"):
                
                btn1 = types.InlineKeyboardButton(text = "Использовать: " + address, callback_data = "3 - order")
                keyboard.add(btn1)

            bot.send_message(message.from_user.id, text = "2⃣ Напишите адрес доставки:" .format(message.from_user), reply_markup=keyboard)

        elif(message.data == "2 - order (S)"):
            dataChange(basedir, message.from_user.id, 1, "3 - order (S)")
            dataChange(basedir, message.from_user.id, 19, "самовывоз")

            keyboard = types.InlineKeyboardMarkup(row_width=1)
            btn1 = types.InlineKeyboardButton(text = "Серпухов ТЦ \"Атлас\"", callback_data = "3 - order (S)")
            keyboard.add(btn1)

            bot.send_message(message.from_user.id, text = "2⃣ Выберите пункт самовывоза:" .format(message.from_user), reply_markup=keyboard)

        elif(message.data == "3 - order (S)"):
            dataChange(basedir, message.from_user.id, 1, "4 - order")
            dataChange(basedir, message.from_user.id, 20, "Серпухов ТЦ \"Атлас\"")

            keyboard = types.InlineKeyboardMarkup(row_width=1)
            btn1 = types.InlineKeyboardButton(text = "Переводом", callback_data = "3 - order (P)")
            btn2 = types.InlineKeyboardButton(text = "Наличными", callback_data = "3 - order (N)")
            keyboard.add(btn1,btn2)

            bot.send_message(message.from_user.id, text = "3⃣ Выберите способ оплаты:" .format(message.from_user), reply_markup=keyboard)

        elif(message.data == "3 - order"):
            dataChange(basedir, message.from_user.id, 1, "4 - order")
            
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            btn1 = types.InlineKeyboardButton(text = "Переводом", callback_data = "3 - order (P)")
            btn2 = types.InlineKeyboardButton(text = "Наличными", callback_data = "3 - order (N)")
            keyboard.add(btn1,btn2)

            bot.send_message(message.from_user.id, text = "3⃣ Выберите способ оплаты:" .format(message.from_user), reply_markup=keyboard)

        elif(message.data == "3 - order (P)"):
            dataChange(basedir, message.from_user.id, 1, "4 - order")
            dataChange(basedir, message.from_user.id, 14, "перевод")

            keyboard = types.InlineKeyboardMarkup(row_width=1)
            btn1 = types.InlineKeyboardButton(text = "Пропустить", callback_data = "5 - order")
            keyboard.add(btn1)

            bot.send_message(message.from_user.id, text = "4⃣ Напишите комментарий к заказу:" .format(message.from_user), reply_markup=keyboard)

        elif(message.data == "3 - order (N)"):
            dataChange(basedir, message.from_user.id, 1, "4 - order")
            dataChange(basedir, message.from_user.id, 14, "наличные")

            keyboard = types.InlineKeyboardMarkup(row_width=1)
            btn1 = types.InlineKeyboardButton(text = "Пропустить", callback_data = "5 - order")
            keyboard.add(btn1)

            bot.send_message(message.from_user.id, text = "4⃣ Напишите комментарий к заказу:" .format(message.from_user), reply_markup=keyboard)

        elif(message.data == "4 - order"):
            dataChange(basedir, message.from_user.id, 1, "4 - order")
            dataChange(basedir, message.from_user.id, 14, "наличные")

            keyboard = types.InlineKeyboardMarkup(row_width=1)
            btn1 = types.InlineKeyboardButton(text = "Пропустить", callback_data = "5 - order")
            keyboard.add(btn1)

            bot.send_message(message.from_user.id, text = "4⃣ Напишите комментарий к заказу:" .format(message.from_user), reply_markup=keyboard)

        elif(message.data == "5 - order"):
            dataChange(basedir, message.from_user.id, 15, "")
            dataChange(basedir, message.from_user.id, 1, "5 - order")
            
            keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=False)
            btn2 = types.KeyboardButton("🚫 отменить")
            btn1 = types.KeyboardButton("✅ заказать")
            keyboard.row(btn2, btn1)

            order = showOrder(basedir,message,bot)
            bot.send_message(message.from_user.id, text = order .format(message.from_user),reply_markup=keyboard)

        elif(dataRecieve(basedir, message.from_user.id, 1) == "business-lunch"):

            if(message.data == "further"):
                if(dataRecieve(basedir, message.from_user.id, 3) == "soups"):
                    dataChange(basedir, message.from_user.id, 3, "firstCourse")
                    editPageBusinessLunch(basedir,message,bot)

                elif(dataRecieve(basedir, message.from_user.id, 3) == "firstCourse"):
                    dataChange(basedir, message.from_user.id, 3, "garnish")
                    editPageBusinessLunch(basedir,message,bot)

                elif(dataRecieve(basedir, message.from_user.id, 3) == "garnish"):
                    dataChange(basedir, message.from_user.id, 3, "salad")
                    editPageBusinessLunch(basedir,message,bot)

                elif(dataRecieve(basedir, message.from_user.id, 3) == "salad"):
                    dataChange(basedir, message.from_user.id, 3, "bread")
                    editPageBusinessLunch(basedir,message,bot)

                elif(dataRecieve(basedir, message.from_user.id, 3) == "bread"):
                    dataChange(basedir, message.from_user.id, 3, "drink")
                    editPageBusinessLunch(basedir,message,bot)

            elif(message.data == "back"):
                if(dataRecieve(basedir, message.from_user.id, 3) == "firstCourse"):
                    dataChange(basedir, message.from_user.id, 3, "soups")
                    editPageBusinessLunch(basedir,message,bot)

                elif(dataRecieve(basedir, message.from_user.id, 3) == "garnish"):
                    dataChange(basedir, message.from_user.id, 3, "firstCourse")
                    editPageBusinessLunch(basedir,message,bot)

                elif(dataRecieve(basedir, message.from_user.id, 3) == "salad"):
                    dataChange(basedir, message.from_user.id, 3, "garnish")
                    editPageBusinessLunch(basedir,message,bot)

                elif(dataRecieve(basedir, message.from_user.id, 3) == "bread"):
                    dataChange(basedir, message.from_user.id, 3, "salad")
                    editPageBusinessLunch(basedir,message,bot)

                elif(dataRecieve(basedir, message.from_user.id, 3) == "drink"):
                    dataChange(basedir, message.from_user.id, 3, "bread")
                    editPageBusinessLunch(basedir,message,bot)

            else:
                
                if(dataRecieve(basedir, message.from_user.id, 3) == "soups"):
                    textToInsert = dataRecieve(basedir, message.from_user.id, 4)
                    textToInsert = textToInsert.replace("суп неизвестен","")
                    dataChange(basedir, message.from_user.id, 4, textToInsert  + message.data + ":")
                    editPageBusinessLunch(basedir,message,bot)

                elif(dataRecieve(basedir, message.from_user.id, 3) == "firstCourse"):
                    textToInsert = dataRecieve(basedir, message.from_user.id, 5)
                    textToInsert = textToInsert.replace("горячее неизвестно","")
                    dataChange(basedir, message.from_user.id, 5, textToInsert  + message.data + ":")
                    editPageBusinessLunch(basedir,message,bot)

                elif(dataRecieve(basedir, message.from_user.id, 3) == "garnish"):
                    textToInsert = dataRecieve(basedir, message.from_user.id, 6)
                    textToInsert = textToInsert.replace("гарнир неизвестен","")
                    dataChange(basedir, message.from_user.id, 6, textToInsert  + message.data + ":")
                    editPageBusinessLunch(basedir,message,bot)

                elif(dataRecieve(basedir, message.from_user.id, 3) == "salad"):
                    textToInsert = dataRecieve(basedir, message.from_user.id, 7)
                    textToInsert = textToInsert.replace("салат неизвестен","")
                    dataChange(basedir, message.from_user.id, 7, textToInsert  + message.data + ":")
                    editPageBusinessLunch(basedir,message,bot)

                elif(dataRecieve(basedir, message.from_user.id, 3) == "bread"):
                    textToInsert = dataRecieve(basedir, message.from_user.id, 8)
                    textToInsert = textToInsert.replace("хлеб неизвестен","")
                    dataChange(basedir, message.from_user.id, 8, textToInsert  + message.data + ":")
                    editPageBusinessLunch(basedir,message,bot)

                elif(dataRecieve(basedir, message.from_user.id, 3) == "drink"):
                    textToInsert = dataRecieve(basedir, message.from_user.id, 9)
                    textToInsert = textToInsert.replace("напиток неизвестен","")
                    dataChange(basedir, message.from_user.id, 9, textToInsert  + message.data + ":")
                    editPageBusinessLunch(basedir,message,bot)

        elif(dataRecieve(basedir, message.from_user.id, 1) == "looking the category" and dataRecieve(basedir, message.from_user.id, 11) == "страница неизвестна"):
            message.data = message.data.replace("@","")
            pageMenu(basedir,message,bot,1)

        elif(dataRecieve(basedir, message.from_user.id, 1) == "looking the menu" and message.data == "further"):
            message.data = message.data.replace("@","")
            page = int(dataRecieve(basedir, message.from_user.id, 11))
            pageMenu(basedir,message,bot,page + 1)

        elif(dataRecieve(basedir, message.from_user.id, 1) == "looking the menu" and message.data == "back"):
            message.data = message.data.replace("@","")
            page = int(dataRecieve(basedir, message.from_user.id, 11))
            pageMenu(basedir,message,bot,page - 1)
        
        

        elif("++" in message.data ):
            afterMessage = message.data
            message.data = message.data.replace("++ ","")
            if("@" in message.data):
                ...
            elif("$" in message.data):
                message.data = int(message.data.replace("$",""))
                text = dataRecieve(basedir, message.from_user.id, message.data)
                name = text.partition("!")[0]
                ruble = text.partition("!")[2].partition("!")[0]
                count = int(text.partition("!")[2].partition("!")[2])
                
                newText = name+"!"+ruble+"!"+str(count + 1)
                
                dataChange(basedir,message.from_user.id, message.data, newText)
                message.data = afterMessage
                basket(basedir, message, bot)

            else:
                textToInsert = dataRecieve(basedir, message.from_user.id, 25)
                dataChange(basedir,message.from_user.id, 25,str(textToInsert + message.data + ":"))

                if(dataRecieve(basedir, message.from_user.id, 1) == "basket"):
                    message.data = afterMessage
                    basket(basedir, message, bot)
                else:
                    page = int(dataRecieve(basedir, message.from_user.id, 11))
                    pageMenu(basedir,message,bot,page)

        elif("--" in message.data):
            afterMessage = message.data 
            message.data = message.data.replace("-- ","")

            if("$" in message.data):
                message.data = int(message.data.replace("$",""))
                text = dataRecieve(basedir, message.from_user.id, message.data)
                name = text.partition("!")[0]
                ruble = text.partition("!")[2].partition("!")[0]
                count = int(text.partition("!")[2].partition("!")[2])

                newText = name+"!"+ruble+"!"+str(count - 1)
                dataChange(basedir,message.from_user.id, message.data, newText)
                message.data = afterMessage
                basket(basedir, message, bot)
            
            else:
                textToInsert = removeDish(basedir,message, 25, message.data)
                dataChange(basedir,message.from_user.id, 25,textToInsert)

                if(dataRecieve(basedir, message.from_user.id, 1) == "basket"):
                    message.data = afterMessage
                    basket(basedir, message, bot)
                else:
                    page = int(dataRecieve(basedir, message.from_user.id, 11))
                    pageMenu(basedir,message,bot,page)

        elif("delete" in message.data):
            
            message.data = message.data.replace("delete","")
            if("$" in message.data):
                message.data = message.data.replace("$","")
                bot.delete_message(message.from_user.id, message.message.id)
                dataChange(basedir,message.from_user.id, int(message.data), "none")
                bot.edit_message_text(chat_id = message.from_user.id, message_id = int(dataRecieve(basedir, message.from_user.id,18)), text = "Итого: " + countingPrise(basedir,message,bot) + "руб")
                
                if((dataRecieve(basedir, message.from_user.id, 25) == ""or dataRecieve(basedir, message.from_user.id, 25) == "меню неизвестно") and "none" in dataRecieve(basedir, message.from_user.id, 27)):
                    bot.delete_message(message.from_user.id, int(dataRecieve(basedir, message.from_user.id, 18)))
                    bot.send_message(message.from_user.id, text = "Ваша корзина пуста!" .format(message.from_user))
                    mainPage(basedir,message,bot)

            else:

                count = int(counting(basedir,message,25, message.data))
                for i in range(count):
                    
                    dataChange(basedir,message.from_user.id, 25,removeDish(basedir,message,25,message.data))
                bot.delete_message(message.from_user.id, message.message.id)
                bot.edit_message_text(chat_id = message.from_user.id, message_id = int(dataRecieve(basedir, message.from_user.id,18)), text = "Итого: " + countingPrise(basedir,message,bot) + "руб")
                
                if((dataRecieve(basedir, message.from_user.id, 25) == "" or dataRecieve(basedir, message.from_user.id, 25) == "меню неизвестно") and "none" in dataRecieve(basedir, message.from_user.id, 27)):
                    bot.delete_message(message.from_user.id, int(dataRecieve(basedir, message.from_user.id, 18)))
                    bot.send_message(message.from_user.id, text = "Ваша корзина пуста!" .format(message.from_user))
                    mainPage(basedir,message,bot)

        elif(dataRecieve(basedir, message.from_user.id, 1) == "looking the menu" and dataRecieve(basedir, message.from_user.id, 11) != "страница неизвестна"):
            if("@" in message.data):
                ...
            else:
                if(dataRecieve(basedir, message.from_user.id, 25) == "меню неизвестно"):
                    dataChange(basedir,message.from_user.id, 25,str(message.data + ":"))

                    page = int(dataRecieve(basedir, message.from_user.id, 11))
                    pageMenu(basedir,message,bot,page)
                else:
                    textToInsert = dataRecieve(basedir, message.from_user.id, 25)
                    dataChange(basedir,message.from_user.id, 25,str(textToInsert + message.data + ":"))

                    page = int(dataRecieve(basedir, message.from_user.id, 11))
                    pageMenu(basedir,message,bot,page)
        
        elif(dataRecieve(basedir, message.from_user.id, 1) == "evaluates" and dataRecieve(basedir, message.from_user.id, 2) == "yes"):

            with open(str(basedir) + r'/Storage/statistics/evaluations.txt', 'r', encoding='utf-8') as file:              
                pastText = file.read()
            
            pastText += " " + str(message.data)

            with open(str(basedir) + r'/Storage/statistics/evaluations.txt', 'w', encoding='utf-8') as file:
                file.write(pastText)
                
            dataChange(basedir, message.from_user.id, 2, "no")
            bot.send_message(message.from_user.id, text = "Спасибо, ваше мнение очень важно для нас!" .format(message.from_user))
            mainPage(basedir,message,bot)


    bot.remove_webhook()
    bot.infinity_polling()
