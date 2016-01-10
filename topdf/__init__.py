from topdf.path_handlers import list_handlers


def topdf(path, open_pdf=False):
    handler = [hnd for name, hnd in list_handlers().items()
               if hnd.can_handle(path)]

    if len(handler) != 1:
        raise RuntimeError("No appropriate handler could be found"
                           " for path: %s" % path)

    pdf = handler[0].make_pdf(path)

    # Open the PDF file in associated viewer
    if open_pdf:
        import sys
        if sys.platform == 'linux':
            import subprocess
            subprocess.call(["xdg-open", pdf])
        else:
            import os
            os.startfile(pdf)
