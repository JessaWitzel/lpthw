##INHERITANCE
class Parent(object):

    def implicit(self):
        print("PARENT implicit()")

    def override(self):
        print("PARENT override()")

    def altered(self):
        print("PARENT altered()")

class Child(Parent):
    def override(self):
        print("CHILD override()")
    def altered(self):
        print("CHILD, BEFORE PARENT altered")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()
#all of the functions/attributes of the parent are present in the child.
dad.implicit()
son.implicit()

#to override a parent class function just define a function with the same name in Child
dad.override()
son.override()

#to override the parent before the parent is called
dad.altered()
son.altered()

#question for Wayne regarding how the SUPER runs because the output prints "Parent altered" then "Child Before" then "parent altered" then "Child after"


## COMPOSITION
class Other(object):

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE OTHER altered")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")

son = Child()

son.implicit()
son.override()
son.altered()
