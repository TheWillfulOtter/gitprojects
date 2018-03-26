'''
Journal app based on the Talk Python Training
by Michael Kennedy
Written by Michael Dux
'''
import journal_file
import datetime

def main():
    print_header()
    run_event_loop()


def print_header():
        print('----------------------------------')
        print('           JOURNAL APP')
        print('----------------------------------')
        print()


def run_event_loop():
    print('What do you want to do with your Journal?')
    cmd = 'EMPTY'
    journal_name = 'default'
    journal_data = journal_file.load(journal_name)

    while cmd != 'x' and cmd:
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x' and cmd:
            print("Sorry, we don't understand {}.".format(cmd))

    print('Logging off. Go and Get after it!')
    journal_file.save(journal_name, journal_data)

def list_entries(data):
    print('Your journal entries')
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print('* [{}] {}'.format(idx + 1, entry))


def add_entry(data):
    #Added a date string to the original program to give the data some sort of relevance.
    entry = input('Type your entry, <enter> to exit: ')
    the_day = datetime.date.today()
    text = str(the_day) + " " + str(entry)
    journal_file.add_entry(text, data)


if __name__ == '__main__':
    main()
