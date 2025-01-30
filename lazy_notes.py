import datetime
import os

NOTES_FILE = "notes.txt"

def add_note():
    note = input("Enter text for a new note: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if not os.path.isfile(NOTES_FILE):
        with open(NOTES_FILE, "w", encoding="utf-8") as file:
            file.write(f"[{timestamp}] {note}\n")
    else:
        with open(NOTES_FILE, "a", encoding="utf-8") as file:
            file.write(f"[{timestamp}] {note}\n")

    print("Note saved!\n")

def search_notes():
    if not os.path.isfile(NOTES_FILE):
        print("Couldn't find the notes file.")
        return
    
    keyword = input("Enter a word to search: ").lower()
    with open(NOTES_FILE, "r", encoding="utf-8") as file:
        notes = file.readlines()
    
    found_notes = [note for note in notes if keyword in note.lower()]
    if found_notes:
        print("\nFound:")
        for note in found_notes:
            print(note.strip())
    else:
        print("Couldn't find notes with that word.")
    print()

def main():
    while True:
        print("Select an action:")
        print("1 - Add note")
        print("2 - Search in notes")
        print("3 - Quit")
        choice = input("Select action: ")
        
        if choice == "1":
            add_note()
        elif choice == "2":
            search_notes()
        elif choice == "3":
            print("Quitting...")
            break
        else:
            print("Invalid action. Try again.\n")

if __name__ == "__main__":
    main()
