import os


def changeNameOfTheFileName():
    files = os.listdir(os.getcwd())
    print(files[0])
    for name in os.listdir(os.getcwd()):
        if len(name) == 5:
            changedName = "0" + name
            os.rename(name, changedName)

changeNameOfTheFileName()
