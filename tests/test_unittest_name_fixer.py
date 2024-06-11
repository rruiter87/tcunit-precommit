from importlib.resources import files

import pytest
from unittest_name_fixer import all_method_names_match_test_names, fix_test_names

import tests.data


@pytest.fixture()
def one_failing_one_ok_name():
    return (
        files(tests.data)
        .joinpath("UnitTestWithOneMatchingAndOneNonMatchingName.TcPOU")
        .read_text(encoding="UTF-8")
    )


@pytest.fixture()
def all_matching_names():
    return (
        files(tests.data)
        .joinpath("UnitTestOnlyMatchingNames.TcPOU")
        .read_text(encoding="UTF-8")
    )


@pytest.fixture()
def two_non_matching_names():
    return (
        files(tests.data)
        .joinpath("UnitTestOnlyMismatchingNames.TcPOU")
        .read_text(encoding="UTF-8")
    )


@pytest.fixture()
def one_missing_test():
    return (
        files(tests.data)
        .joinpath("OneTestHasMissingTest.TcPOU")
        .read_text(encoding="UTF-8")
    )


def test_file_with_non_matching_names(one_failing_one_ok_name):
    assert not all_method_names_match_test_names(one_failing_one_ok_name, verbose=False)


def test_file_with_only_matching_names(all_matching_names):
    assert all_method_names_match_test_names(all_matching_names, verbose=False)


def test_file_with_two_mismatching_names(two_non_matching_names):
    assert not all_method_names_match_test_names(two_non_matching_names, verbose=False)


def test_missing_test_at_start(one_missing_test):
    assert all_method_names_match_test_names(one_missing_test, verbose=False)


def test_fixing_non_matching_names(two_non_matching_names):
    fixed_content = fix_test_names(two_non_matching_names)
    assert all_method_names_match_test_names(fixed_content, verbose=False)
