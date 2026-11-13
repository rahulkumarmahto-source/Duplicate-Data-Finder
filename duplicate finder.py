import os
import sys

def normalize_text(text,ignore_case_and_spaces):
    if ignore_case_and_spaces:
        return " ".Join(text.strip().split()).lower()  
    return text.strip("\r\n") 
def process_duplicate_data():
    file_name = input("Enter the input file name (default 'data.text'): ").strip()
    if not file_name:
        file_name = "data.text"

        try:
            with open(file_name, "r", encoding="utf-8") as file:
                lines = file.readlines()
        except Exception as e:
            print(f"Error reading file: {e}")
            return
        if not lines or all(line.strip() == "" for line in lines):
            print("File is empty. Nothing to check.")
            return
        print("\nselection Matching Mode:")
        print("1. Exact match")
        print("2. Ignore case and extra spaces")
        choice = input("Enter option (1 or 2):").strip()

        ignore_mode = choice == "2"
        totaL_item = 0
        raw_entries = []
        processed_entries = []

        for line in lines:
            cleaned_line = line.strip("\r\n") 
            if cleaned_line: 
                total_items += 1
                raw_entries.append(cleaned_line)
                processed_entries.append(normalize_text(cleaned_line, ignore_mode))
        if total_items == 0:
            print("file is empty. Nothing to check.")
            return
        unique_keys = []
        seen = set()
        for entry in processed_entries:
            if entry not in seen:
                unique_keys.append(entry)
        counts = {} 
        for entry in processed_entries:
            counts[entry] = counts.get(entry,0) + 1

        duplicates = {k: v for k,v in counts.items() if v >1}  
        unique_count = len(unique_keys)

        print(f"\ntotal items: {total_items} | Unique items: {unique_count}")

        if duplicates:
            dup_strings = [f"{key} ({count} times)" for key, count in duplicates.items()]
            print("Duplicates: " + " | ".join(dup_strings))
        else:
            print("no duplicates found.") 
        output_filename = "unique.txt"
        try:
            with open(output_filename, "w", encoding="utf-8") as file:
                for key in unique_keys:
                    file.write(f"{key}\n") 
            print(f"Unique list saved to {output_filename}")  
        except Exception as e:
            print(f"Error writing to outputfile: {e}") 
    if __name__ == "__main__" :
        process_duplicate_data()               
