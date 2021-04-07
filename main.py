def dec_to_binary(n, current=""):
    if n >= 1:
        current = dec_to_binary(n//2, current)
        return current + str(n % 2)
    return ""


tab = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
def dec_to_hex(n, current=""):
    if n >= 1:
        current = dec_to_hex(n//16, current)
        result = n % 16
        if result > 9:
            result = tab[result % 10]
        return current + str(result)
    return ""


def dec_to_oct(n, current=""):
    if n >= 1:
        current = dec_to_oct(n//8, current)
        return current + str(n % 8)
    return ""


number = int(input("Type in the number: "), 0)
print("dec: ", number)
print("hex: ", dec_to_hex(number))
print("oct: ", dec_to_oct(number))
print("bin: ", dec_to_binary(number))
