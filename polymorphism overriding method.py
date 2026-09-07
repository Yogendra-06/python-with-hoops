class Dog:
    def speak(self):
        print("Dog bark")
    def eat(self):
        print("Dog eat")
class Cat(Dog):
    def speak(self):
        print("cat bark")
c=Cat()
c.eat()
c.speak()