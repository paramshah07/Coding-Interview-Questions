def Column_Title(n):
    s = ""
    if n == 0:
        return s
    else:
        while n > 0:
            n -= 1
            s = chr(n % 26 + 65) + s
            n //= 26
        return s

print(Column_Title(1))
print(Column_Title(28))
print(Column_Title(701))