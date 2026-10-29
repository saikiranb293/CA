def to_binary(n):
    return format(n & 0xFF, '08b')


def to_signed(binary):
    value = int(binary, 2)
    if value >= 128:
        value -= 256
    return value


# QUESTION 1: Signed binary arithmetic
def question1():
    print("QUESTION 1: SIGNED BINARY ARITHMETIC")

    expressions = [(45, 19), (-35, -12)]

    for a, b in expressions:
        result = a - b

        print("\nExpression:", a, "-", "(", b, ")")
        print("First operand:", to_binary(a))
        print("Second operand:", to_binary(b))
        print("Result binary:", to_binary(result))
        print("Result decimal:", to_signed(to_binary(result)))

        if result < -128 or result > 127:
            print("Overflow: Yes")
        else:
            print("Overflow: No")


# QUESTION 2(a): Rotate left without carry
def rotate_left(binary, positions):
    print("\nQUESTION 2(a): ROL")
    print("Original:", binary)

    for i in range(positions):
        binary = binary[1:] + binary[0]
        print("After rotation", i + 1, ":", binary)

    print("Final result:", binary)


# QUESTION 2(b): Rotate left with carry
def rotate_left_carry(binary, carry, positions):
    print("\nQUESTION 2(b): RCL")
    print("Original:", binary)
    print("Initial carry:", carry)

    for i in range(positions):
        new_carry = int(binary[0])
        binary = binary[1:] + str(carry)
        carry = new_carry
        print("After rotation", i + 1, ":", binary,
              "Carry:", carry)

    print("Final result:", binary)
    print("Final carry:", carry)


question1()
rotate_left("10110110", 2)
rotate_left_carry("10110110", 0, 2)