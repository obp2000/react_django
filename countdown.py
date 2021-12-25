def countdown(n):
    if n <= 0:
        print('Готово!')
    else:
        print(n)
        countdown(n)

def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)

def print_spam():
    print('spam')

def do_n(f, p='тест1', n=5):
    for i in range(n):
        f(p)
    
def accept(a):
    print('Херня эта ваша', a) 
