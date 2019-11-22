# Matt Landale
# Lab 9

class DecrementingCounter:
    """Simple counter that can be incremented, decremented, and cleared.""" 
 
    def __init__(self):
        """Initialize counter to 0."""
        self.count = 0 
 
    def increment(self):
        """Increment counter by 1."""
        self.count += 1 
 
    def decrement(self):
        """Decrement counter by 1."""
        self.count -= 1
        
    def clear(self):
        """Clear counter to 0."""
        self.count = 0 
 
    def get_value(self):
        """Return the current value of the counter."""
        return self.count 
 
