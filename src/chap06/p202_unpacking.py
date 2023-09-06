# 언패킹(unpacking)
 
# 1
alist = [1, 2, 3]
print(*alist)
print(alist)

# 2
def sum(a, b, c) :
    print(a + b + c)

alist = [1, 2, 3]
sum(*alist)
sum(alist)    # Error