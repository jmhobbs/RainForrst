# -*- coding: utf-8 -*-

class ForrstError ( Exception ):
	def __init__ ( self, apiversion, message ):
		self.apiversion = apiversion
		self.message = message

	def __str__ ( self ):
		return self.message

	def __repr__ ( self ):
		return '<ForrstError( %d, "%s" )>' % ( self.apiversion, self.message )

class InvalidVersionError ( ForrstError ):
	def __init__ ( self, apiversion ):
		ForrstError.__init__( self, apiversion, 'Version %d is not a valid API version.' % apiversion )

class InvalidObjectError ( ForrstError ):
	def __init__ ( self, apiversion, object_type ):
		ForrstError.__init__( self, apiversion, 'The object type "%s" is not valid in API version %d.' % ( object_type, apiversion ) )

class InvalidMethodError ( ForrstError ):
	def __init__ ( self, apiversion, object_type, method_name ):
		ForrstError.__init__( self, apiversion, 'The method "%s" is not valid for the object "%s" in API version %d.' % ( object_type, method_name, apiversion ) )

class ForrstNotFound ( ForrstError ):
	def __init__ ( self, apiversion ):
		ForrstError.__init__( self, apiversion, 'Object Not Found' )
