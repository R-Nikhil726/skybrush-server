"""Main package for the Flockwave server."""

from __future__ import absolute_import

from .app import app
from .version import __version__, __version_info__

__all__ = ("__version__", "__version_info__", "app")
