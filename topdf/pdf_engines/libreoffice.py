
import os
import subprocess

_formats = ["ppt", "pptx", "doc", "docx"]


class LibreOfficeEngine():

    """ Uses libreoffice to convert files to pdfs. """

    @staticmethod
    def can_handle(path):
        return path.endswith(tuple(_formats))

    @staticmethod
    def make_pdf(path):
        command = ["libreoffice", "--headless", "--convert-to", "pdf", path]
        subprocess.call(command)

        file_name, file_ext = os.path.splitext(os.path.basename(path))
        return file_name + ".pdf"
