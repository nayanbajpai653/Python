def fectorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fectorial(n - 1)
    
print(fectorial(4))
print(fectorial(0))
print(fectorial(1))

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(9))
print(fibonacci(0) , fibonacci(1))