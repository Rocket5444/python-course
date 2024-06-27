import os

def list_directory_contents(path):
    try:
        # Get the list of all files and directories in the specified path
        contents = os.listdir(path)
        print(f"Contents of the directory '{path}':")
        
        # Print each item in the directory
        for item in contents:
            print(item)
    
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the directory path
directory_path = "/"

# Call the function to list directory contents
list_directory_contents(directory_path)
