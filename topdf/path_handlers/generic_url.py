import urllib.parse

from topdf.path_handlers.base import BaseHandler
from topdf.pdf_engines.pandoc import PandocEngine


class GenericURL(BaseHandler):

    """ Handles any arbitrary URL. """

    # Minimum priority so that all other handlers get matched first.
    priority = -1

    @classmethod
    def can_handle(cls, path):
        parsed = urllib.parse.urlsplit(path)
        return parsed.scheme.startswith("http")

    @classmethod
    def make_pdf(cls, path):
        return PandocEngine.make_pdf(path)
