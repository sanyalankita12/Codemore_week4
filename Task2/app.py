import os

FILE_NAME = r"C:\Users\Ishit\PycharmProjects\PythonProject10\Task2\NOTES.txt"


def add_note():
    note = input("Enter your note: ")

    with open(FILE_NAME, "a") as file:
        file.write(note + "\n")

    print("Note added successfully.\n")


def view_notes():
    if not os.path.exists(FILE_NAME):
        print("No notes available.\n")
        return

    with open(FILE_NAME, "r") as file:
        notes = file.readlines()

    if not notes:
        print("No notes available.\n")
        return

    print("\nYour Notes:")
    for index, note in enumerate(notes, start=1):
        print(f"{index}. {note.strip()}")

    print()


def delete_note():
    if not os.path.exists(FILE_NAME):
        print("No notes available.\n")
        return

    with open(FILE_NAME, "r") as file:
        notes = file.readlines()

    if not notes:
        print("No notes available.\n")
        return

    print("\nAvailable Notes:")

    for index, note in enumerate(notes, start=1):
        print(f"{index}. {note.strip()}")

    try:
        choice = int(input("Enter note number to delete: "))

        if 1 <= choice <= len(notes):
            notes.pop(choice - 1)

            with open(FILE_NAME, "w") as file:
                file.writelines(notes)

            print("Note deleted successfully.\n")

        else:
            print("Invalid note number.\n")

    except ValueError:
        print("Please enter a valid number.\n")


def main():
    while True:

        print("===== FILE NOTES APP =====")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Delete Note")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_note()

        elif choice == "2":
            view_notes()

        elif choice == "3":
            delete_note()

        elif choice == "4":
            print("Thank you for using Notes App.")
            break

        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()