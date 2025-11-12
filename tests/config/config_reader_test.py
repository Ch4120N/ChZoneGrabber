import configparser
import os

def read_cfg(file_path):
    """Read and parse a CFG/INI file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Configuration file '{file_path}' not found.")

    config = configparser.ConfigParser()
    config.read(file_path)

    # Print the sections to debug if the file is read correctly
    print(f"Sections in the config file: {config.sections()}")

    # Example: Access values
    try:
        db_host = config.get("database", "host", fallback="127.0.0.1")
        db_port = config.getint("database", "port", fallback=3306)
        debug_mode = config.getboolean("app", "debug", fallback=False)
    except Exception as e:
        print(f"Error accessing config values: {e}")
        raise

    return {
        "db_host": db_host,
        "db_port": db_port,
        "debug_mode": debug_mode
    }

def write_cfg(file_path):
    """Create or update a CFG/INI file."""
    config = configparser.ConfigParser()

    # Add sections and keys
    config["database"] = {
        "host": "localhost",
        "port": "5432",
        "user": "admin",
        "password": "secret"
    }
    config["app"] = {
        "debug": "True",  # Ensure this is "True" or "False"
        "log_file": "app.log"
    }

    # Save to file
    with open(file_path, "w") as config_file:
        config.write(config_file)

if __name__ == "__main__":
    cfg_file = "config.cfg"

    # Create a sample config file if it doesn't exist
    if not os.path.exists(cfg_file):
        write_cfg(cfg_file)
        print(f"Created default config file: {cfg_file}")

    # Read and display config values
    try:
        settings = read_cfg(cfg_file)
        print("Configuration Loaded:", settings)
    except Exception as e:
        print("Error reading config:", e)
