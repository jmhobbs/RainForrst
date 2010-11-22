# -*- coding: utf-8 -*-

"""
RainForrst is a simple module for quick access to the Forrst API.
"""

# Based on http://forrst.com/apidocs.html
# Last Updated 2010-11-16

import errors
import objects

object_mapping = {
	'user': objects.User,
	'post': objects.Post
}

class Forrst ( object ):

	queryable_objects = {
		1: [ 'user' ]
	}

	def __init__ ( self, version ):
		self.version = version
		self.method = ''

	def __getattr__ ( self, name ):
		if name in self.queryable_objects[self.version]:
			return object_mapping[name]( self.version )
		else:
			raise errors.InvalidObjectError( self.version, name )

if __name__ == "__main__":
	pass
	#x = Forrst( 1 )
	#jmhobbs = x.user.info( username='jmhobbs' )
	#print jmhobbs
	#print jmhobbs.posts()
	#kyle = objects.User( 1, { 'username': 'kyle' } )
	#print kyle.posts()