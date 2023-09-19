def mult_(x, y):
    return x * y

def div_(x, y):
    return x /y

def add_(x, y):
    return x + y

def sub_(x, y):
    return x - y

def ost_(x, y):
    return x % y

def sqrt_(x, y):
    return x**y

def calc(x, y, z):
    if z == '-':
        return sub_(x, y)
    elif z == '*':
        return mult_(x, y)
    elif z == '/':
        return div_(x, y)
    elif z == '+':
        return add_(x, y)
    elif z == '**':
        return sqrt_(x, y)
    elif z == '%':
        return ost_(x, y)
    
print(calc(4, 5, ''))