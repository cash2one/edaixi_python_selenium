# -*- coding: utf-8 -*-
from mock import Mock
 
# create the mock object
mockFoo = Mock(name = "Foo")
 
print mockFoo
# returns: <Mock name='Foo' id='494864'>
print repr(mockFoo)
# still returns: <Mock name='Foo' id='494864'>