import time

def usingWhile():
    i = 0
    while i < 10000:
        i +=1
        print(i)

def usingFor():
    for i in range(1000):
        print(i)

# init = time.time()
# usingFor()
# print(time.time()-init)

# init = time.time()
# usingWhile()
# print(time.time()-init)


# t = time.localtime()
# print(t) ##BAD OUTPUT

print(time.strftime("%Y-%m-%d-%H"))
print(time.strftime("%D"))
print(time.strftime("%X %Z",))