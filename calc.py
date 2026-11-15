def add(a, b):
    if isinstance(a, str) or isinstance(b, str): raise TypeError("numbers only")
    return a + b
