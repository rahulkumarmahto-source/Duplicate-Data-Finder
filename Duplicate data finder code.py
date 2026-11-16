"""Duplicate Data Finder

Reads a text file (one entry per line), finds duplicate entries, reports how
many times each one repeats, and saves the unique entries to unique.txt.

Menu:
  1. Exact match
  2. Ignore case and extra spaces
"""


def read_entries(filename):
    """Read non-empty lines from a file into a list.
    Returns None if the file does not exist."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return [line.rstrip("\n") for line in f if line.strip() != ""]
    except FileNotFoundError:
        print(f"File '{filename}' not found. Please enter a valid file name.")
        return None


def normalize(entry):
    """Ignore case and extra spaces (collapse inner spaces, trim ends)."""
    return " ".join(entry.split()).lower()


def find_duplicates(entries, ignore_case):
    """Return (prepared_entries, unique_in_order, duplicates_dict)."""
    prepared = [normalize(e) for e in entries] if ignore_case else list(entries)

    # Use a set to find the unique entries (keep first-seen order in a list).
    seen = set()
    unique = []
    for item in prepared:
        if item not in seen:
            seen.add(item)
            unique.append(item)

    # Use a loop to count how many times each unique entry repeats.
    duplicates = {}
    for item in unique:
        count = 0
        for other in prepared:
            if other == item:
                count += 1
        if count > 1:
            duplicates[item] = count

    return prepared, unique, duplicates


def save_unique(unique, filename="unique.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for item in unique:
            f.write(item + "\n")


def main():
    print("=== Duplicate Data Finder ===")
    filename = input("Enter file name (e.g. data.txt): ").strip()

    entries = read_entries(filename)
    if entries is None:
        return
    if len(entries) == 0:
        print("File is empty. Nothing to check.")
        return

    print("\nMenu:")
    print("1. Exact match")
    print("2. Ignore case and extra spaces")
    choice = input("Enter your choice (1/2): ").strip()

    if choice == "1":
        ignore_case = False
    elif choice == "2":
        ignore_case = True
    else:
        print("Invalid choice. Please enter 1 or 2.")
        return

    prepared, unique, duplicates = find_duplicates(entries, ignore_case)

    print(f"\nTotal items: {len(prepared)} | Unique items: {len(unique)}")
    if duplicates:
        parts = [f"{item} ({count} times)" for item, count in duplicates.items()]
        print("Duplicates: " + " | ".join(parts))
    else:
        print("No duplicates found.")

    save_unique(unique)
    print("Unique list saved to unique.txt")


if __name__ == "__main__":
    main()
