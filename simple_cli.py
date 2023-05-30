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


subparsers = parser.add_subparsers(dest='subparse',help='sub-command help')

load_set_parser = subparsers.add_parser('load_set_from_file', help='load a new set from a file')
load_set_parser.add_argument('-f', dest='file' , required=True, help='Path to the file')
load_set_parser.add_argument('-n', dest='name' , required=True, help='Name of the created set')
load_set_parser.add_argument('-s', dest='separator' , required=True, help='Separator used in the file')
load_set_parser.set_defaults(func=load_set_from_file)

args = parser.parse_args()

if not hasattr(args, 'func'):
    parser.print_help()
else:
    args.func(args)