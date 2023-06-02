import argparse
from CLI import CLI_Utilities
from CLI.FileOperator import FileOperator, FileAlias
from CLI.Exporters.BaseExporter import ExportInfo
from CLI.Exporters.SingleSetExporter import SingleSetExporter
from CLI.Exporters.AllSetsExporter import AllSetsExporter
from CLI.FlashcardsSetImporter import FlashcardsSetImporter, ImportInfo

FILE_OPERATOR = FileOperator()

PROGRAM_NAME = 'Flashcards Application'
PROGRAM_DESCRIPTION = 'Interface for Flashcards Application'
PROGRAM_BOTTOM_LINE = 'Happy learning'

parser = argparse.ArgumentParser(
    prog=PROGRAM_NAME,
    description=PROGRAM_DESCRIPTION,
    epilog=PROGRAM_BOTTOM_LINE
)

def load_set_from_file(args):
    import_info = ImportInfo(args.filepath, args.name, args.separator)
    importer = FlashcardsSetImporter(import_info)

    if not importer.check_if_file_exists(): print("File doesn't exist")
    if not importer.check_if_name_is_valid(): print(f"Name {args.name} is not a valid set name")
    elif importer.check_if_set_exists(): print(f"Set with given name already exists")
    else:
        try:
            importer.import_set()
            print("Done")
        except Exception:
            print("File is not properly formatted")

def export_set_to_file(args):
    export_info = ExportInfo(args.directory, args.name, args.separator)
    exporter = SingleSetExporter(args.set_name, export_info)

    if not exporter.check_if_directory_exists(): print("Directory doesn't exist")
    if not exporter.check_if_set_exists(): print("Set with given name doesn't exist")
    else:
        exporter.export_set()
        print("Done")
    
def export_all_sets(args):
    export_info = ExportInfo(args.directory, args.name, args.separator)
    exporter = AllSetsExporter(export_info)

    if not exporter.check_if_directory_exists(): print("Directory doesn't exist")
    else:
        exporter.export_sets()
        print("Done")

subparsers = parser.add_subparsers(dest='subparse',help='sub-command help')

load_set_parser = subparsers.add_parser('load_set_from_file', help='load a new set from a file')
load_set_parser.add_argument('-f', dest='filepath', required=True, help='Path to the file')
load_set_parser.add_argument('-n', dest='name' , required=True, help='Name of the created set')
load_set_parser.add_argument('-s', dest='separator' , required=True, help='Separator used in the file')
load_set_parser.set_defaults(func=load_set_from_file)

export_set_parser = subparsers.add_parser('export_set_to_file', help='export an existing set to a file')
export_set_parser.add_argument('--set', dest='set_name', required=True, help='Set being exported')
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