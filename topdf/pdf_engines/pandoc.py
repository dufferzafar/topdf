
import os
import pypandoc

_formats = ["docx", "epub", "html", "json",
            "tex", "md", "opml", "rst"]


class PandocEngine():

    """ Uses pandoc to convert . """

    @staticmethod
    def can_handle(file_ext):
        return file_ext[1:] in _formats

    @staticmethod
    def make_pdf(path):
        file_name, file_ext = os.path.splitext(os.path.basename(path))
        return pypandoc.convert(
            path,
            to='pdf',
            outputfile=file_name + ".pdf",
            extra_args=[
                "--toc",
                "--latex-engine", "xelatex",
            ]
        )
