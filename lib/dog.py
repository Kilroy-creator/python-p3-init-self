class Dog:
    """
    A class representing a Dog with name and breed attributes.
    """
    
    def __init__(self, name, breed="Mutt"):
        """
        Initialize a Dog instance.
        
        Args:
            name: The dog's name (required)
            breed: The dog's breed (optional, defaults to "Mutt")
        """
        self.name = name
        self.breed = breed
    
    def bark(self):
        """
        Makes the dog bark.
        Prints 'Woof!' to the console.
        """
        print("Woof!")
    
    def sit(self):
        """
        Makes the dog sit.
        Prints 'The dog is sitting.' to the console.
        """
        print("The dog is sitting.")