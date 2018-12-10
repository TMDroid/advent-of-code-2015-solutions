with open("input") as f:
    input = f.readlines()[0]

times = 40
output = ""
for index in range(times):
    same = ""
    output = ""

    i = 0
    while i < len(input):
        digit = input[i]

        if same == "" or digit in same:
            same += digit

            if i == len(input) - 1:
                output += str(len(same)) + same[0]
                same = ""
                break

            i += 1
        else:
            output += str(len(same)) + same[0]
            same = ''

    input = output

print(output)
print(len(output))
