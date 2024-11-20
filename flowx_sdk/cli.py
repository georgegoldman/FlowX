import argparse

def main():
    parser = argparse.ArgumentParser(description="Flowx_sdk cli tool")
    parser.add_argument('command', help="The command to run")
    parser.add_argument('--option', help='An example option', default='default_value')

    args = parser.parse_args()

    if args.command == 'init':
        print("")