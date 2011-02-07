# REALLY REALLY IMPORTANT NOTE #

Forrst has removed their API.  Until such time as they replace it, this module is useless.

Sorry.

# RainForrst

RainForrst is a quick little file to access the [Forrst API](http://forrst.com/apidocs.html).

# Usage

    import RainForrst

    api = RainForrst.Forrst( 1 ) # The argument here is the API version

    # Query through the API to get a user object
    jmhobbs = api.user.info( username='jmhobbs' )
    print "John's ID:", jmhobbs.id

    # Directly create a user object
    kyle = RainForrst.objects.User( 1, username='kyle' )
    print "Kyle's Posts:\n"
    for post in kyle.posts():
      print '"%s"\n' % post.page_title.strip()

Would print something like this:

    John's ID: 3199
    Kyle's Posts:

    "Keith whipped up this really simple FAQ design. I'm digging the typography, how about you? It's all built using 960.gs, too."

    ...

    "Which JQuery Rich Text Editor plugin(s) would you recommend?"


All API calls will either return a response object or raise an exception.

# Testing

RainForrst is in flux at the moment (like the Forrst API) so it has minimal test suites.

You can run what it has with nose.

    $ cd RainForrst
    $ nosetests
    ..
    ----------------------------------------------------------------------
    Ran 2 tests in 0.454s

    OK
    $

# Installation

    $ python setup.py install
