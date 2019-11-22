# Matt Landale
# Lab 9

class DecrementingCounter2(Counter):
    """Simple counter that can be incremented, decremented, and cleared.""" 
 
    def increment(self):
        """Increment counter by 2."""
        self.count += 2 
 
    def decrement(self):
        """Decrement counter by 1."""
        self.count -= 1 
 
