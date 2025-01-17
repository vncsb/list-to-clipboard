import argparse

from list_to_clipboard import core

def parse_args():

    parser = argparse.ArgumentParser(
        prog="l2c",
        description="Gets itens from file or input and make them available to be copied to the clipboard",
        formatter_class=argparse.MetavarTypeHelpFormatter,
    )

    parser.add_argument(
        "-f",
        "--filename",
        help="File to read. Ignored when something is passed via stdin.",
        type=str,
        required=False,
    )
    parser.add_argument(
        "--no-description",
        action="store_true",
        help="Indicates that the list has no description for the values. (default: %(default)s)",
    )
    parser.add_argument(
        "--description-separator",
        default="||",
        help="Text that separates the value from description. (default: %(default)s)",
        type=str,
    )

    return parser.parse_args()

def main():
    args = parse_args()
    core.main(args.filename)
