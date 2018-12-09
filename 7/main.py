import re

with open("input") as f:
    instructions = f.read().splitlines()

values = {}

executedInstructions = []

instructionRegex = r'(\w+\s)?(\w+) (\w+) -> (\w+)'
assignmentRegex = r'(\w+) -> (\w+)'
instructionIndex = 0

while len(instructions):
    if instructionIndex >= len(instructions):
        instructionIndex = 0
    instruction = instructions[instructionIndex]
    components = re.findall(instructionRegex, instruction)

    if len(components) == 0:
        components = re.findall(assignmentRegex, instruction)
        components = list(components[0])
        for e in components:
            if not type(e) == int:
                if e.isdigit():
                    components[components[0].index(e)] = int(e)
        components = [tuple(components)]

    for tple in components:
        if len(tple) == 2:
            one = int(tple[0]) if type(tple[0]) == str and tple[0].isdigit() else (
                tple[0] if type(tple[0]) == int else (
                    values[tple[0]] if tple[0] in values else False
                )
            )

            if type(one) == bool:
                break

            values[tple[1]] = one
            executedInstructions.append(instruction)
            instructions.remove(instruction)
            instructionIndex -= 1
        else:
            v = []

            tple = tuple(map(lambda x: x.strip(), tple))

            if not tple[0].isdigit() and tple[0]:
                v.append(tple[0])
            elif tple[0]:
                v.append(int(tple[0]))

            if not tple[2].isdigit() and tple[2]:
                v.append(tple[2])
            elif tple[2]:
                v.append(int(tple[2]))

            hasKeys = True
            for k in v:
                if not k in values and not type(k) == int:
                    hasKeys = False
                    break

            if hasKeys:
                operation = tple[1]
                v = list(map(lambda x: values[x] if x in values else x , v))

                if operation == 'LSHIFT' or operation == 'RSHIFT':
                    v.append(int(components[0][2]))

                result = (v[0] & v[1]) if operation == "AND" else (
                    (v[0] | v[1]) if operation == "OR" else (
                        (v[0] << int(v[1])) if operation == "LSHIFT" else (
                            (v[0] >> int(v[1])) if operation == "RSHIFT" else (
                                (~v[0])
                            )
                        )
                    )
                )

                values[tple[3]] = result
                executedInstructions.append(instruction)
                instructions.remove(instruction)
                instructionIndex -= 1

    print(components)

    instructionIndex += 1

print(values['a'])
