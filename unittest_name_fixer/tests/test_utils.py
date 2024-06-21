from importlib.resources import files

import pytest

import unittest_name_fixer.tests.data as test_data
from unittest_name_fixer.utils import find_mismatched_test_names, fix_test_names


@pytest.fixture()
def one_failing_one_ok_name():
    return (
        files(test_data)
        .joinpath("UnitTestWithOneMatchingAndOneNonMatchingName.TcPOU")
        .read_text(encoding="UTF-8")
    )


@pytest.fixture()
def all_matching_names():
    return (
        files(test_data)
        .joinpath("UnitTestOnlyMatchingNames.TcPOU")
        .read_text(encoding="UTF-8")
    )


@pytest.fixture()
def two_non_matching_names():
    return (
        files(test_data)
        .joinpath("UnitTestOnlyMismatchingNames.TcPOU")
        .read_text(encoding="UTF-8")
    )


@pytest.fixture()
def one_missing_test():
    return (
        files(test_data)
        .joinpath("OneTestHasMissingTest.TcPOU")
        .read_text(encoding="UTF-8")
    )


@pytest.fixture()
def ordered_test():
    return files(test_data).joinpath("OrderedTest.TcPOU").read_text(encoding="UTF-8")


def test_file_with_non_matching_names(one_failing_one_ok_name):
    mismatches = find_mismatched_test_names(one_failing_one_ok_name)
    assert len(mismatches) > 0


def test_file_with_only_matching_names(all_matching_names):
    mismatches = find_mismatched_test_names(all_matching_names)
    assert len(mismatches) == 0


def test_file_with_two_mismatching_names(two_non_matching_names):
    mismatches = find_mismatched_test_names(two_non_matching_names)
    assert len(mismatches) > 0


def test_missing_test_at_start(one_missing_test):
    mismatches = find_mismatched_test_names(one_missing_test)
    assert len(mismatches) == 0


def test_fixing_non_matching_names(two_non_matching_names):
    mismatches = find_mismatched_test_names(two_non_matching_names)
    fixed_content = fix_test_names(two_non_matching_names, mismatches)
    new_mismatches = find_mismatched_test_names(fixed_content)
    assert len(new_mismatches) == 0


def test_ordered_test(ordered_test):
    mismatches = find_mismatched_test_names(ordered_test)
    assert len(mismatches) == 1
