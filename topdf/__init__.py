from topdf.path_handlers import list_handlers


def topdf(path, open_pdf=False):
    handlers = [h for h in list_handlers() if h.can_handle(path)]

    # TODO: Also notify user that multiple handlers were found
    if not handlers:
        raise RuntimeError("No appropriate handlers could be found"
                           " for path: %s" % path)

    # Pick the handler with highest priority (for now, atleast)
    handler = sorted(handlers, key=lambda h: h.priority)[-1]

    pdf = handler.make_pdf(path)

    # Open the PDF file in associated viewer
    if open_pdf:
        import sys
        if sys.platform == 'linux':
            import subprocess
            subprocess.call(["xdg-open", pdf])
        else:
            import os
            os.startfile(pdf)
