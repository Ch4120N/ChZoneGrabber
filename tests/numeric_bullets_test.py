from colorama import Fore, init

init()

class NumericBulletGenerator:
    """
    A class for generating formatted numeric bullets with color customization options.
    """
    
    # ANSI color codes
    COLORS = {
        'black': Fore.BLACK,
        'red': Fore.RED,
        'green': Fore.GREEN,
        'yellow': Fore.YELLOW,
        'blue': Fore.BLUE,
        'magenta': Fore.MAGENTA,
        'cyan': Fore.CYAN,
        'white': Fore.WHITE,
        'bright_black': Fore.LIGHTBLACK_EX,
        'bright_red': Fore.LIGHTRED_EX,
        'bright_green': Fore.LIGHTGREEN_EX,
        'bright_yellow': Fore.LIGHTYELLOW_EX,
        'bright_blue': Fore.LIGHTBLUE_EX,
        'bright_magenta': Fore.LIGHTMAGENTA_EX,
        'bright_cyan': Fore.LIGHTCYAN_EX,
        'bright_white': Fore.LIGHTWHITE_EX,
        'reset': Fore.RESET
    }
    
    def __init__(self, start=1, padding=2, prefix="[ ", suffix=" ]", auto_increment=True,
                 brackets_color=None, numbers_color=None):
        """
        Initialize the bullet generator with color options.
        
        Args:
            start (int): Starting number for bullets
            padding (int): Number of digits to pad with zeros
            prefix (str): Text before the number
            suffix (str): Text after the number
            auto_increment (bool): Whether to automatically increment numbers
            brackets_color (str): Color for brackets/prefix-suffix (from COLORS keys)
            numbers_color (str): Color for numbers (from COLORS keys)
        """
        self.current = start
        self.padding = padding
        self.prefix = prefix
        self.suffix = suffix
        self.auto_increment = auto_increment
        self.brackets_color = brackets_color
        self.numbers_color = numbers_color
    
    def _apply_color(self, text, color_name):
        """
        Apply ANSI color to text if color is specified.
        
        Args:
            text (str): Text to colorize
            color_name (str): Color name from COLORS dict
        
        Returns:
            str: Colorized text or original text if no color
        """
        if color_name and color_name in self.COLORS:
            return f"{self.COLORS[color_name]}{text}{self.COLORS['reset']}"
        return text
    
    def generate(self, text, number=None, brackets_color=None, numbers_color=None):
        """
        Generate a bullet point with optional color overrides.
        
        Args:
            text (str): The text content for the bullet
            number (int, optional): Specific number to use. If None, uses current number.
            brackets_color (str, optional): Override for brackets color
            numbers_color (str, optional): Override for numbers color
        
        Returns:
            str: Formatted bullet string with colors
        """
        if number is None:
            number = self.current
            if self.auto_increment:
                self.current += 1
        
        # Use instance colors if overrides not provided
        brackets_color = brackets_color or self.brackets_color
        numbers_color = numbers_color or self.numbers_color
        
        formatted_number = str(number).zfill(self.padding)
        
        # Apply colors
        colored_prefix = self._apply_color(self.prefix, brackets_color)
        colored_suffix = self._apply_color(self.suffix, brackets_color)
        colored_number = self._apply_color(formatted_number, numbers_color)
        
        bullet = f"{colored_prefix}{colored_number}{colored_suffix} {text}"
        return bullet
    
    def generate_list(self, items, start_number=None, brackets_color=None, numbers_color=None):
        """
        Generate a list of bullet points with colors.
        
        Args:
            items (list): List of text items
            start_number (int, optional): Starting number for the list
            brackets_color (str, optional): Override for brackets color
            numbers_color (str, optional): Override for numbers color
        
        Returns:
            list: List of formatted bullet strings
        """
        if start_number is not None:
            self.current = start_number
        
        bullets = []
        for item in items:
            bullets.append(self.generate(item, brackets_color=brackets_color, numbers_color=numbers_color))
        
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
    
    def set_colors(self, brackets_color=None, numbers_color=None):
        """
        Update color settings.
        
        Args:
            brackets_color (str, optional): New brackets color
            numbers_color (str, optional): New numbers color
        """
        if brackets_color is not None:
            self.brackets_color = brackets_color
        if numbers_color is not None:
            self.numbers_color = numbers_color
    
    def get_available_colors(self):
        """
        Get list of available color names.
        
        Returns:
            list: Available color names
        """
        return list(self.COLORS.keys())
    
    def get_current_number(self):
        """
        Get the current number without incrementing.
        
        Returns:
            int: Current number
        """
        return self.current
    
    def generate_plain(self, text, number=None):
        """
        Generate a bullet without any colors (useful for file output).
        
        Args:
            text (str): The text content
            number (int, optional): Specific number to use
        
        Returns:
            str: Plain formatted bullet string
        """
        if number is None:
            number = self.current
            if self.auto_increment:
                self.current += 1
        
        formatted_number = str(number).zfill(self.padding)
        bullet = f"{self.prefix}{formatted_number}{self.suffix} {text}"
        return bullet

