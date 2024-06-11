from importlib.resources import files

import pytest

import tests.data
from src.tcunit_precommit.unittest_name_check import check_unit_test_method_names


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


def test_file_with_non_matching_names(one_failing_one_ok_name):
    assert not check_unit_test_method_names(one_failing_one_ok_name)


def test_file_with_only_matching_names(all_matching_names):
    assert check_unit_test_method_names(all_matching_names)
