A simple program designed to quickly record notes along with the timestamp of when they were written. This tool allows users to easily store their thoughts, ideas, or any important information and search through past entries.

## Features

- **Add notes**: Quickly record notes with a timestamp.
- **Search notes**: Search through your saved notes by keywords.
- **Timestamp**: Every note is saved with the exact date and time it was written.

## Requirements

Before running this program, make sure you have the following installed:

- Python 3.12

## Installation

To get started with this program, follow these simple steps:

1. **Clone the repository**:
   
   git clone https://github.com/Yereklayy/Lazy-Notes.git

3. **Navigate to the project folder**:

   cd lazy-notes

4. **Run the script**:
   
   python lazy_notes.py

No additional libraries or dependencies are required, as this script uses only the Python Standard Library.

## Usage

After running the program, you will be prompted with the following options:

1. **Add a note**:
   - Enter the text of the note.
   - The program will record the note along with the current timestamp.
   
2. **Search for notes**:
   - You can search for specific keywords within your saved notes. The program will return all notes that contain the specified keyword.

3. **Quit**:
   - This option will exit the program.

### Example Run

Select an action:
1 - Add note
2 - Search in notes
3 - Quit
Select action: 1
Enter text for a new note: Buy groceries.
Note saved!

Select an action:
1 - Add note
2 - Search in notes
3 - Quit
Select action: 2
Enter a word to search: groceries
Found:
[2025-01-30 15:30:25] Buy groceries.

Select an action:
1 - Add note
2 - Search in notes
3 - Quit
Select action: 3
Quitting...

## File Format

Notes are saved in a simple text file, notes.txt. Each note is stored with the following format:


[YYYY-MM-DD HH:MM:SS] Note text

For example:

[2025-01-01 00:00:00] Buy groceries.
