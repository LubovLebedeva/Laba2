def Func (value, power):
    x = 1
    eps = 0.001

    while 1:
        print(x)
        newx = 1/power*((power-1)*x+value/(x**(power-1)))
        if(abs(newx-x) < eps):
            break
        x = newx
    return x

print(Func(2, 2))
