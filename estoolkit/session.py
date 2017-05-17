# coding: utf-8

import re


class SessionException(Exception):
    pass


class Session(object):
    """Elasticsearch session
    """
    session_re = re.compile(
        r'^(?P<protocol>https?)://(?P<host>([a-z0-9-_])+(\.[a-z0-9-_]+){0,})(:(?P<port>\d{1,5}))?$'
    )

    def __init__(self, protocol, host, port=None):
        """Constructor.

        Args:
            protocol (str): http or https
            host (str): hostname
            port (int): port number
        """
        self.protocol = protocol
        self.host = host
        if port is None:
            port = 9200
        self.port = port

    @classmethod
    def from_string(cls, session_as_string):
        """Parse a string and create a session

        Args:
            cls (class): Session class
            session_as_string (str): string to parse

        Returns:
            Session: Session instance with parsed data

        Raises:
            SessionException
        """
        session_as_string = session_as_string.strip()

        m = cls.session_re.match(session_as_string)
        if m is None:
            raise SessionException("string does not match a session")
        else:
            port = None
            if m.group('port'):
                port = int(m.group('port'))
            return cls(m.group('protocol'), m.group('host'), port)

    def __str__(self):
        """
        """
        return "{}://{}:{}".format(self.protocol, self.host, self.port)
