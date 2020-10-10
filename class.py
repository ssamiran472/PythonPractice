class Computer:
    def specification(self):
        print("I am a computer class.")


class Laptop(Computer):
    def specification(self):
        print("I am a laptop class.")
        return 10


class Desktop(Computer):
    def specification(self):
        print("I am a desktop class.")
        return 0o1

class Desptop_and_laptop(Desktop, Laptop):
    

lap1 = Laptop()
dep1 = Desktop()

print(lap1.specification())
print(dep1.specification())
