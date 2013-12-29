#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import logging
import getpass
from optparse import OptionParser

import sleekxmpp


# Python versions before 3.0 do not use UTF-8 encoding
# by default. To ensure that Unicode is handled properly
# throughout SleekXMPP, we will set the default encoding
# ourselves to UTF-8.
if sys.version_info < (3, 0):
    print 'Using Pre3: %s' % (sys.version_info)
    from sleekxmpp.util.misc_ops import setdefaultencoding
    setdefaultencoding('utf8')
else:
    raw_input = input


'''Here we will create out echo bot class'''

if __name__ == '__main__':
    '''Here we will configure and read command line options'''

    '''Here we will instantiate our echo bot'''

    '''Finally, we connect the bot and start listening for messages'''


