# Make sure that overriding __file__ doesn't change the traceback

import sys
m = sys.modules['__main__']
m.__file__ = "/dev/null"

a # not defined, should throw
