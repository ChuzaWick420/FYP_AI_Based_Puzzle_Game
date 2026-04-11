class Obj:
    value = 69

obj_1 = Obj

def foo(object):
    temp = object

    temp.value = 420

foo(obj_1)

print(obj_1.value)
