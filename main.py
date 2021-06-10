# This is a sample Python script.

# Deve ser um array de arrays. Ex.:
# [
#   ['q0'],
#   ['q0', 'q1', 'q2', 'q3', 'q4'],
#   ['a', 'b', 'c'],
#   ['X', 'Y', 'a', 'b', 'c'],
#   [('q0', ['B', 'B', 'R'], 'q1')*] -> Tupa com (inicio, [lê, escreve, direção], fim)
# ]

# O meu teste é para L(m) = {a^nb^n | n > 0}
entry = [
    ['q0'],
    ['a0', 'q1', 'q2', 'q3, q4'],
    ['a', 'b', 'c'],
    ['X', 'Y', 'a', 'b', 'c'],
    [
        ('qT', ['B', 'B', 'R'], 'q0'),
        ('q0', ['Y', 'Y', 'N'], 'q4'),
        ('q0', ['a', 'X', 'R'], 'q1'),
        ('q1', ['a', 'a', 'R'], 'q1'),
        ('q1', ['b', 'b', 'R'], 'q1'),
        ('q1', ['B', 'B', 'L'], 'q2'),
        ('q1', ['Y', 'Y', 'L'], 'q2'),
        ('q2', ['b', 'Y', 'L'], 'q3'),
        ('q3', ['b', 'b', 'L'], 'q3'),
        ('q3', ['a', 'a', 'L'], 'q3'),
        ('q3', ['X', 'X', 'R'], 'q0'),
    ]
]
or_tape = []
tape = ['B', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 'b', 'B']
tape_por = 0

state = 'qT'
direction = 'L'


def move_tape():
    global tape_por

    if direction == 'L':
        tape_por -= 1
        if tape_por < 0:
            raise IndexError(f'Acabou a Fita. A entrada >{or_tape}< não pertence a L(m)')
    else:
        tape_por += 1
        if tape_por > len(tape):
            raise IndexError(f'Acabou a Fita. A entrada >{or_tape}< não pertence a L(m)')


def select_rules():
    rules = []

    for item in entry[4]:
        if item[0] == state:
            rules.append(item)

    return rules


def verify_rule(rules, e):
    global state
    global direction

    for rule in rules:
        if rule[1][0] == e:
            e = rule[1][1]
            direction = rule[1][2]
            state = rule[2]

            return e

    raise ValueError(f'Regra não encontrada. A entrada >{or_tape}< não pertence a L(m)')


def verify_end():
    if direction == 'N':
        return 0
    else:
        return 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    or_tape = tape.copy()

    while True:
        r = select_rules()

        tape[tape_por] = verify_rule(r, tape[tape_por])

        move_tape()

        if verify_end() == 0:
            break

    print(f'{or_tape} pertence a L(m)')