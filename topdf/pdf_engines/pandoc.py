import os
import subprocess

# Based on pypandoc's '_convert_input' function
def pandoc(source, dest, format=None):
    # _ensure_pandoc_path()

    args = ["pandoc", source]

    if format:
        args.extend(["--from=" + format])

    args.extend([
        "--to=latex",
        "--pdf-engine", "xelatex",
        # "--toc",
        "-V geometry:margin=0.1in",
        "-V documentclass=report",
        "--output=" + dest,
    ])

    print(" ".join(args))
    subprocess.call(args)

    return dest


class PandocEngine():

    """ Uses pandoc to convert . """

    valid_formats = ("docx", "epub", "html", "json",
                     "tex", "md", "opml", "rst")

    @classmethod
    def can_handle(cls, path):
        return path.endswith(cls.valid_formats)

    @classmethod
    def make_pdf(cls, path, outputfile=None, **kwargs):
        if not outputfile:
            file_name, file_ext = os.path.splitext(os.path.basename(path))
            outputfile = file_name + ".pdf"

        return pandoc(path, outputfile, **kwargs)
