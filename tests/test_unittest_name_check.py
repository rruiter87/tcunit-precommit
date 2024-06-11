from importlib.resources import files

import pytest

import tests.data
from src.tcunit_precommit.unittest_name_check import all_method_names_match_test_names


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
    assert not all_method_names_match_test_names(one_failing_one_ok_name)


def test_file_with_only_matching_names(all_matching_names):
    assert all_method_names_match_test_names(all_matching_names)


def test_file_with_two_mismatching_names(two_non_matching_names):
    assert not all_method_names_match_test_names(two_non_matching_names)


def test_missing_test_at_start(one_missing_test):
    assert all_method_names_match_test_names(one_missing_test)
