from topdf.path_handlers import list_handlers


def topdf(path):
    handler = [hnd for name, hnd in list_handlers().items()
               if hnd.can_handle(path)]

    if len(handler) != 1:
        raise RuntimeError("No appropriate handler could be found"
                           " for path: %s" % path)

    handler[0].make_pdf(path)
