import os
from . import creatingPictures as creatingPictures

def distribution(basedir, folderName):

    filenames = []
    amount = 0

    for root, dirs, files in os.walk(basedir + r"/Storage/images/" + folderName):  
        for filename in files:

            amount += 1
            filename = filename.replace('.jpg','')
            filenames.append(filename)

    for root, dirs, files in os.walk(basedir + r"/Storage/imagesForClients/" + folderName):  
        for filename in files:

            os.remove(basedir + r"/Storage/imagesForClients/" + folderName + "/" + filename)

    listPosition = 0

    for i in range(int(len(filenames) / 4) + 1):  

        savePath = (basedir + r"/Storage/imagesForClients/" + folderName + "/" + str(i + 1) + "-")  
                      
        if (amount >= 1):

            amount -= 1
            firstNameImage = filenames[listPosition]
            listPosition += 1

            if(amount != 0 ):
                savePath += (firstNameImage + "$")
            else:
                savePath += (firstNameImage)
        else:
            break

        if (amount >= 1):

            amount -= 1
            secondNameImage = filenames[listPosition]
            listPosition += 1

            if(amount != 0 ):
                savePath += (secondNameImage + "$")
            else:
                savePath += (secondNameImage)

        else:
            secondNameImage = 'empty'

        if (amount >= 1):

            amount -= 1
            thirdNameImage = filenames[listPosition]
            listPosition += 1

            if(amount != 0 ):
                savePath += (thirdNameImage + "$")
            else:
                savePath += (thirdNameImage)

            

        else:
            thirdNameImage = 'empty'

        if (amount >= 1):

            amount -= 1
            fourthNameImage = filenames[listPosition]
            listPosition += 1

            savePath += (fourthNameImage )

        else:
            fourthNameImage = 'empty'

        if (os.path.exists(basedir + "/Storage/imagesForClients/" + folderName) != True):
            os.mkdir(basedir + "/Storage/imagesForClients/" + folderName)
        
        savePath += ".jpg"

        creatingPictures.creatingPictures(
            firstNameImage,
            secondNameImage,
            thirdNameImage,
            fourthNameImage,
            folderName,
            i + 1,
            savePath,
            basedir,
        )

        
                

        
