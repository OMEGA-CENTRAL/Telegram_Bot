from datetime import datetime
import time
from PIL import Image, ImageDraw, ImageFont


def creatingPictures(firstNameImage, secondNameImage, thirdNameImage, fourthNameImage, namePage, numberPage, savePath, basedir):
    try:

        colorForNumber = (148,210,75)
        colorForName = "white"
        colorForBackground = "white"
        colorForGramm = "white"
        colorForPrise = (148,210,75)
        colorForTop = (148,210,75)

        startTime = time.time()

        log  = (str(datetime.now()) + ' Картинка: '+ str(namePage) + ' ' + str(numberPage) + ' страница - начато создание...' + '\n')

        logs = open(str(basedir) + r'\Storage\logs.txt', 'a', encoding='utf-8')
        logs.write(log)
        logs.close()

        fontForName = ImageFont.truetype(basedir + r'\WorkBot\Fonts\font.ttf', size = 78)
        fontForPage = ImageFont.truetype(basedir + r'\WorkBot\Fonts\font.ttf', size = 64)
        fontForNumbers = ImageFont.truetype(basedir + r'\WorkBot\Fonts\font.ttf', size = 78)
        fontForNameImage = ImageFont.truetype(basedir + r'\WorkBot\Fonts\font.ttf', size = 38)

        Background = Image.new('RGB', (1200, 1400), color = colorForBackground)

        firstPath = str(basedir + r"\\Storage\\images\\" + namePage + r"\\" + firstNameImage + '.jpg')
        if(secondNameImage != 'empty'):
            secondPath = str(basedir + r"\\Storage\\images\\" + namePage + r"\\" + secondNameImage + '.jpg')
        if(thirdNameImage != 'empty'):
            thirdPath = str(basedir + r"\\Storage\\images\\" + namePage + r"\\" + thirdNameImage + '.jpg')
        if(fourthNameImage != 'empty'):
            fourthPath = str(basedir + r"\\Storage\\images\\" + namePage + r"\\" + fourthNameImage + '.jpg')

        firstImage = Image.open(firstPath).convert('RGBA')
        if(secondNameImage != 'empty'):
            secondImage = Image.open(secondPath).convert('RGBA')
        if(thirdNameImage != 'empty'):
            thirdImage = Image.open(thirdPath).convert('RGBA')
        if(fourthNameImage != 'empty'):
            fourthImage = Image.open(fourthPath).convert('RGBA')
        
        firstImage = firstImage.resize((600,600))
        if(secondNameImage != 'empty'):
            secondImage = secondImage.resize((600,600))
        if(thirdNameImage != 'empty'):
            thirdImage = thirdImage.resize((600,600))
        if(fourthNameImage != 'empty'):
            fourthImage = fourthImage.resize((600,600))

        Background.paste(firstImage,(0,200),firstImage)
        if(secondNameImage != 'empty'):
            Background.paste(secondImage,(600,200),secondImage)
        if(thirdNameImage != 'empty'):
            Background.paste(thirdImage,(0,800),thirdImage)
        if(fourthNameImage != 'empty'):
            Background.paste(fourthImage,(600,800),fourthImage)


        draw = ImageDraw.Draw(Background)

        draw.rectangle((0,0, 1200, 200), fill = colorForTop)
        draw.line((0,202,1200,202), fill = 'black', width=5)
        draw.line((600,200,600,1400), fill = 'black', width=5)
        draw.line((0,800,1200,800), fill = 'black', width=5)

        draw.text((600,60), namePage, fill = 'black', font = fontForName, anchor= 'mm')
        draw.text((600,140), (str(numberPage) + ' страница'), fill = 'black', font = fontForPage, anchor= 'mm')

        #Номера

        draw.ellipse((20,220,130,330), fill=colorForNumber, outline=(0,0,0),width=5)
        if(secondNameImage != 'empty'):
            draw.ellipse((620,220,730,330), fill=colorForNumber, outline=(0,0,0),width=5)
        if(thirdNameImage != 'empty'):
            draw.ellipse((20,820,130,930), fill=colorForNumber, outline=(0,0,0),width=5)
        if(fourthNameImage != 'empty'):
            draw.ellipse((620,820,730,930), fill=colorForNumber, outline=(0,0,0),width=5)

        draw.text((75,275), '1', fill = 'black', font = fontForNumbers, anchor= 'mm')
        if(secondNameImage != 'empty'):
            draw.text((675,275), '2', fill = 'black', font = fontForNumbers, anchor= 'mm')
        if(thirdNameImage != 'empty'):
            draw.text((75,875), '3', fill = 'black', font = fontForNumbers, anchor= 'mm')
        if(fourthNameImage != 'empty'):
            draw.text((675,875), '4', fill = 'black', font = fontForNumbers, anchor= 'mm')

        #Названия

        draw.rounded_rectangle((180, 230, 580, 320), fill=colorForName, outline="black",width=1, radius=30)
        if(secondNameImage != 'empty'):
            draw.rounded_rectangle((780, 230, 1180, 320), fill=colorForName, outline="black",width=1, radius=30)
        if(thirdNameImage != 'empty'):
            draw.rounded_rectangle((180, 830, 580, 920), fill=colorForName, outline="black",width=1, radius=30)
        if(fourthNameImage != 'empty'):
            draw.rounded_rectangle((780, 830, 1180, 920), fill=colorForName, outline="black",width=1, radius=30)

        draw.text((380,275), firstNameImage.partition('!')[0], fill = 'black', font = fontForNameImage, anchor= 'mm')
        if(secondNameImage != 'empty'):
            draw.text((980,275), secondNameImage.partition('!')[0], fill = 'black', font = fontForNameImage, anchor= 'mm')
        if(thirdNameImage != 'empty'):
            draw.text((380,875), thirdNameImage.partition('!')[0], fill = 'black', font = fontForNameImage, anchor= 'mm')
        if(fourthNameImage != 'empty'):
            draw.text((980,875), fourthNameImage.partition('!')[0], fill = 'black', font = fontForNameImage, anchor= 'mm')

        #Граммы

        firstNameImage = firstNameImage.partition('!') [2]
        if(secondNameImage != 'empty'):
            secondNameImage = secondNameImage.partition('!') [2]
        if(thirdNameImage != 'empty'):
            thirdNameImage = thirdNameImage.partition('!') [2]
        if(fourthNameImage != 'empty'):
            fourthNameImage = fourthNameImage.partition('!') [2]
        
        draw.rounded_rectangle((20, 720, 130, 780), fill=colorForGramm, outline="black",width=1, radius=20)
        if(secondNameImage != 'empty'):
            draw.rounded_rectangle((620, 720, 730, 780), fill=colorForGramm, outline="black",width=1, radius=20)
        if(thirdNameImage != 'empty'):
            draw.rounded_rectangle((20, 1320, 130, 1380), fill=colorForGramm, outline="black",width=1, radius=20)
        if(fourthNameImage != 'empty'):
            draw.rounded_rectangle((620, 1320, 730, 1380), fill=colorForGramm, outline="black",width=1, radius=20)

        draw.text((75,750), firstNameImage.partition('!')[0] + 'г', fill = 'black', font = fontForNameImage, anchor= 'mm')
        if(secondNameImage != 'empty'):
            draw.text((675,750), secondNameImage.partition('!')[0] + 'г', fill = 'black', font = fontForNameImage, anchor= 'mm')
        if(thirdNameImage != 'empty'):
            draw.text((75,1350), thirdNameImage.partition('!')[0] + 'г', fill = 'black', font = fontForNameImage, anchor= 'mm')
        if(fourthNameImage != 'empty'):
            draw.text((675,1350), fourthNameImage.partition('!')[0] + 'г', fill = 'black', font = fontForNameImage, anchor= 'mm')

        #Ценники

        draw.rounded_rectangle((400, 720, 580, 780), fill=colorForPrise, outline="black",width=1, radius=20)
        if(secondNameImage != 'empty'):
            draw.rounded_rectangle((1000, 720, 1180, 780), fill=colorForPrise, outline="black",width=1, radius=20)
        if(thirdNameImage != 'empty'):
            draw.rounded_rectangle((400, 1320, 580, 1380), fill=colorForPrise, outline="black",width=1, radius=20)
        if(fourthNameImage != 'empty'):
            draw.rounded_rectangle((1000, 1320, 1180, 1380), fill=colorForPrise, outline="black",width=1, radius=20)

        draw.text((490,750), firstNameImage.partition('!')[2] + ' руб', fill = 'black', font = fontForNameImage, anchor= 'mm')
        if(secondNameImage != 'empty'):
            draw.text((1090,750), secondNameImage.partition('!')[2] + ' руб', fill = 'black', font = fontForNameImage, anchor= 'mm')
        if(thirdNameImage != 'empty'):
            draw.text((490,1350), thirdNameImage.partition('!')[2] + ' руб', fill = 'black', font = fontForNameImage, anchor= 'mm')
        if(fourthNameImage != 'empty'):
            draw.text((1090,1350), fourthNameImage.partition('!')[2] + ' руб', fill = 'black', font = fontForNameImage, anchor= 'mm')

        Background = Background.resize((1200,1400))

        Background.save(savePath)

        leadTime = time.time() - startTime
        log  = (str(datetime.now()) + ' Картинка: '+ str(namePage) + ' ' + str(numberPage) + ' страница - успешно создана за ' + str(round(leadTime,3)) + ' ms' + '\n')
        
        logs = open(str(basedir) + r'\Storage\logs.txt', 'a',encoding='utf-8')
        logs.write(log)
        logs.close()

    except:

        log  = (str(datetime.now()) + ' Картинка: '+ str(namePage) + ' ' + str(numberPage) + ' страница - ошибка при создании!' + '\n')
        
        logs = open(str(basedir) + r'\Storage\logs.txt', 'a',encoding='utf-8')
        logs.write(log)
        logs.close()

        print("Ошибка!")
