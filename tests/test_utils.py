import pytest as pytest

from src.hamming_code import encode, decode, detect, fix


@pytest.fixture
def decoded_data():
    return [1, 0, 0, 1, 1, 0, 1, 0]


@pytest.fixture
def encoded_data():
    return [0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0]


@pytest.fixture
def encoded_data_1_error(encoded_data):
    encoded_data_1_error = encoded_data.copy()
    encoded_data_1_error[3] ^= 1
    return encoded_data_1_error


@pytest.fixture
def encoded_data_2_errors(encoded_data):
    encoded_data_2_errors = encoded_data.copy()
    encoded_data_2_errors[1] ^= 1
    encoded_data_2_errors[4] ^= 1
    return encoded_data_2_errors


def test_encode(decoded_data, encoded_data):
    assert encode(decoded_data) == encoded_data


def test_decode(decoded_data, encoded_data):
    assert decode(encoded_data) == decoded_data


def test_detect_correct(encoded_data):
    assert detect(encoded_data) is False


def test_detect_incorrect(encoded_data_2_errors):
    assert detect(encoded_data_2_errors) is True


def test_fix_correct(encoded_data):
    assert fix(encoded_data) == encoded_data


def test_fix_incorrect(encoded_data_1_error, encoded_data):
    assert fix(encoded_data_1_error) == encoded_data
