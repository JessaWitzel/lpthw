class Parent(object):

    def implicit(self):
        print("PARENT implicit()")

    def override(self):
        print("PARENT override()")

class Child(Parent):
    def override(self):
        print("CHILD override()")

dad = Parent()
son = Child()
#all of the functions/attributes of the parent are present in the child.
dad.implicit()
son.implicit()

#to override a parent class function just define a function with the same name in Child
dad.override()
son.override()
