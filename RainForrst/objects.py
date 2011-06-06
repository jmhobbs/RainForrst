# -*- coding: utf-8 -*-

from errors import *

import urllib
import urllib2

# Protected JSON Import From pyforrst - https://github.com/paparent/pyforrst
try:
	import json
except ImportError:
	try:
		import simplejson as json
	except ImportError:
		raise Exception( "A JSON parser is required, e.g., simplejson at http://pypi.python.org/pypi/simplejson/")

class ForrstObject ( object ):
	_methods = {}
	_name = ''

	def __init__ ( self, apiversion, **kwargs ):
		
		self._version = apiversion
		self._method = ''
		self._loaded = False

		for key, value in kwargs.items():
			setattr( self, key, value )
			self._loaded = True

	def __getattr__ ( self, name ):
		try:
			if name in self._methods[self._version]:
				self._method = name
				return self
		except:
			pass

		return None

	def __call__ ( self, **kwargs ):
		if self._method not in self._methods[self._version].keys():
			raise InvalidMethodError( self._version, self._name, self._method )

		data = urllib.urlencode( kwargs )
		
		endpoint = 'http://api.forrst.com'
		if self._version > 1:
			endpoint = 'http://forrst.com'

		url = '%s/api/v%d/%s/%s?%s' % ( endpoint, self._version, self._methods[self._version][self._method], self._method, data )

		try:
			req = urllib2.Request( url )
			response = urllib2.urlopen( req )
			value = response.read()
			data = json.loads( value )
			if 'resp' not in data:
				raise ForrstError( self._version, 'Message malformed, no "resp" key: %s' % value )
			return self._parse( self._method, data['resp'] )
		except urllib2.HTTPError, e:
			if 404 == e.code:
				raise ForrstNotFound( self._version )
			else:
				raise e
		finally:
			self._method = ''

	def _parse ( self, method, data ):
		return data

class User ( ForrstObject ):
	_methods = {
		1: { 'info': 'users', 'posts': 'users' },
		2: { 'auth': 'users', 'info': 'users', 'posts': 'user' }
	}
	_name = 'users'

	def _parse ( self, method, data ):
		if 'info' == method:
			if 1 == self._version:
				return User( self._version, **data['user'] )
			else:
				return User( self._version, **data )
		elif 'posts' == method:
			posts = []
			for post in data['posts']:
				if 'snap' == post['post_type']:
					posts.append( Snap( self._version, **post ) )
				elif 'link' == post['post_type']:
					posts.append( Link( self._version, **post ) )
				elif 'code' == post['post_type']:
					posts.append( Code( self._version, **post ) )
				elif 'question' == post['post_type']:
					posts.append( Question( self._version, **post ) )
				else:
					posts.append( Post( self._version, **post ) )
			return posts

	def __call__ ( self, **kwargs ):
		# Intercept argument-less calls and add arguments if needed
		username = getattr( self, 'username', None )
		userid = getattr( self, 'id', None )
		if username or userid:
			if 'username' not in kwargs and 'id' not in kwargs:
				if username:
					kwargs['username'] = username
				elif userid:
					kwargs['id'] = userid
		return ForrstObject.__call__( self, **kwargs )

class Post ( ForrstObject ):
	_methods = {
		1: {},
		2: { 'show': 'posts', 'all': 'posts', 'list': 'posts', 'comments': 'post' }
	}
	_name = 'post'

	def _parse ( self, method, data ):
		if 'show' == method:
			return Post( self._version, **data )
		elif 'comments' == method:
			comments = []
			for comment in data['comments']:
				comments.append( Comment( self._version, **comment ) )
			return comments

	def __call__ ( self, **kwargs ):
		# Intercept argument-less calls and add arguments if needed
		postid = getattr( self, 'id', None )
		tinyid = getattr( self, 'tiny_id', None )
		if postid or tinyid:
			if 'id' not in kwargs and 'tiny_id' not in kwargs:
				if postid:
					kwargs['id'] = postid
				elif userid:
					kwargs['tiny_id'] = tinyid
		return ForrstObject.__call__( self, **kwargs )

class Snap ( Post ):
	_name = 'snap'

class Link ( Post ):
	_name = 'link'

class Code ( Post ):
	_name = 'code'

class Question ( Post ):
	_name = 'question'

class Comment ( ForrstObject ):
	_name = 'comment'

