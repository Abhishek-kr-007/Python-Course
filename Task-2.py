# List Operations: Extracting and Reversing Elements

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    extracted_list = numbers[:5]  # Extracts the first 5 elements
    reversed_list = extracted_list[::-1]  # Reverses the extracted list

    print("Original list:",numbers)
    print("Extracted list:", extracted_list)
    print("Reversed list:", reversed_list)

# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()