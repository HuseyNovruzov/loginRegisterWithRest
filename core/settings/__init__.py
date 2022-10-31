try:
    from .local_settings import *

    live = False
except ImportError:
    live = True

if live:
    from .prodduction import *