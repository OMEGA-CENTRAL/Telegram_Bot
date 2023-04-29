import time
import telebot
import os
from datetime import datetime

def dataChange(basedir, IDforChange, lineNumberToChange, replacementText):

    replacementText = replacementText + str(hex(lineNumberToChange)) +"\n"

    with open(str(basedir) + r'\\Storage\\users\\' + str(IDforChange)+ ".txt", 'r', encoding='utf-8') as file:              
        for i in range(lineNumberToChange):
            lineToChange = file.readline()
        file.close()
    
    with open (str(basedir) + r'\\Storage\\users\\' + str(IDforChange)+".txt", 'r', encoding='utf-8') as f:
        old_data = f.read()
    
    new_data = old_data.replace(lineToChange, replacementText)
    
    with open (str(basedir) + r'\\Storage\\users\\' + str(IDforChange) + ".txt", 'w', encoding='utf-8') as f:
        f.write(new_data)


def dataRecieve(basedir, IDforRecieve, lineNumberToRecieve):

    file = open(str(basedir) + r'\\Storage\\users\\' + str(IDforRecieve)+".txt", 'r', encoding='utf-8')
    for i in range(lineNumberToRecieve):
        lineToReturn = file.readline()
    file.close()

    lineToReturn = lineToReturn.replace("\n","")
    lineToReturn = lineToReturn.replace(str(hex(lineNumberToRecieve)), "")
    return lineToReturn

def startTimeWaiting():
    basedir = os.path.dirname(__file__)
    current_datetime = datetime.now()

    while True:
        if(current_datetime.day == 23):
            print("Обновление статистики")

            countingNewUsers(basedir)
            countingOrders(basedir)
            avaregeOrder(basedir)
            distributionShares(basedir)

        time.sleep(86400)

def countingNewUsers(basedir):
    numberUsers = 0
    for root, dirs, files in os.walk(basedir + r"\Storage\users"):  
            for file in files:
                numberUsers += 1

    with open (str(basedir) + r'\\Storage\\statistics\\usersLastMouth.txt', 'r', encoding='utf-8') as file:
          numberUsersLastMouth = file.read()      

    with open (str(basedir) + r'\\Storage\\statistics\\users.txt', 'w', encoding='utf-8') as file:
          file.write(str(numberUsers - int(numberUsersLastMouth)))

    with open (str(basedir) + r'\\Storage\\statistics\\usersLastMouth.txt', 'w', encoding='utf-8') as file:
          file.write(str(numberUsers))

def countingOrders(basedir):
    with open (str(basedir) + r'\\Storage\\statistics\\numberOrder.txt', 'r', encoding='utf-8') as file:
        numberOrder = file.read()
    
    with open (str(basedir) + r'\\Storage\\statistics\\numberOrderLastMouth.txt', 'w', encoding='utf-8') as file:
        file.write(str(numberOrder))

    with open (str(basedir) + r'\\Storage\\statistics\\numberOrder.txt', 'w', encoding='utf-8') as file:
        file.write("0")

def avaregeOrder(basedir):

    with open(str(basedir) + r'\\Storage\\statistics\\orderAmounts.txt', 'r', encoding='utf-8') as file:              
        orders = file.read()
    
    averageOrder = 0
    if(orders != ""):
        orders = orders.split()
        for i in range(len(orders)):
            averageOrder += int(orders[i])

        averageOrder = float(averageOrder / len(orders))
        averageOrder = round(averageOrder, 2)
    
    with open(str(basedir) + r'\\Storage\\statistics\\averageCheckLastMouth.txt', 'w', encoding='utf-8') as file:              
        file.write(str(averageOrder))

    with open(str(basedir) + r'\\Storage\\statistics\\orderAmounts.txt', 'w', encoding='utf-8') as file:              
        file.write("")

def distributionShares(basedir):

    userToken = "5778968531:AAEmYXnNrWlfz4qpdmS8kfO0bgKavtuF-Kk"
    bot = telebot.TeleBot(userToken)

    with open(str(basedir) + r'\\Storage\\minimumOrderAmount.txt', 'r', encoding='utf-8') as file:              
                    minimumOrderAmount = file.read()

    with open(str(basedir) + r'\\Storage\\amountDiscont.txt', 'r', encoding='utf-8') as file:              
                    amountDiscont = file.read()

    amount = 0

    for root, dirs, files in os.walk(basedir + r"\Storage\users"):  
            for file in files:

                file = str(file)
                file = file.replace(".txt","")
                orderPrise = dataRecieve(basedir, file, 21)
                
                if(orderPrise == "" or orderPrise == "неизвестна сумма заказа за месяц"):
                    dataChange(basedir, file, 22, str(amountDiscont))
                    bot.send_message(file, text= "🤩 Самое время насладиться нашей едой! Вам выдана скидка в 10% на следующий заказ." + amountDiscont + "%")
                    amount += 1

                elif(int(orderPrise) <= int(minimumOrderAmount)):
                    dataChange(basedir, file, 22, str(amountDiscont))
                    bot.send_message(file, text= "🤩 Самое время насладиться нашей едой! Вам выдана скидка в 10% на следующий заказ." + amountDiscont + "%")
                    amount += 1
                
                dataChange(basedir, file, 21, "0")

    with open(str(basedir) + r'\\Storage\\statistics\\amountsDiscont.txt', 'w', encoding='utf-8') as file:              
        file.write(str(amount))

