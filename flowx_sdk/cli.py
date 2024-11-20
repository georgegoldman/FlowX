import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="Flowx_sdk cli tool")
    parser.add_argument('command', help="The command to run")
    parser.add_argument('--option', help='An example option', default='default_value')

    args = parser.parse_args()

    if args.command == 'init':
        # Get the root directory of your project
        project_root = os.getcwd()

        # Define the file pat
        file_path = os.path.join(project_root, ".flowx")
        print(file_path)

        # Just create the file
        with open(file_path, 'w') as file:
            pass # This just opens the file and leaves it empty
        print("Sdk initialized")


main()