def fibonacci(n1):
    list = []
    a, b = 0,1
    for i in range(n1):
        list.append(a)
        a,b = b,a + b
    return list
num = int(input("digite um número do termo: "))
print(fibonacci(num))
