
import os
import pypandoc

_formats = ["docx", "epub", "html", "json",
            "tex", "md", "opml", "rst"]


class PandocEngine():

    """ Uses pandoc to convert . """

    @staticmethod
    def can_handle(path):
        return path.endswith(tuple(_formats))

    @staticmethod
    def make_pdf(path, format=None, outputfile=None):
        if not outputfile:
            file_name, file_ext = os.path.splitext(os.path.basename(path))
            outputfile = file_name + ".pdf",

        return pypandoc.convert(
            path,
            format=format,
            to='pdf',
            outputfile=outputfile,
            extra_args=[
                "--toc",
                "--latex-engine", "xelatex",
            ]
        )
