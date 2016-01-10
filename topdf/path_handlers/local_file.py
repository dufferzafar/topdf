import os

from topdf.pdf_engines.pandoc import PandocEngine
from topdf.pdf_engines.libreoffice import LibreOfficeEngine


class LocalFileHandler():

    """ Handles paths to local files. """

    @staticmethod
    def can_handle(path):
        return os.path.isfile(path)

    @staticmethod
    def make_pdf(path):
        if PandocEngine.can_handle(path):
            return PandocEngine.make_pdf(path)
        elif LibreOfficeEngine.can_handle(path):
            return LibreOfficeEngine.make_pdf(path)
