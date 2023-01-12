
# read file content


def readFileContent (path):
    try:
        with open(path, "r", encoding="UTF-8") as fileToRead:
            return fileToRead.read()
    except FileNotFoundError:
        return "There is no such file!"


print(readFileContent("oceany.txt"))


# LXXXII - Image size

from PIL import Image

def showImageSize(path):
    try:
        file = Image.open(path)
        return file.size
    except FileNotFoundError:
        return "There is no such file!"


print("Image size: ", showImageSize("image.png"))
print("Szerokość obrazka:", showImageSize("image.png")[0])
print("Wysokość obrazka:", showImageSize("image.png")[1])


# LXXXII - ilość wystąkień słowa kot w pliku

word  = "kot"
def catCounter(path):
    try:
        with open(path, "r", encoding="UTF-8") as file:
            return file.read().lower().count(word)
    except FileNotFoundError:
        return "There is no such file!"
    except PermissionError:
        return "Permission denied"


file = "oceany.txt"
print(f"Słowo '{word}' wystąpiło {catCounter(file) } razy w pliku '{file}'.")
