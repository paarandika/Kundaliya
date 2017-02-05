import argparse


def main():
    parser = argparse.ArgumentParser(description='Tool chain to build and test typefaces')
    subparsers = parser.add_subparsers(help='List of commands to be used')
    parser_build = subparsers.add_parser('build', help='Builds the typefaces according to the settings.yaml')
    parser_build.add_argument("-p", "--path",
                        help="Path to the directory containing the settings.yaml, by default current directory is searched for setting.yaml")
    parser.parse_args()


if __name__ == '__main__':
    main()
