# -*- coding: utf-8 -*-

import RainForrst

# The argument here is the API version
api = RainForrst.Forrst( 2 )

# Query through the API to get a user object
jmhobbs = api.user.info( username='jmhobbs' )
print "John's ID:", jmhobbs.id

# Directly instantiate a user object
kyle = RainForrst.objects.User( 2, username='kyle' )
print "Kyle's Posts:\n"

# You can now run functions directly on objects
for post in kyle.posts():
	print '"%s"' % post.title.strip()

# Grab the last post (for discussion sake)
post_id = kyle.posts()[-1].tiny_id

# Get it's details
post = api.post.show( tiny_id=post_id )
print "Short ID: %s" % post.title.strip()

# Now try comments (breaks because Auth is disabled)
#for comment in post.comments():
#	print comment.body.strip()
