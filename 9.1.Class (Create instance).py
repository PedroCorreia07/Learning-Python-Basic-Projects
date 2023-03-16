class Virtual_Pet: #create class
    color="Brown" #class variable
    legs=4
    lives="9"
    wagging_tail=True
fluffy=Virtual_Pet() #creating instance
print(fluffy.color) #way to access a class variable is "instance.class_variable"
print(f"Fluffy is wagging tail? {fluffy.wagging_tail}")

