from datetime import datetime


NAME = 0
SCORE = 1
DATE = 2
FULLLIST = []
NAMELIST = []
SCORELIST = []
DATELIST = []


def main():
    text = read_file("./highscore.bat")
    preprocess(text)
    print("Sorted by name")
    sort(NAME)
    print("Sorted by score")
    sort(SCORE)
    print("Sorted by date")
    sort(DATE)


def sort(key):
    if key == NAME:
        NAMELIST.sort()
        # print the full list which each name is included
        for name in NAMELIST:
            for item in FULLLIST:
                if name in item:
                    print(item)
    elif key == SCORE:
        SCORELIST.sort()
        # print the score list which each score is included
        for score in SCORELIST:
            for item in FULLLIST:
                if str(score) in item:
                    print(item)
    elif key == DATE:
        DATELIST.sort(key=lambda date: datetime.strptime(date, "%m/%d/%Y"))
        # print the date list wich each date is included
        for date in DATELIST:
            for item in FULLLIST:
                if date in item:
                    print(item)


def read_file(path):
    return open(path).read()


def preprocess(text):
    # split the text into line by line
    for line in text.split("\n"):
        # add each line into a list called FULLLIST
        FULLLIST.append(line)
        # split the lines into words by words
        i = 0
        for word in line.split(","):
            if i == 0:
                NAMELIST.append(word.strip())
            elif i == 1:
                SCORELIST.append(int(word))
            elif i == 2:
                DATELIST.append(word.strip())
            i += 1


if __name__ == "__main__":
    main()