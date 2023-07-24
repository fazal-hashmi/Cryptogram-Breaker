import string


def dictionaries(ciphertext, size):
    # letterMapping1
    dic1 = {
        'o': 'u', 'l': 'n', 'q': 'c', 'i': 'o', 'h': 'm', 'x': 'f', 'r': 'r', 'c': 't', 'k': 'a', 'g': 'b', 'n': 'l', 'z': ['e', 'y']
    }
    # letterMapping2
    dic2 = {
        'p': ['c', 'i', 'p', 'u'], 'l': ['o', 'n'], 'q': ['n', 'c', 'r', 'i'], 'r': ['v', 'r', 't'], 'z': 'e', 'b': ['s', 'd']
    }
    # letterMapping3
    dic3 = {
        'm': ['a', 'd'], 'p': ['d', 'i'], 'b': ['m', 's'], 'k': ['i', 'a'], 's': ['t', 'p'], 'i': ['e', 'o'], 'l': ['l', 'n'], 'c': ['y', 't']
    }
    # other two dictionries for holding letter mapping
    finaldic = {}
    finaldic1 = {}
    apla = []  # declaring the a list
    # putting values into list from letterMapping1
    for x, y in dic1.items():
        apla.append(x)
    # putting values into list from letterMapping2
    for x, y in dic2.items():
        apla.append(x)
    # putting values into list from letterMapping3
    for x, y in dic3.items():
        apla.append(x)
    apla.sort()  # sorting the list
    apla = list(dict.fromkeys(apla))  # removing duplicate values
    # simple for loop x,y,z to store values from letterMapping1,letterMapping2,letterMapping3
    j = 0
    for a in apla:
        count = 0
        x = ''
        y = ''
        z = ''
        # print(x,'y=',y,'z=',z)
        # letterMapping1
        if(a in dic1.keys()):
            x = dic1.get(a)
        # letterMapping2
        if(a in dic2.keys()):
            y = dic2.get(a)
        # letterMapping3
        if(a in dic3.keys()):
            z = dic3.get(a)
        if x != '' and y == '' and z == '':  # if letter is only present in letterMapping1
            temp = x
            if(len(temp) < 4):
                finaldic[a] = x
        elif x == '' and y != '' and z == '':  # if letter is only present in letterMapping2
            temp = x
            if(len(temp) < 4):
                finaldic[a] = y
        elif x == '' and y == '' and z != '':  # if letter is only present in letterMapping3
            temp = x
            if(len(temp) < 4):
                finaldic[a] = z
        elif x != '' and y != '' and z == '':  # if letter is present letterMapping1 and letterMapping2
            temp = x  # temperary variable
            temp1 = y  # temperary variable
            if(len(temp) >= len(temp1)):
                t = ''
                ct = 0
                for v in temp:
                    # letter is reapted more than zero times/once than put into a intermediate list
                    n = temp1.count(v)
                    if(n > ct):
                        ct = n
                        t = v
                finaldic[a] = t
            elif(len(temp) < len(temp1)):
                t = ''
                ct = 0
                for v in temp1:
                    # letter is not in the lettermapping do not assign letter or empty place
                    n = temp.count(v)
                    if(n > ct):
                        ct = n
                        t = v
                finaldic[a] = t
        elif x != '' and y == '' and z != '':  # if letter is present letterMapping1 and letterMapping3
            temp = x  # temperary variable
            temp1 = z  # temperary variable
            if(len(temp) >= len(temp1)):
                t = ''
                ct = 0
                for v in temp:
                    # if letter is occurs more than once in two lettermappings
                    n = temp1.count(v)
                    if(n > ct):
                        ct = n
                        t = v
                finaldic[a] = t
            elif(len(temp) < len(temp1)):
                t = ''
                ct = 0
                for v in temp1:
                    n = temp.count(v)
                    if(n > ct):
                        ct = n
                        t = v
                finaldic[a] = t
        elif x == '' and y != '' and z != '':  # if letter is present letterMapping2 and letterMapping3
            temp = y
            temp1 = z
            if(len(temp) >= len(temp1)):
                t = ''
                ct = 0
                for v in temp:
                    n = temp1.count(v)
                    if(n > ct):
                        ct = n
                        t = v
                finaldic[a] = t
            elif(len(temp) < len(temp1)):
                t = ''
                ct = 0
                for v in temp1:
                    n = temp.count(v)
                    if(n > ct):
                        ct = n
                        t = v
                finaldic[a] = t
        elif x != '' and y != '' and z != '':  # if letter is present letterMapping1, letterMapping2, and letterMapping3
            temp = x
            temp1 = y
            temp3 = z
            # same as above but this time we are checking letter in three lettermappings
            if(len(temp) >= len(temp1) and len(temp) >= len(temp3)):
                t = ''
                ct = 0
                for v in temp:
                    n = temp1.count(v)
                    n = n+temp3.count(v)
                    if(n > ct):
                        ct = n
                        t = v
                finaldic[a] = t
            elif(len(temp1) >= len(temp) and len(temp1) >= len(temp3)):
                t = ''
                ct = 0
                for v in temp1:
                    n = temp.count(v)
                    n = n+temp3.count(v)
                    if(n > ct):
                        ct = n
                        t = v
                finaldic[a] = t
            elif(len(temp3) >= len(temp) and len(temp3) >= len(temp1)):
                t = ''
                ct = 0
                for v in temp3:
                    n = temp.count(v)
                    n = n+temp1.count(v)
                    if(n > ct):
                        ct = n
                        t = v
                finaldic[a] = t

    tempDic = {}  # creating another list to store those letter whos mapping is not found
    print(finaldic)  # printing the intermidiate mapping we have done till know
    for d in finaldic.keys():
        if(len(finaldic.get(d))) < 2:
            finaldic1[d] = finaldic.get(d)
        else:
            tempDic[d] = finaldic.get(d)

    print(tempDic)  # print those letters whos mapping is not found
    # print(finaldic1)
    # mapping thsoe letter whos mapping is not found
    # on the base that they are already present map by another letter
    for d in tempDic.keys():
        if(len(finaldic[d])) > 1:
            temp = finaldic.get(d)
            for x in temp:
                if(finaldic1.values()):
                    finaldic1[d] = x

    print(finaldic1)  # printing out the final lettermapping

    # print('Loop ', j, ' : ', a, '  ', 'x=', x, 'Y=', y, 'Z=', z)
    #  j = j+1
    # mapping cipter text using final lettermapping and storing it into a string
    plaintext = ''
    for i in range(size):
        char = ciphertext[i]
        if char in finaldic1:
            plaintext = plaintext + finaldic1[char]
        else:  # if letter is not presnet in final lettermapping
            plaintext = plaintext + ciphertext[i]
    # priinting the plaintext
    print(plaintext)

# main function


def main():
    ciphertext = str(input('Enter the encrypted text: ')
                     )  # taking input from a user
    # converting input into lowercase because if user enter uppercase
    ciphertext = ciphertext.lower()
    size = len(ciphertext)  # calculating the size of input
    # calling the function and passing ciphere text that user entered and the size
    dictionaries(ciphertext, size)


main()  # main function call
