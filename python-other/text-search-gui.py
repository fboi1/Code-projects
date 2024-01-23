import os
import tkinter as tk
from tkinter import filedialog
import json

def load_previous_data():
    try:
        print(os.getcwd)
        print(os.path.isfile('C:/firaas/code/text-search-app/settings.json'))
# Use os.path.join() to create the file path
        file_path = r'C:/firaas/code/text-search-app/settings.json'




# Print out the file_path variable
        print(file_path)

# Check if the file path exists


        # Check if the file exists
        print(os.path.isfile(file_path))

        # Open and load the file
        with open(file_path) as f:    
            data = json.load(f)
            folder_path.set(data['folder'])
            search_string.set(data['search_string'])
    except FileNotFoundError:
        pass
    except json.JSONDecodeError:
        pass

def save_current_data():
    file_path = r'C:/firaas/code/text-search-app/settings.json'
    print(os.path.isfile(file_path))
    with open(file_path, 'w') as f:
        json.dump({'folder': folder_path.get(), 'search_string': search_string.get()}, f)



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
            break
        except Exception as e:
            continue

    return list_of_results

def browse_directory():
    folder_selected = filedialog.askdirectory()
    folder_path.set(folder_selected)

def execute_search():
    dir_to_search = folder_path.get()
    string_to_search = search_string.get()
    text_widget.delete(1.0, tk.END)

    for foldername, _, filenames in os.walk(dir_to_search):
        for filename in filenames:
            if filename.endswith((".txt", ".srt",".ja")):
                full_file_path = os.path.join(foldername, filename)
                matched_lines = search_string_in_file(full_file_path, string_to_search)
                for elem in matched_lines:
                    text_widget.insert(tk.END, f"Found in {elem[0]} on line {elem[1]}: {elem[2]}\n")
    save_current_data()                 

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Text Search App")

    folder_path = tk.StringVar()
    search_string = tk.StringVar()

    load_previous_data()

    browse_button = tk.Button(root, text="Browse", command=browse_directory)
    browse_button.pack()

    folder_label = tk.Label(root, text="Folder:")
    folder_label.pack()
    folder_entry = tk.Entry(root, textvariable=folder_path)
    folder_entry.pack()

    string_label = tk.Label(root, text="Search for:")
    string_label.pack()
    string_entry = tk.Entry(root, textvariable=search_string)
    string_entry.pack()

    search_button = tk.Button(root, text="Search", command=execute_search)
    search_button.pack()

    text_widget = tk.Text(root, wrap=tk.WORD)
    text_widget.pack()

    root.mainloop()
