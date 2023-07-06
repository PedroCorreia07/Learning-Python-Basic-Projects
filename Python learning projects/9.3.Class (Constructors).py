#The constructor "__init__()" alows to set unique values for class variables when we create an instance, 
#instead of setting it in the class definition
class Pokemon:
    def __init__(self,color,name,sound): #add three parameters to the constructor| Just like with regular class methods we need to add self to the first parameter
        self.color=color #By using the self keyword to refer to these variables, we are telling Python to assign the values of color, name, and sound to these instance variables of the current object.
        self.name=name
        self.sound=sound
    def pokemon_sound(self): #create method for the pokemon sound
        print(self.sound)
charizard=Pokemon("orange","charizard","roarrrr") #create instance (3 parameters like above)
print(charizard.color) #show parameters
print(charizard.name)
charizard.pokemon_sound() #show method

