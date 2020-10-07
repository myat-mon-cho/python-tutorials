from datetime import datetime


NAME = 0
SCORE = 1
DATE = 2
MAPPING = {}
NAMELIST = []
SCORELIST = []
DATELIST = []


def main():
    # read text from highscore.bat
    text = open("highscore.bat").read()
    # preprocess the data
    pre_process(text)
    # sort and print
    print("Sorted by Name")
    sort(NAME)
    print("Sorted by Score")
    sort(SCORE)
    print("Sorted by Date")
    sort(DATE)


def sort(key):
    # if it needs to sort by name
    if key == NAME:
        # names are sorted
        NAMELIST.sort()
        # and print the whole data (name, score, date) which is concerned with the name
        for name in NAMELIST:
            print(MAPPING[name])
    elif key == SCORE:
        # scores are sorted
        SCORELIST.sort()
        # and print the whole data (name, score, date) which is concerned with the score
        for score in SCORELIST:
            # here as score is number, it needs type cast to string
            print(MAPPING[str(score)])
    elif key == DATE:
        # dates are sorted using date sorting method
        # here the date is in format (mm/dd/yyyy)
        DATELIST.sort(key=lambda date: datetime.strptime(date, "%m/%d/%Y"))
        # and print the whole data (name, score, date) which is concerned with the date
        for date in DATELIST:
            print(MAPPING[date])
    


def pre_process(text):
    i = 0
    # split the text into words by words
    # for each line of the text
    for txt in text.split():
        # if it is the first column then it is name
        if i % 3 == 0:
            # add name => name, score, date to dictionary
            name = txt.replace(",", "")
            MAPPING[name] = text.split("\n")[i // 3]
            # add name to namelist for the purpose of sorting
            NAMELIST.append(name)
        # if it is the second column then it is score
        elif (i-1) % 3 == 0:
            # add score => name, score, date to dictionary
            score = txt.replace(",", "")
            MAPPING[score] = text.split("\n")[(i-1) // 3]
            # add score to scorelist for the purpose of sorting
            # as scores are numbers, it needs type cast to int
            SCORELIST.append(int(score))
        # if it is the third column then it is date
        elif (i-2) % 3 == 0:
            # add date => name, score, date to dictionary
            date = txt.replace(",", "")
            MAPPING[date] = text.split("\n")[(i-2) // 3]
            # add date to datelist for the purpose of sorting
            DATELIST.append(date)
        i += 1


if __name__ == "__main__":
    main()