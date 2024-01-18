def climbstairs(n):
    if n == 0 or n == 1:
        return 1
    else:
        return climbstairs(n-1) + climbstairs(n-2)
print(climbstairs(3))
print(climbstairs(4))
print(climbstairs(5))