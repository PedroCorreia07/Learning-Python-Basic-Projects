#The constructor "__init__()" alows to set unique values for class variables when we create an instance, 
#instead of setting it in the class definition
class Pokemon:
    def __init__(self,color,name,sound): #add two parameters to the constructor
        self.color=color
        self.name=name
        self.sound=sound
    def pokemon_sound(self):
        print(self.sound)
charizard=Pokemon("orange","charizard","roarrrr")
print(charizard.color)
print(charizard.name)
charizard.pokemon_sound()

