try:
    from {{app_name}}.version import __version__
except Exception, err:
    __version__ = '1.0.0'
