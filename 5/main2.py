import re

class GetOutOfLoop( Exception ):
    pass

with open("input") as f:
    content = f.readlines()

niceStrings = 0
for text in content:
    # Rule 1: It contains a pair of any two letters that appears at least twice in the string without overlapping
    matches = re.findall(r"(\w{2}).*?(\1)", text)
    rule1 = True if len(list(zip(*matches))) else False
    rule2 = False

    # Rule 2: It contains at least one letter which repeats with exactly one letter between them
    try:
        rule2 = False
        for i, c in enumerate(text):
            for i2, c2 in enumerate(text):
                if c == c2 and abs(i - i2) == 2:
                    rule2 = True
                    raise GetOutOfLoop
    except GetOutOfLoop:
        pass


    if rule1 and rule2:
        niceStrings += 1


print(niceStrings)

