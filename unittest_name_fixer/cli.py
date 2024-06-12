import argparse
import sys

from unittest_name_fixer.utils import all_method_names_match_test_names, fix_test_names


def main():
    parser = argparse.ArgumentParser(
        description="Check if method names match test names in XML files."
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Do not print which files has non-matching test-method names.",
    )
    parser.add_argument(
        "--fix", action="store_true", help="Fix non-matching TEST('..') METHOD names"
    )
    parser.add_argument("filenames", nargs="+", help="XML files to check")

    args = parser.parse_args()
    verbose = not args.quiet
    all_files_match = True

    for filename in args.filenames:
        try:
            with open(filename, "r", encoding="utf-8") as file:
                xml_content = file.read()
                if not all_method_names_match_test_names(xml_content, verbose):
                    all_files_match = False
                    if args.fix:
                        if verbose:
                            print(f"Fixing file {filename}...")
                        fixed_content = fix_test_names(xml_content)
                        with open(filename, "w", encoding="utf-8") as file:
                            file.write(fixed_content)
        except Exception as e:
            print(f"Error reading file {filename}: {e}", file=sys.stderr)
            all_files_match = False

    if not all_files_match:
        sys.exit(1)


if __name__ == "__main__":
    main()
