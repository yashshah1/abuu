import os,re,shelve
originalWords=['fuck','bitch','dick','asshole','shit']
replacedWords=['HULK','DUTCH','KICK','HEARTSOUL','SHEET']
#To find the profanity words and their places
def pfinder(text):
    newSet=[]
    diff=[]
    for i in range(len(originalWords)):
        if len(originalWords[i])!=len(replacedWords[i]):
            newSet+=[originalWords[i].lower()]
            diff+=[len(replacedWords[i])-len(originalWords[i])]
    dummy=0
    corrector=0
    foundList=[]
    while True:
        banWords = re.compile('|'.join(originalWords),re.I)
        found = banWords.search(text[dummy:])
        if found == None :
            break
        else:
            foundList+=[(found.span()[0]+dummy+corrector,found.group())]
            dummy+=found.span()[1]
            if found.group().lower() in newSet:
                for i in range(len(newSet)):
                    if found.group().lower()==newSet[i]:
                        corrector+=diff[i]
    return foundList
#To replace the profanity words
def pfilter(text):
    newText=text
    for i in range(len(originalWords)):
        rep = re.compile(originalWords[i],re.I)
        newText=rep.sub(replacedWords[i],newText)
    return newText
#Main funtion
def profanityFilter(filePath):
    for folderName,subFolders,fileNames in os.walk(filePath):
        os.chdir(folderName)
        for fileName in fileNames:            
            fileCheck = re.compile(r'.srt')
            files = fileCheck.search(str(fileName))
            if files!=None :
                masterList=[]
                fileOpen = open(fileName,'r')
                subtext = fileOpen.read()
                fileOpen.close()
                masterList+=pfinder(str(subtext))
                if masterList!=[]:
                    sh=shelve.open('log')
                    sh[fileName]=masterList
                    sh.close()
                    replacedText=pfilter(str(subtext))
                    fileWrite = open(fileName,'w')
                    fileWrite.write(replacedText)
                    fileOpen.close()
    print("Profanity Filtered")
def revertBack(filePath):
    for folderName,subFolders,fileNames in os.walk(filePath):
        os.chdir(folderName)
        try:
            sh=shelve.open('log')
            for fileName in fileNames:
                masterList=[]
                if fileName in list(sh.keys()):
                   masterList=sh[fileName]
                   fileRead=open(fileName,'r')
                   text=fileRead.read()
                   fileRead.close()
                   newtext=str(text)
                   for word in reversed(masterList):
                       for i in range(len(replacedWords)):
                           if word[1].lower()==originalWords[i].lower():
                               length=len(replacedWords[i])
                               newtext=newtext[:word[0]]+word[1]+newtext[word[0]+length:]
                   fileWrite=open(fileName,'w')
                   fileWrite.write(newtext)
                   fileRead.close()
            sh.close()
            print("Reverted Back")
        except:
            print("Log file is missing in "+str(folderName))
choice = "Yes"
while choice.lower() == 'yes':
    print("What do you want to do:")
    print("1. Profanity filtering\t2. Revert Back")
    num=int(input())
    if num == 1:
        print('Please enter the path of a directory which contains subtitles: ',end="")
        givenPath = input()
        profanityFilter(givenPath)
    elif num == 2:
        print('Please enter the path of a directory which need to be reverted: ',end="")
        givenPath = input()
        revertBack(givenPath)
    else:
        print("Invalid Choice")
    print("If you want to continue, type 'Yes'. Otherwise, type anything else:")
    choice = input()
