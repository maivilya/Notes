from colorama import Fore, Style


class View(object):

    @staticmethod
    def show_number_point_list(notes):
        for note in notes:
            print(Fore.YELLOW + '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
                  + Style.RESET_ALL)
            print(note)
            print(Fore.YELLOW + '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
                  + Style.RESET_ALL)

    @staticmethod
    def show_note(note):
        print(Fore.YELLOW + '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
              + Style.RESET_ALL)
        print(note)
        print(Fore.YELLOW + '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
              + Style.RESET_ALL)

    @staticmethod
    def show_empty_list_message():
        print(Fore.YELLOW + '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
              + Style.RESET_ALL)
        print('No notes')
        print(Fore.YELLOW + '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
              + Style.RESET_ALL)

    @staticmethod
    def display_note_id_not_exist(note_id):
        print(Fore.RED + '**************************************************************'
              + Style.RESET_ALL)
        print('Not such note with id {}'.format(note_id))
        print(Fore.RED + '**************************************************************'
              + Style.RESET_ALL)

    @staticmethod
    def display_note_id_exist(note_id):
        print(Fore.RED + '**************************************************************')
        print('The note with id: {} is already there'.format(note_id))
        print('**************************************************************'
              + Style.RESET_ALL)

    @staticmethod
    def display_note_stored():
        print(Fore.YELLOW + '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++' + Style.RESET_ALL)
        print(Fore.GREEN + 'Note added' + Style.RESET_ALL)
        print(Fore.YELLOW + '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++' + Style.RESET_ALL)

    @staticmethod
    def display_note_updated(note_id):
        print(Fore.YELLOW + '---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --' + Style.RESET_ALL)
        print(Fore.GREEN + 'Tag with id:{} updated successfully'
              .format(note_id) + Style.RESET_ALL)
        print(Fore.YELLOW + '---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --' + Style.RESET_ALL)

    @staticmethod
    def display_note_deletion(note_id):
        print('--------------------------------------------------------------')
        print(Fore.LIGHTRED_EX + 'Removing a note with id: {} is done!'.format(note_id) + Style.RESET_ALL)
        print('--------------------------------------------------------------')

    @staticmethod
    def display_all_notes_deletion():
        print(Fore.RED + '--------------------------------------------------------------')
        print('All notes are removed')
        print('--------------------------------------------------------------' + Style.RESET_ALL)


def display_note_id_not_exist(search_id):
    return search_id