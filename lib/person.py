class Person:
    """
    A class representing a Person with a name attribute.
    """
    
    def __init__(self, name):
        """
        Initialize a Person instance.
        
        Args:
            name: The person's name (required)
        """
        self.name = name
    
    def talk(self):
        """
        Makes the person talk.
        Prints 'Hello World!' to the console.
        """
        print("Hello World!")
    
    def walk(self):
        """
        Makes the person walk.
        Prints 'The person is walking.' to the console.
        """
        print("The person is walking.")