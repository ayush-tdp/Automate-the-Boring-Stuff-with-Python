hens=2
def myFunc():
    global eggs
    eggs = 10
    print(eggs)
    print(hens)
    eggs = eggs * hens

# eggs = 20
myFunc()
print(eggs)