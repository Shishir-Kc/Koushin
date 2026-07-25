import argparse

def main():
    parser = argparse.ArgumentParser(prog="koushin")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("generate", help="Generate something")
    subparsers.add_parser("info", help="Show info")

    args = parser.parse_args()

    if args.command == "generate":
        print("Generating...")
    elif args.command == "info":
        print("koushin info here")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
