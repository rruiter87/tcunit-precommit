import argparse
import sys

from unittest_name_fixer import all_method_names_match_test_names


def main():
    parser = argparse.ArgumentParser(
        description="Check if method names match test names in XML files."
    )
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("filenames", nargs="+", help="XML files to check")

    args = parser.parse_args()

    all_files_match = True

    for filename in args.filenames:
        try:
            with open(filename, "r", encoding="utf-8") as file:
                xml_content = file.read()
                if not all_method_names_match_test_names(xml_content, args.verbose):
                    all_files_match = False
        except Exception as e:
            print(f"Error reading file {filename}: {e}", file=sys.stderr)
            all_files_match = False

    if not all_files_match:
        sys.exit(1)


if __name__ == "__main__":
    main()
