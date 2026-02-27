class superClass:
    def __init__(self):
        self.superAttribute = "Super's attribute"

    def superMethod(self):
        print("Super Method")

class baseClass1(superClass):
    def __init__(self):
        super()

    def baseMethod(self):
        self.superAttribute = "changed by 1"
        print("base Method 1")

class baseClass2(superClass):
    def __init__(self):
        super()

    def baseMethod(self):
        self.superAttribute = "changed by 2"
        print("base Method 2")

obj1 = baseClass1()

obj2 = baseClass2()

obj = obj1

print(obj.baseMethod())

# obj = obj2
#
# print(obj.baseMethod())
