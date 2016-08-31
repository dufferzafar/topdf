import os

from topdf.path_handlers.base import BaseHandler
from topdf.pdf_engines.pandoc import PandocEngine
from topdf.pdf_engines.libreoffice import LibreOfficeEngine


class LocalFile(BaseHandler):

    """ Handles paths to local files. """

    @classmethod
    def can_handle(cls, path):
        return os.path.isfile(path)

    @classmethod
    def make_pdf(cls, path):
        if PandocEngine.can_handle(path):
            return PandocEngine.make_pdf(path)
        elif LibreOfficeEngine.can_handle(path):
            return LibreOfficeEngine.make_pdf(path)
