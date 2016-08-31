"""Defines the abstract interface of a Path Handler."""

import abc


class BaseHandler(object):

    # This allows us to create an order in which handlers are matched.
    priority = 1

    @abc.abstractmethod
    def can_handle(cls, path):
        """
        Check whether or not this handler can handle the path.

        return: boolean
        """
        return

    @abc.abstractmethod
    def make_pdf(cls, path):
        """
        Convert the path (which could be a file or url) to a local pdf.

        return: path to the pdf created.
        """
        return
