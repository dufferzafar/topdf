import re
import requests

from topdf.path_handlers.base import BaseHandler


class GithubReadme(BaseHandler):

    """Uses gitprint website to convert github readmes to pdfs."""

    GP_URL = "https://gitprint.com/%s?download"

    GH_REGEX = re.compile(r"https:\/\/github\.com\/(.*\.md)$")

    valid_formats = ["md"]

    @classmethod
    def can_handle(cls, url):
        return bool(re.match(cls.GH_REGEX, url))

    @classmethod
    def make_pdf(cls, url):

        m = re.match(cls.GH_REGEX, url)
        file_name = m.group(1).replace("/", "-") + ".pdf"

        r = requests.get(cls.GP_URL % m.group(1), stream=True)
        with open(file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)

        return file_name
