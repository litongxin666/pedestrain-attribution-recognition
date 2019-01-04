class A(object):
    def __getitem__(self, item):
        return item

a = A()
print(a[0], a[12])