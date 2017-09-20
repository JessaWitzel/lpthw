##Animal is-a object
class Animal(object):
    pass

#Dog is-a Animal
class Dog(Animal):
    #class Dog has-a __init__ function that takes self and name
    def __init__(self, name):
        #Associates paramater name with this instance of Dog
        self.name = name

#Cat is-a Animal
class Cat(Animal):
    #class Cat has-a __init__ function that takes self and name
    def __init__(self, name):
        #associates parameter name with instance of Cat
        self.name = name

#Person is-a object
class Person(object):
    #class Person has-a __init__ funciton that takes self and name
    def __init__(self, name):
        #Person has-a name
        self.name = name

        ##Person has-a pet of some kind
        self.pet = None

#Employee is-a Person
class Employee(Person):
    #class Employee has-a __init__ function that takes self, name, salary
    def __init__(self, name, salary):
        #dunno yet
        super(Employee, self).__init__(name)
        #Employee has-a salary
        self.salary = salary

#Fish is-a object
class Fish(object):
    pass

#Salmon is-a Fish
class Salmon(Fish):
    pass

#Halibut is-a Fish
class Halibut(Fish):
    pass

##rover is-a Dog
rover = Dog("Rover")

#satan is-a Cat
satan = Cat("Satan")

#mary is-a Person
mary = Person("Mary")

#mary's pet is satan
mary.pet = satan

#frank is-a employee with name Frank and salary 120000
frank = Employee("Frank", 120000)

#frank has-a pet rover
frank.pet = rover

#flipper is-a Fish
flipper = Fish()

#crouse is-a Salmon
crouse = Salmon()

#harry is-a Halibut
harry = Halibut()
