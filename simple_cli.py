import argparse
from CLI import CLI_Utilities

PROGRAM_NAME = 'Flashcards Application'
PROGRAM_DESCRIPTION = 'Interface for Flashcards Application'
PROGRAM_BOTTOM_LINE = 'Happy learning'

parser = argparse.ArgumentParser(
    prog=PROGRAM_NAME,
    description=PROGRAM_DESCRIPTION,
    epilog=PROGRAM_BOTTOM_LINE
)

def load_set_from_file(args):
    if not CLI_Utilities.check_if_file_exists(args.file): print("File doesn't exist")
    else:
        try:
            flashcards = CLI_Utilities.convert_text_to_flashcards(args.file, args.separator)
            try_create_set(args.name, flashcards)
        except Exception:
            print("File is not properly formatted")

def try_create_set(name, flashcards):
    if not CLI_Utilities.check_if_name_is_valid(name):
        print(f"Name {name} is not a valid set name")
    elif CLI_Utilities.check_if_set_exists(name):
        print(f"Set with given name already exists")
    else:
        CLI_Utilities.create_set(name, flashcards)
        print("Done")

def export_set_to_file(args):
    if not CLI_Utilities.check_if_directory_exists(args.directory): print("Directory doesn't exist")
    if not CLI_Utilities.check_if_set_exists(args.set): print("Set with given name doesn't exist")
    else:
        if not args.name: args.name = args.set
        if not args.separator: args.separator = ' - '
        set_text = CLI_Utilities.get_set_to_text(args.set, args.separator)
        CLI_Utilities.write_set_text_to_file(set_text, args.directory, args.name)
        print("Done")
    
def export_all_sets(args):
    if not CLI_Utilities.check_if_directory_exists(args.directory): print("Directory doesn't exist")
    else:
        if not args.name: args.name = 'CreatedSets'
        if not args.separator: args.separator = ' - '
        CLI_Utilities.export_all_sets_to_archive(args.directory, args.name, args.separator)
        print("Done")


subparsers = parser.add_subparsers(dest='subparse',help='sub-command help')

load_set_parser = subparsers.add_parser('load_set_from_file', help='load a new set from a file')
load_set_parser.add_argument('-f', dest='directory' , required=True, help='Path to the file')
load_set_parser.add_argument('-n', dest='name' , required=True, help='Name of the created set')
load_set_parser.add_argument('-s', dest='separator' , required=True, help='Separator used in the file')
load_set_parser.set_defaults(func=load_set_from_file)

export_set_parser = subparsers.add_parser('export_set_to_file', help='export an existing set to a file')
export_set_parser.add_argument('--set', dest='set', required=True, help='Set being exported')
export_set_parser.add_argument('-d', dest='directory' , required=True, help='Path to the directory')
export_set_parser.add_argument('-n', dest='name' , required=False, help='Name of the file')
export_set_parser.add_argument('-s', dest='separator' , required=False, help='Separator used in the file')
export_set_parser.set_defaults(func=export_set_to_file)

export_all_sets_parser = subparsers.add_parser('export_all_sets', help='export all sets to an archive')
export_all_sets_parser.add_argument('-d', dest='directory' , required=True, help='Path to the directory')
export_all_sets_parser.add_argument('-n', dest='name' , required=False, help='Name of the archive')
export_all_sets_parser.add_argument('-s', dest='separator' , required=False, help='Separator used in sets files')
export_all_sets_parser.set_defaults(func=export_all_sets)

args = parser.parse_args()

if not hasattr(args, 'func'):
    parser.print_help()
else:
    args.func(args)