# -*- coding: utf-8 -*-

import RainForrst

# The argument here is the API version
api = RainForrst.Forrst( 1 )

# Query through the API to get a user object
jmhobbs = api.user.info( username='jmhobbs' )
print "John's ID:", jmhobbs.id

# Directly instantiate a user object
kyle = RainForrst.objects.User( 1, username='kyle' )
print "Kyle's Posts:\n"
# You can now run functions directly on objects
for post in kyle.posts():
	print '"%s"\n' % post.page_title.strip()