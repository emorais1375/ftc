import re


def checkLogin(string, index, brokeChain=False):
    loginRegex = re.compile(r'[a-z]+[a-zA-Z]*')

    if loginRegex.match(string[index]) is not None:
        if brokeChain is True:
            return True
        return checkCpf(string, index + 1)
    return False


def checkCpf(string, index):
    if checkPattern(string[index]) is True:
        if checkValidity(string[index]):
            return checkEmail(string, index + 1)
    return False


def checkPattern(string):
    cpfRegex = re.compile(r'[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}')

    return cpfRegex.fullmatch(string) is not None


def checkValidity(string):
    digits = getDigits(string)
    firstDigit = getFirstVerifyDigit(digits)
    proposition1 = string[-2] == str(firstDigit)

    if proposition1 is True:
        secondDigit = getSecondVerifyDigit(digits)
        proposition2 = string[-1] == str(secondDigit)

        return proposition2

    return False


def getDigits(string):
    newString = ''
    for e in string.split('.'):
        if '-' in e:
            string1, string2 = e.split('-')
            newString += string1 + string2
        else:
            newString += e
    digits = [int(e) for e in newString]
    return digits


def getFirstVerifyDigit(digits):
    newDigits = [(10 - i) * v for i, v in enumerate(digits[:-2])]
    sumDigits = sum(newDigits)

    rest = sumDigits % 11
    if rest < 2:
        return 0
    else:
        return 11 - rest


def getSecondVerifyDigit(digits):
    newDigits = digits[:-2]
    newDigits.append(getFirstVerifyDigit(digits))

    newDigits = [(11 - i) * v for i, v in enumerate(newDigits)]
    sumDigits = sum(newDigits)

    rest = sumDigits % 11
    if rest < 2:
        return 0
    else:
        return 11 - rest


def checkEmail(string, index, brokeChain=False):
    emailRegex = re.compile(r'[a-z][^@]*@[^@]*\.+[^@]*')

    if emailRegex.match(string[index]) is not None:
        if brokeChain is True:
            return True
        return checkSenha(string, index + 1)
    return False


def checkSenha(string, index):
    senhaRegex = re.compile(
        r'(\d[A-F]|[A-F]\d|(\d)(?!\2)\d)'
        r'\.((\d[A-F]|[A-F]\d|(\d)(?!\5)\d))'
        r'\.((\d[A-F]|[A-F]\d|(\d)(?!\8)\d))'
        r'\.((\d[A-F]|[A-F]\d|(\d)(?!\11)\d))')

    if senhaRegex.match(string[index]) is not None:
        return checkNomeApp(string, index + 1)
    return False


def checkNomeApp(string, index):
    senhaRegex = re.compile(r'[a-zA-Z]{2,}')

    if senhaRegex.match(string[index]) is not None:
        return checkVersaoApp(string, index + 1)
    return False


def checkVersaoApp(string, index):
    senhaRegex = re.compile(r'([0-9]+)\.([0-9]+)')
    result = senhaRegex.search(string[index])

    if result is not None:
        numA = int(result.group(1))
        numB = int(result.group(2))
        if numB > numA:
            return False
        return checkPlataforma(string, index + 1)

    return False


def checkPlataforma(string, index):
    senhaRegex = re.compile(r'\bwindows\b'
                            r'|\bmac\b'
                            r'|\blinux\b'
                            r'|\bios\b'
                            r'|\bandroid\b'
                            r'|\bwindowsPhone\b')
    result = senhaRegex.match(string[index])

    return result is not None


if __name__ == '__main__':

    empty_word = True
    while True:

        try:
            string = re.split(r'\s+', string = input(''))
            empty_word = False
            if len(string) >= 7:
                result = checkLogin(string, 0)
                if result is True:
                    for index in range(7, len(string)):
                        if not (checkLogin(string, index, True) or checkEmail(string, index, True)):
                            result = False
                            break

                print(result)

            else:
                print(False)
        except:
            if empty_word is True:
                print(False)
            break
