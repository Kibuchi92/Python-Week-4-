def main():
    input_filename = input("Enter the filename to read: ")

    try:
        # Try to open and read the input file
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Example modification: convert content to uppercase
        modified_content = content.upper()

        # Define output filename
        output_filename = "modified_" + input_filename

        # Write modified content to new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Modified content written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{input_filename}' could not be read.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
