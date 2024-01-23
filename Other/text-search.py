import os

def search_string_in_file(file_name, string_to_search):
    line_number = 0
    list_of_results = []
    encodings = ['utf-8', 'shift_jis', 'euc_jp', 'iso2022_jp']

    for encoding in encodings:
        try:
            with open(file_name, 'r', encoding=encoding) as read_obj:
                for line in read_obj:
                    line_number += 1
                    if string_to_search in line:
                        list_of_results.append((file_name, line_number, line.rstrip()))
            break  # If the file was read successfully, break out of the loop
        except UnicodeDecodeError:
            print(f"Failed decoding {file_name} using {encoding}")
        except Exception as e:
            print(f"An error occurred: {e}")
            break

    return list_of_results


#C:\\firaas\\code\\Obfuscate
#C:\\firaas\\anime\\subs
def main():
    # Ask user for the string to search
    string_to_search = input("Enter the string to search: ")
    
    # Define the directory where to search
    dir_to_search = "C:\\firaas\\anime\\subs"  # Replace with your directory path

    # Iterate through each file in the directory
# Iterate through each file in the directory
    for foldername, subfolders, filenames in os.walk(dir_to_search):
        for filename in filenames:
            if filename.endswith((".txt", ".srt")):  # Search .txt and .srt files
                full_file_path = os.path.join(foldername, filename)
                matched_lines = search_string_in_file(full_file_path, string_to_search)
                for elem in matched_lines:
                    print(f"Found in {elem[0]} on line {elem[1]}: {elem[2]}")


if __name__ == '__main__':
    main()
