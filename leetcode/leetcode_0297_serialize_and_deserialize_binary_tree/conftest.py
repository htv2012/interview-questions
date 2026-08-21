import pytest

from solution import Codec


@pytest.fixture
def codec():
    """Function under test"""
    codec_obj = Codec()
    return codec_obj
