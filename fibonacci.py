def fibonacci(n):
    nth = int(n)

    def fibon(a,b,nth,result):
        c = a + b
        result.append(c)
        if c < nth:
            fibon(,b,c,nth,result)
        return result

    return fibon(0,1,nth,[])

print(fibonacci(input("Enter nth Term to Produce Sequence:")))
