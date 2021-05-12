def reverseString(string):
    newString = ''
    oldString = string
    for i in range(len(string)):
        newString = oldString[0] + newString
        oldString = oldString[1:]
    return newString

def removeNonsense(string, nonsense):
    newString = ''
    oldString = string
    for i in nonsense:
        for n in string:
            if i == n:
                newString = oldString.replace(n, '')
                oldString = newString
    return newString

def main():
    encryptedMessage = 'T%u$No@c\O*C S^7eV@OL nA@T7$U#GN&7a&&7Ro'
    nonsense = '%$@\*^7#&'
    print("The encrypted message: {}".format(encryptedMessage))
    reversed = reverseString(encryptedMessage)
    removedRandom = removeNonsense(reversed, nonsense).capitalize()
    print("The decrypted message: {}".format(removedRandom))

main()