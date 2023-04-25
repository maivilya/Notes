import datetime
from colorama import Fore, Style

from controller import Controller
from modelJSON import ModelJSON
from note import Note
from view import View


def run():
    c = Controller(ModelJSON("notes.json"), View())

    while True:
        command = input(Fore.BLUE +
                        '1 - Add note\n'
                        '2 - Show note\n'
                        '3 - Modified note\n'
                        '4 - Remove note\n'
                        '5 - Remove all notes\n'
                        '6 - Show all notes\n'
                        '7 - Exit\n' +
                        'Choose features: '
                        + Style.RESET_ALL)
        if command == '7':
            break

        if command == '1':
            print(Fore.GREEN + '\nAdd note:' + Style.RESET_ALL)
            c.create_note(get_note_data())

        elif command == '2':
            print(Fore.GREEN + '\nShow note:' + Style.RESET_ALL)
            if c.notes_exist():
                c.show_note(int(get_number()))
        elif command == '3':
            if c.notes_exist():
                print(Fore.YELLOW + '\nModified note:' + Style.RESET_ALL)
                updated_id = int(get_number())
                if c.note_id_exist(updated_id):
                    c.update_note(updated_id, get_note_data())

        elif command == '4':
            if c.notes_exist():
                print(Fore.RED + '\nRemove note:' + Style.RESET_ALL)
                delete_id = int(get_number())
                if c.note_id_exist(delete_id):
                    c.delete_note(delete_id)

        elif command == '5':
            if c.notes_exist():
                print(Fore.RED + '\nRemove all notes:' + Style.RESET_ALL)
                if input(Fore.RED + 'Are you sure to remove all notes?(yes/no): '
                         + Style.RESET_ALL).capitalize() == 'yes':
                    if c.notes_exist():
                        c.delete_all_notes()

        elif command == '6':
            if c.notes_exist():
                print(Fore.BLUE + '\nList of all notes:' + Style.RESET_ALL)
                c.show_notes()
        else:
            print(Fore.RED + 'Not such command' + Style.RESET_ALL)


def get_note_data():
    note_id = 0
    date = datetime.datetime.now()
    title = input('Enter the title of the note: ')
    text = input('Enter the description of the note: ')
    return Note(note_id, date, title, text)


def get_number():
    while True:
        get_choice = input('Enter the id of the note: ')
        if get_choice.isdigit() and int(get_choice) > 0:
            return get_choice
        else:
            print(Fore.RED + 'Enter positive digit' + Style.RESET_ALL)