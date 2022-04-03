import string

def checkPassword(inputStr):
    if not len(inputStr):
        print("Empty string was entered!")
        exit(0)

    if len(inputStr) < 8 or len(inputStr) >12:
        return "Password must be between 8-12 characters"

    countupper = 0
    countletter = 0
    countlower = 0
    countDigits = 0
    countSpec = 0
    countWS = 0

    for i in inputStr:

        if i in string.ascii_lowercase or i in string.ascii_lowercase:
            countletter += 1

        if i in string.ascii_uppercase:
             countupper += 1

        if i in string.digits:
            countDigits += 1

        if i in string.punctuation:
            countSpec += 1

        if i in string.whitespace:
            countWS += 1


    if not countletter:
        return "Invalid Password!! No alphabets were found"

    if not countupper:
        return "Invalid Password!! No uppercase were found"

    if not countupper:
        return "Invalid Password!! No uppercase were found"

    elif not countDigits:
        return "Invalid Password!! No digits were found"

    elif not countSpec:
        return "Invalid Password!! No Special Character is found"

    elif countWS:
        return "Invalid Password!! No white space is allowed"
    else:
        return "Password is valid"


print(checkPassword(input("Enter Password : ")))