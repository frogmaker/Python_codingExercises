
# read file content


def readFileContent (path):
    try:
        with open(path, "r", encoding="UTF-8") as fileToRead:
            return fileToRead.read()
    except FileNotFoundError:
        return "There is no such file!"


print(readFileContent(input("File name: ")))
