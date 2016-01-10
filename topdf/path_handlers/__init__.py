from .local_file import LocalFileHandler


def list_handlers():
    """ Return a list of an instance of every supported provider. """

    return {
        name: klass()
        for name, klass in globals().items()
        if name.endswith('Handler')
    }


if __name__ == '__main__':
    print(list_handlers())
