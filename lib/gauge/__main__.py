def main():
    HEADER = ('Gauge. Version 0.0.1\n'
        'Command-line assistant and toolbox for MS SQL server\n\n'
        'usage: gauge [-v|--version] [-h|--help] [-s|--server] [-u|--user] [-p|--password]\n'
        '             [--[no-]colored] <command> [<args>] [<command options>]\n')

    COMMANDS = ('The most commonly used gauge commands are:\n'
        'check    Checks database structure against the metadata\n'
        'sync     Synchronize database structure regarding the metadata\n'
        'help     Displays additional help info\n\n'
        "See 'gauge help <command>' for more information on a specific command.")

    print(HEADER)
    print(COMMANDS)

if __name__ == '__main__':
    main()
