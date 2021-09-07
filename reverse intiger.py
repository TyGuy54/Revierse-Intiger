# Reverse an intiger thats both positave and negitive

def soution(x):

    string = str(x)

    if string[0] == "-":
        return int('-' + string[:0:-1])
    else:
        return int(string[::-1])

print(soution(-961))
print(soution(458))
