# -*- coding: utf-8 -*-
# core/numeric_bullets.py

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