# Example usage and demonstration
def main():
    # Basic usage with colors
    print("=== Basic Usage with Colors ===")
    bullet_gen = NumericBulletGenerator(
        brackets_color='bright_blue',
        numbers_color='bright_yellow'
    )
    print(bullet_gen.generate("First colored item"))
    print(bullet_gen.generate("Second colored item"))
    
    # Different color combinations
    print("\n=== Different Color Combinations ===")
    color_combinations = [
        {'brackets_color': 'red', 'numbers_color': 'white'},
        {'brackets_color': 'green', 'numbers_color': 'bright_white'},
        {'brackets_color': 'magenta', 'numbers_color': 'cyan'},
        {'brackets_color': 'bright_red', 'numbers_color': 'bright_green'},
    ]
    
    for i, colors in enumerate(color_combinations, 1):
        gen = NumericBulletGenerator(**colors)
        print(gen.generate(f"Color combo {i}"))
    
    # Override colors per generation
    print("\n=== Per-item Color Overrides ===")
    flexible_gen = NumericBulletGenerator(
        brackets_color='blue',
        numbers_color='white'
    )
    print(flexible_gen.generate("Default colors"))
    print(flexible_gen.generate("Red brackets", brackets_color='red'))
    print(flexible_gen.generate("Green numbers", numbers_color='green'))
    print(flexible_gen.generate("Both overridden", brackets_color='magenta', numbers_color='cyan'))
    
    # List generation with colors
    print("\n=== Colored List Generation ===")
    items = ["Apple", "Banana", "Cherry", "Date"]
    list_gen = NumericBulletGenerator(
        start=1,
        brackets_color='bright_cyan',
        numbers_color='bright_magenta'
    )
    bullet_list = list_gen.generate_list(items)
    for bullet in bullet_list:
        print(bullet)
    
    # Plain generation (no colors)
    print("\n=== Plain Generation (No Colors) ===")
    plain_gen = NumericBulletGenerator()  # No colors specified
    print(plain_gen.generate("Plain item 1"))
    print(plain_gen.generate("Plain item 2"))
    
    # Explicit plain generation
    print(plain_gen.generate_plain("Explicitly plain item"))
    
    # Available colors
    print("\n=== Available Colors ===")
    demo_gen = NumericBulletGenerator()
    colors = demo_gen.get_available_colors()
    print(f"Available colors: {', '.join(colors[:8])}...")

# Functional approach with color support
def create_bullet_generator(**kwargs):
    """Factory function to create a bullet generator with custom settings."""
    return NumericBulletGenerator(**kwargs)

def generate_bullets(items, start=1, padding=2, prefix="[ ", suffix=" ]", 
                    brackets_color=None, numbers_color=None):
    """
    One-time function to generate bullets with colors without creating a class instance.
    
    Args:
        items (list): List of text items
        start (int): Starting number
        padding (int): Number padding
        prefix (str): Prefix text
        suffix (str): Suffix text
        brackets_color (str): Color for brackets
        numbers_color (str): Color for numbers
    
    Returns:
        list: List of formatted bullet strings
    """
    generator = NumericBulletGenerator(
        start=start, 
        padding=padding, 
        prefix=prefix, 
        suffix=suffix,
        brackets_color=brackets_color,
        numbers_color=numbers_color
    )
    return generator.generate_list(items)

if __name__ == "__main__":
    main()
    
    # Example of functional approach with colors
    print("\n=== Functional Approach with Colors ===")
    items = ["Quick", "Bullet", "List"]
    bullets = generate_bullets(
        items, 
        start=5, 
        padding=3,
        brackets_color='bright_green',
        numbers_color='bright_white'
    )
    for bullet in bullets:
        print(bullet)