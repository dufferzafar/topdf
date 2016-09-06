import os
import subprocess


# Based on pypandoc's '_convert_input' function
def pandoc(source, dest, format=None):
    # _ensure_pandoc_path()

    args = ["pandoc", source]

    if format:
        args.extend(["--from="+format])

    args.extend([
        "--to=latex",
        "--output="+dest,
        "--toc",
        "--latex-engine", "xelatex",
    ])

    # print(" ".join(args))
    subprocess.call(args)

    return dest


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

        return pandoc(path, outputfile, format)
