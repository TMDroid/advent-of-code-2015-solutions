import re

with open("input") as f:
    content = f.readlines()

niceStrings = 0
for text in content:
    # Rule 1: At least 3 vowels
    vowels = "aeiou"
    numberOfVowels = 0
    for c in text:
        if c in vowels:
            numberOfVowels += 1
    rule1 = True if numberOfVowels >= 3 else False

    # Rule 2:
    matches = re.findall(r"([a-z\d])\1", text)
    rule2 = True if len(matches) >= 1 else False

    #Rule 3:
    disallowed = ['ab', 'cd', 'pq', 'xy']
    rule3 = [False for x in disallowed if x in text]
    rule3 = False if len(rule3) > 0 and rule3[0] is False else True

    if rule1 & rule2 & rule3:
        niceStrings += 1


print(niceStrings)

