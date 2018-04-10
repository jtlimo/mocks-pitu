from unittest.mock import patch
from safe import is_the_world_safe
import pytest

class GoogleResponse:

    def __init__(self, status_code):
        self.status_code = status_code

@patch('requests.get', return_value=GoogleResponse(200))
def test_that_the_world_is_safe_when_has_google(requests_mock):
   assert is_the_world_safe()
   requests_mock.assert_called_with('http://google.com')


@patch('requests.get', return_value=GoogleResponse(400))
def test_that_the_world_is_safe_when_has_google(requests_mock):
   assert is_the_world_safe() is False
   requests_mock.assert_called_with('http://google.com')

@patch('requests.get', side_effect=ConnectionError('No connection'))
def test_that_the_world_is_safe_when_has_google(requests_mock):
    with pytest.raises(ConnectionError) as excinfo:
        is_the_world_safe()
    assert str(excinfo.value) == 'No connection'

    requests_mock.assert_called_with('http://google.com')
