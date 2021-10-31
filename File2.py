Ball = open("Text1.txt")
f = Ball.read()
print(f)
Filelines = Ball.readlines()
for i in Filelines:
    print(i)
intro = "My Name Is Madhav"
words = intro.split()
print(words)
intro = "My Name Is, Madhav"
words = intro.split(",")
print(words)
def countingWords():
    fileName = input("Enter The File Name")
    file = open(fileName,"r")
    numberOfWords = 0
    for i in file :
        words = i.split()
        numberOfWords = numberOfWords + len(words)
    print(numberOfWords)
countingWords()
