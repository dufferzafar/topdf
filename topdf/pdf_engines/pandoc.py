import os
import pypandoc


class PandocEngine():

    """ Uses pandoc to convert . """

    valid_formats = ["docx", "epub", "html", "json",
                     "tex", "md", "opml", "rst"]

    @classmethod
    def can_handle(cls, path):
        return path.endswith(tuple(cls.valid_formats))

    @classmethod
    def make_pdf(cls, path, format=None, outputfile=None):
        if not outputfile:
            file_name, file_ext = os.path.splitext(os.path.basename(path))
            outputfile = file_name + ".pdf"

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
