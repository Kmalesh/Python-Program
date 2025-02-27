import os

def write_to_file(filename):
    try:
        # Ensure the file has a valid path
        if not os.path.isabs(filename):
            filename = os.path.join(os.getcwd(), filename)
        
        with open(filename, 'w') as file:
            data = input("Enter data to write to the file: ")
            file.write(data)
            print("Data written successfully!")
    except PermissionError:
        print("Permission denied! Try using a different filename or directory.")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_from_file(filename):
    try:
        # Ensure the file has a valid path
        if not os.path.isabs(filename):
            filename = os.path.join(os.getcwd(), filename)
        
        with open(filename, 'r') as file:
            content = file.read()
            print("File Content:")
            print(content)
    except FileNotFoundError:
        print("File not found! Please write to the file first.")
    except PermissionError:
        print("Permission denied! Try using a different filename or directory.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    filename = input("Enter the filename (with extension): ")
    while True:
        print("\nFile Operations Menu:")
        print("1. Write to File")
        print("2. Read from File")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            write_to_file(filename)
        elif choice == '2':
            read_from_file(filename)
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()