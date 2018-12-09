import hashlib

with open("input") as f:
    content = f.readlines()[0]

found = False


number = 1
while not found:
    phrase = content + str(number)

    crypt = hashlib.md5()
    crypt.update(phrase.encode('utf-8'))
    digest = crypt.hexdigest()

    if digest[0:5] == '00000':
        print("Found the magic key: {0}".format(phrase))
        found = True

    number += 1
