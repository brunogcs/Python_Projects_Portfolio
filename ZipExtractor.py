import os
import zipfile
import sys

def main():
    try:
        # Ask the user to input the path to the ZIP file
        path = input("Enter the path to the ZIP file: ")

        # Check if the specified file path exists
        if os.path.exists(path) ==  False:
            print("Error: File {} does not exist".format(path))
            sys.exit(1)
        else:
            # If the file exists, attempt to extract its contents
            with zipfile.ZipFile(path) as zfile:
                zfile.extractall()
            print("The files from {} were successfully extracted".format(path))
            print("Current working directory:", os.getcwd())
    except zipfile.BadZipFile:
        # Handle the case where the specified file is not a valid ZIP file
        print("Error: The file {} is not a valid ZIP file".format(path))
        sys.exit(1)
    except Exception as e:
        # Handle unexpected errors
        print("Unexpected error:", str(e))
        sys.exit(1)

if __name__ == "__main__":
    main()