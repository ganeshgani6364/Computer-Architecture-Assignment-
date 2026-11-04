
def left_shift(binary, n):
    print("Original Number:", binary)

    for i in range(n):
        binary = binary[1:] + '0'
        print("Step", i + 1, ":", binary)

    print("Final Result:", binary)

def right_shift(binary, n):
    print("Original Number:", binary)

    for i in range(n):
        binary = '0' + binary[:-1]
        print("Step", i + 1, ":", binary)

    print("Final Result:", binary)

print("a) Logical Left Shift")
left_shift("10110110", 3)

print("\nb) Logical Right Shift")
right_shift("11010100", 3)
