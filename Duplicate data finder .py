def read_entries(filename):
    try:
        with open(filename, "r") as f:
            lines = [line.strip() for line in f]
    except FileNotFoundError:
        print(f"File '{filename}' not found. Please enter a valid file name.")
        return None
    return [line for line in lines if line != ""]
def normalize(entry, ignore_case):
    if ignore_case:
        return " ".join(entry.lower().split())
    return entry
def run(filename, option):
    entries = read_entries(filename)
    if entries is None:
        return
    if len(entries) == 0:
        print("File is empty. Nothing to check.")
        return
    ignore_case = (str(option).strip() == "2")
    items = [normalize(e, ignore_case) for e in entries]
    unique_set = set(items)
    counts = {}
    unique_list = []
    for item in items:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
            unique_list.append(item)
    duplicates = [(k, v) for k, v in counts.items() if v > 1]
    print(f"\nTotal items: {len(items)} | Unique items: {len(unique_set)}")
    if duplicates:
        parts = [f"{k} ({v} times)" for k, v in duplicates]
        print("Duplicates: " + " | ".join(parts))
    else:
        print("No duplicates found.")
        
    with open("unique.txt", "w") as f:
        for item in unique_list:
            f.write(item + "\n")
    print("Unique list saved to unique.txt")
def main():
    filename = input("Enter file name: ").strip()
    print("\nMenu:")
    print("1. Exact match")
    print("2. Ignore case and extra spaces")
    choice = input("Choose option (1/2): ").strip()
    run(filename, choice)
if __name__ == "__main__":
    main()
