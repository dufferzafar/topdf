
import os
import subprocess


class LibreOfficeEngine():

    """ Uses libreoffice to convert files to pdfs. """

    valid_formats = ["ppt", "pptx", "doc", "docx"]

    @classmethod
    def can_handle(cls, path):
        return path.endswith(tuple(cls.valid_formats))

    @classmethod
    def make_pdf(cls, path):
        command = ["libreoffice", "--headless", "--convert-to", "pdf", path]

        with open(os.devnull, "w") as devnull:
            subprocess.call(command, stdout=devnull)

        file_name, file_ext = os.path.splitext(os.path.basename(path))
        return file_name + ".pdf"
