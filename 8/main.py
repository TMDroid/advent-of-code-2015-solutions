import re

with open("input") as f:
    strings = f.read().splitlines()

codeCharacterCount = inMemoryCharacterCount = escapedCharacterCount = 0


def multiple_replace(dict, text):
    # Create a regular expression  from the dictionary keys
    regex = re.compile("(%s)" % "|".join(map(re.escape, dict.keys())))

    # For each match, look-up corresponding value in dictionary
    return regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]], text)

escapeDictionary = {
    "\\": "\\\\",
    "\"": "\\\"",
}

for string in strings:
    codeCharacterCount += len(string)

    index = 0
    while index < len(string):
        c = string[index]

        if c == "\"":
            index += 1
            continue

        if c == '\\':
            cc = c + string[index + 1]

            if cc == "\\\"":
                index += 2
                inMemoryCharacterCount += 1
                continue
            elif cc == "\\\\":
                index += 2
                inMemoryCharacterCount += 1
                continue
            elif len(re.findall(r'\\x[0-9a-f]{2}', string[index: index + 4])) > 0:
                index += 4
                inMemoryCharacterCount += 1
                continue
        else:
            inMemoryCharacterCount += 1

        index += 1

    string = multiple_replace(escapeDictionary, string)
    string = "\"" + string + "\""

    escapedCharacterCount += len(string)

    print(string)


# Part 1
print((codeCharacterCount - inMemoryCharacterCount))

# Part 2
print((escapedCharacterCount - codeCharacterCount))
