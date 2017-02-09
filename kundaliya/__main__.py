import argparse
from creator import Params


def main():
    parser = argparse.ArgumentParser(description='Tool chain to build and test typefaces')
    subparsers = parser.add_subparsers(help='List of commands to be used',dest="subparser_name")
    build_parser = subparsers.add_parser('build', help='Builds the typefaces according to the settings.yaml')
    build_parser.add_argument("-p", "--path",
                        help="Path to the directory containing the settings.yaml, by default current directory is searched for setting.yaml")
    args=parser.parse_args()
    args=vars(args)

    subparser_name=args.pop('subparser_name')

    if subparser_name=='build':
        settings=Params(args.pop('path'))


if __name__ == '__main__':
    main()
