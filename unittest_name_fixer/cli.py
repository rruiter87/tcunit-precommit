import argparse
import sys

from unittest_name_fixer.utils import find_mismatched_test_names, fix_test_names


def main():
    parser = argparse.ArgumentParser(
        description="Check if TwinCAT method names match TcUnit test names."
    )
    parser.add_argument(
        "--fix", action="store_true", help="Fix non-matching TEST('..') METHOD names"
    )
    parser.add_argument("filenames", nargs="+", help="TcPOU files to check")
    args = parser.parse_args()

    all_files_match = True
    for filename in args.filenames:
        try:
            with open(filename, "r", encoding="utf-8") as file:
                xml_content = file.read()
                non_matches = find_mismatched_test_names(xml_content)
                if len(non_matches) > 0:
                    all_files_match = False
                    if args.fix:
                        print(f"Fixing file {filename}...")
                        fixed_content = fix_test_names(xml_content, non_matches)
                        with open(filename, "w", encoding="utf-8") as write_file:
                            write_file.write(fixed_content)
        except Exception as e:
            print(f"Error reading file {filename}: {e}", file=sys.stderr)
            all_files_match = False

    if not all_files_match:
        sys.exit(1)


if __name__ == "__main__":
    main()
