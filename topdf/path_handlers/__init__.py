from topdf.path_handlers.base import BaseHandler

import topdf.path_handlers.generic_url
import topdf.path_handlers.github_readme
import topdf.path_handlers.local_file
import topdf.path_handlers.reddit
import topdf.path_handlers.stackoverflow


def list_handlers():
    return BaseHandler.__subclasses__()


if __name__ == '__main__':
    print(list_handlers())
