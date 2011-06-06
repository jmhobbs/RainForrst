# -*- coding: utf-8 -*-

"""
RainForrst is a simple module for quick access to the Forrst API.
"""

# Version 1 based on http://forrst.com/apidocs.html
# Version 2+ based on http://forrst.com/api
#
# Last Updated 2011-05-06

import errors
import objects

object_mapping = {
	'user': objects.User,
	'post': objects.Post,
	'users': objects.User,
	'posts': objects.Post
}

class Forrst ( object ):

	queryable_objects = {
		1: [ 'user' ],
		2: [ 'user', 'users', 'post', 'posts' ]
	}

	def __init__ ( self, version ):
		self.version = version
		self.method = ''

		if self.version not in self.queryable_objects.keys():
			raise errors.InvalidVersionError( self.version )


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
