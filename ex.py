def make_adder(n):
    def adder(k):
        return k+n
    return adder

def square(x):
    return x*x

def triple(x):
    return 3*x

def compose1(f,g):
    def h(x):
        return f(g(x))
    return h

compose1(square, make_adder(2))(3)

def print_sums(x):
    print(x)
    def next_sum(y):
        return print_sums(x+y)
    return next_sum
    
    
print_sums(3)(2)

def curry2(f):
    def g(x):
        def h(y):
            return f(x,y)
        return h
    return g


def cake():
    print('beets')
    def pie():
        print('sweets')
        return 'cake'
    return pie
   
chocolate = cake()
chocolate()
more_chocolate, more_cake = chocolate(), cake

def snake(x,y):
    if cake == more_cake:
        return chocolate
    else:
        return x+y

cake = 'cake'
snake(10,20)