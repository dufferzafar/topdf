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
        file_name, file_ext = os.path.splitext(os.path.basename(path))

        if PandocEngine.can_handle(file_ext):
            return PandocEngine.make_pdf(path)
        elif LibreOfficeEngine.can_handle(file_ext):
            return LibreOfficeEngine.make_pdf(path)
