import os

from topdf.pdf_engines.pandoc import PandocEngine


class LocalFileHandler():

    """ Handles paths to local files. """

    @staticmethod
    def can_handle(path):
        return os.path.isfile(path)

    @staticmethod
    def make_pdf(path):
        file_name, file_ext = os.path.splitext(os.path.basename(path))

        if PandocEngine.can_handle(file_ext):
            PandocEngine.make_pdf(path)
