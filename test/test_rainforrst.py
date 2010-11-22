# -*- coding: utf-8 -*-
import unittest
from nose.tools import raises

import sys, os

# Fix it so we import the dev version of RainForrst before anything else
lib_path = os.path.abspath( os.path.join( os.path.dirname( os.path.abspath( __file__ ) ), '..', 'lib' ) )
sys.path.insert( 0, lib_path )
import RainForrst
del sys.path[0]

class TestUsers ( unittest.TestCase ):

	def __init__ ( self, *args ):
		unittest.TestCase.__init__( self, *args )

		self.forrst = RainForrst.Forrst( 1 )

	def test_get_user_by_id ( self ):
		user = self.forrst.user.info( username='kyle' )
		self.assertEquals( user.id, '1' )

	@raises( RainForrst.errors.ForrstNotFound )
	def test_get_user_by_invalid_id ( self ):
		user = self.forrst.user.info( id=0 )

if __name__ == '__main__':
	unittest.main()