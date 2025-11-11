class NumericBulletGenerator:
    """
    A class for generating formatted numeric bullets with various customization options.
    """
    
    def __init__(self, start=1, padding=2, prefix="[ ", suffix=" ]", auto_increment=True):
        """
        Initialize the bullet generator.
        
        Args:
            start (int): Starting number for bullets
            padding (int): Number of digits to pad with zeros
            prefix (str): Text before the number
            suffix (str): Text after the number
            auto_increment (bool): Whether to automatically increment numbers
        """
        self.current = start
        self.padding = padding
        self.prefix = prefix
        self.suffix = suffix
        self.auto_increment = auto_increment
    
    def generate(self, text, number=None):
        """
        Generate a bullet point.
        
        Args:
            text (str): The text content for the bullet
            number (int, optional): Specific number to use. If None, uses current number.
        
        Returns:
            str: Formatted bullet string
        """
        if number is None:
            number = self.current
            if self.auto_increment:
                self.current += 1
        
        formatted_number = str(number).zfill(self.padding)
        bullet = f"{self.prefix}{formatted_number}{self.suffix} {text}"
        return bullet
    
    def generate_list(self, items, start_number=None):
        """
        Generate a list of bullet points.
        
        Args:
            items (list): List of text items
            start_number (int, optional): Starting number for the list
        
        Returns:
            list: List of formatted bullet strings
        """
        if start_number is not None:
            self.current = start_number
        
        bullets = []
        for item in items:
            bullets.append(self.generate(item))
        
        return bullets
    
    def reset(self, start=1):
        """
        Reset the counter to a specific number.
        
        Args:
            start (int): Number to reset to
        """
        self.current = start
    
    def set_format(self, padding=None, prefix=None, suffix=None):
        """
        Update the formatting options.
        
        Args:
            padding (int, optional): New padding value
            prefix (str, optional): New prefix
            suffix (str, optional): New suffix
        """
        if padding is not None:
            self.padding = padding
        if prefix is not None:
            self.prefix = prefix
        if suffix is not None:
            self.suffix = suffix
    
    def get_current_number(self):
        """
        Get the current number without incrementing.
        
        Returns:
            int: Current number
        """
        return self.current

# Example usage and demonstration
def main():
    # Basic usage
    print("=== Basic Usage ===")
    bullet_gen = NumericBulletGenerator()
    print(bullet_gen.generate("First item"))
    print(bullet_gen.generate("Second item"))
    print(bullet_gen.generate("Third item"))
    
    # Custom formatting
    print("\n=== Custom Formatting ===")
    custom_gen = NumericBulletGenerator(
        start=1,
        padding=3,
        prefix="< ",
        suffix=" >"
    )
    print(custom_gen.generate("Custom formatted"))
    print(custom_gen.generate("Another item"))
    
    # Generate list
    print("\n=== List Generation ===")
    items = ["Apple", "Banana", "Cherry", "Date"]
    list_gen = NumericBulletGenerator(start=10, padding=2)
    bullet_list = list_gen.generate_list(items)
    for bullet in bullet_list:
        print(bullet)
    
    # Manual number control
    print("\n=== Manual Number Control ===")
    manual_gen = NumericBulletGenerator(auto_increment=False)
    print(manual_gen.generate("Fixed number 5", 5))
    print(manual_gen.generate("Same number 5", 5))
    print(manual_gen.generate("Different number", 10))
    
    # Reset functionality
    print("\n=== Reset Functionality ===")
    reset_gen = NumericBulletGenerator(start=100)
    print(reset_gen.generate("Item 100"))
    print(reset_gen.generate("Item 101"))
    reset_gen.reset(start=1)
    print(reset_gen.generate("Back to 1"))
    
    # Different padding examples
    print("\n=== Different Padding ===")
    for padding in [1, 2, 3, 4]:
        pad_gen = NumericBulletGenerator(padding=padding, prefix="[", suffix="]")
        print(pad_gen.generate(f"Padding {padding}"))

# Alternative: Functional approach
def create_bullet_generator(**kwargs):
    """Factory function to create a bullet generator with custom settings."""
    return NumericBulletGenerator(**kwargs)

def generate_bullets(items, start=1, padding=2, prefix="[ ", suffix=" ]"):
    """
    One-time function to generate bullets without creating a class instance.
    
    Args:
        items (list): List of text items
        start (int): Starting number
        padding (int): Number padding
        prefix (str): Prefix text
        suffix (str): Suffix text
    
    Returns:
        list: List of formatted bullet strings
    """
    generator = NumericBulletGenerator(start=start, padding=padding, prefix=prefix, suffix=suffix)
    return generator.generate_list(items)

if __name__ == "__main__":
    main()
    
    # Example of functional approach
    print("\n=== Functional Approach ===")
    items = ["Quick", "Bullet", "List"]
    bullets = generate_bullets(items, start=5, padding=3)
    for bullet in bullets:
        print(bullet)