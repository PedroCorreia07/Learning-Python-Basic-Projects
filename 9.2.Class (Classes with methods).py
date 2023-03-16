#Functions inside Classes are called "Methods"
class Pokemon:
    name="Pikachu"
    color="Yellow"
    def introduce(self): # create method:: We use "self" to make class variables (name and color) accessible inside the method
        print("Hi!")
        print("I am" + self.name)
pikachu=Pokemon() #creating instance
pikachu.introduce()
print(pikachu.color)

