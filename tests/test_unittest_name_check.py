from importlib.resources import files

import pytest

import tests.data
from src.tcunit_precommit.unittest_name_check import check_unit_test_method_names


@pytest.fixture()
def one_failing_one_ok_name():
    return (
        files(tests.data)
        .joinpath("UnitTestWithOneMatchingAndOneNonMatchingName.TcPOU")
        .read_text()
    )


def test_file_with_non_matching_names(one_failing_one_ok_name):
    assert not check_unit_test_method_names(one_failing_one_ok_name)
