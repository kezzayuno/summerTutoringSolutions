# there can be errors in  the file
#     - number would have not an integer
#     - duplicates phone number like two tims with the same number
#     - two numbers with two different people which imply that these two live together

def createDict(file):
    phoneBook = {}
    done = False
    for line in file:
        splitLine = line.rstrip().split('$')
        number = formatNumber(splitLine[1])
        if len(phoneBook) != 0:
            for name in phoneBook.keys():
                if phoneBook[name] == number:
                    saved = name
                    phoneBook.pop(name)
                    phoneBook[saved + ', ' + splitLine[0]] = number
                    break
        if done == False:
            phoneBook[splitLine[0]] = number
    return phoneBook

def formatNumber(number):
    newNumber = []
    strNumber = ''
    for tupleDigit in zip(*([iter(number)] * 3)):
        newNumber.append(''.join(tupleDigit))
    for num in newNumber:
        if num == newNumber[len(newNumber) - 1]:
            strNumber += num
        else:
            strNumber += num + '-'
    strNumber += number[len(number) - 1]
    return strNumber

def checkPhoneNumber(phoneBook, name):
    for phoneName in phoneBook.keys():
        if phoneName == name:
            return phoneBook[phoneName]
        if ',' in phoneName:
            splitNames = phoneName.split(',')
            for aName in splitNames:
                if name == aName:
                    return phoneBook[phoneName]
    return "This name does not exist in this phone book."

def main():
    with open('myContacts.txt', 'r') as f:
        readFile = f.readlines()
    phoneBook = createDict(readFile)
    getPhoneNumber = input("Whose phone number do you wish to see? >")
    print(checkPhoneNumber(phoneBook, getPhoneNumber))

main()