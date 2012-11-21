from .settings import *
try:
    from .settings_local import *
except ImportError, exc:
    exc.args = ('cannot load settings_local.py')
    raise exc
