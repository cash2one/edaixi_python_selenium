# -*- coding: utf-8 -*-
import mock
#from object import patch
from mock import patch
from time import sleep
 
class Sweetness(object):
    def slow_remote_call(self):
        sleep(10)
        return "some_data" 
# lets pretend we get this back from our remote api call
 
def test_long_call():
    s = Sweetness()
#     with patch.object(s, "slow_remote_call", return_value="some_data"):
#         result = s.slow_remote_call()
#     assert result == "some_data"