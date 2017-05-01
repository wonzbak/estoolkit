# coding: utf-8

"""Es commands
"""
import requests


class EsCommands(object):
    """All elasticsearch interaction
    """

    def init(self, protocol=None, host=None, port=None, session=None, options=None):
        """Constructor
        """
        self.options = options

        if session is not None:
            self.protocol = session.protocol
            self.host = session.host
            self.port = session.port
        else:
            self.protocol = protocol
            self.host = host
            self.port = port

    def command(verb, path, options=None):
        """Execute command
        """
