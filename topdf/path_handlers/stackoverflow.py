import os
import re
from tempfile import NamedTemporaryFile

import requests

from topdf.path_handlers.base import BaseHandler
from topdf.pdf_engines.pandoc import PandocEngine


class StackOverflowAnswer(BaseHandler):

    """Handles urls to stackoverflow answers."""

    API_URL = ("https://api.stackexchange.com/2.2/answers/%s"
               "?site=%s&filter=!GeEyUcJFJeD0Q")

    # TODO: Add support for other StackExchange sites
    SO_REGEX = re.compile(r"https?:\/\/(stackoverflow)\.com\/a\/(\d+)")

    @classmethod
    def can_handle(cls, url):
        return bool(re.match(cls.SO_REGEX, url))

    @classmethod
    def make_pdf(cls, url):
        """Fetches raw markdown of an answer and convert it to PDF."""

        m = re.match(cls.SO_REGEX, url)
        response = requests.get(cls.API_URL % (m.group(2), m.group(1)))
        body = response.json()["items"][0]["body_markdown"]

        with NamedTemporaryFile(prefix='topdf_so_', delete=False,
                                mode='wt') as mdfile:
            mdfile.write(body)

        # TODO: Could just invoke a MD to PDF converter here?
        # Now that we have a markdown file

        outputfile = 'StackOverflow - %s.pdf' % m.group(2)
        try:
            PandocEngine.make_pdf(
                path=mdfile.name,
                format='commonmark',
                outputfile=outputfile,
            )
        except:
            print("Fix the markdown file and try again: %s" % mdfile.name)
            raise
        else:
            os.remove(mdfile.name)
            return outputfile


if __name__ == '__main__':
    url = "https://stackoverflow.com/a/15927037/2043048"
    StackOverflowAnswer.make_pdf(url)
