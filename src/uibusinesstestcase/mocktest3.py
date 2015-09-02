# -*- coding: utf-8 -*-
from mock import Mock

 
# The class interfaces
class Foo(object):
    # instance properties
    _fooValue = 123
     
    def callFoo(self):
        print "Foo:callFoo_"
     
    def doFoo(self, argValue):
        print "Foo:doFoo:input = ", argValue    
 
# create the mock object
mockFoo = Mock(spec = Foo)
 
# accessing the mocked attributes
print mockFoo
# returns <Mock spec='Foo' id='507120'>
print mockFoo._fooValue
# returns <Mock name='mock._fooValue' id='2788112'>
print mockFoo.callFoo()
# returns: <Mock name='mock.callFoo()' id='2815376'>
 
mockFoo.callFoo()
# nothing happens, which is fine
 
# accessing the missing attributes
print mockFoo._fooBar
# raises: AttributeError: Mock object has no attribute '_fooBar'
mockFoo.callFoobar()
# raises: AttributeError: Mock object has no attribute 'callFoobar'