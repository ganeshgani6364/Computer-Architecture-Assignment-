
def to_binary(n):
    return format(n & 0xFF, '08b')

def signed_value(n):
    return n if n < 128 else n - 256

def add(a, b):
    result = (a + b) & 0xFF

    print("First Operand :", to_binary(a))
    print("Second Operand:", to_binary(b))
    print("Binary Sum    :", to_binary(result))
    print("Decimal Result:", signed_value(result))

    if a + b > 127 or a + b < -128:
        print("Overflow: Yes")
    else:
        print("Overflow: No")

print("a) 120 + 62")
add(120, 62)

print("\nb) -120 + (-62)")
add(-120, -62)
