# global statement

def spam():
    global eggs # <- global statement
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs) # => spam
