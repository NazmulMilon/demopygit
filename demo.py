class A:
    def sum(a, b, c):
        add = a + b + c
        # return add

    def sub(self, m, n):
        diff = m-n
        return diff


m1, m2 = map(int, input("Enter numbr: ").split())
obj = A()
x = obj.sub(m1, m2)

print(x)


'''
def sum(a,b,c):
    add = a+b+c
    return add


x, y, z = map(int, input("Enter number: ").split())
r = sum(x, y, z)
print(r)
'''