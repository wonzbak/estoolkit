# coding: utf-8

"""Lexers for estoolkit
"""
import logging

from prompt_toolkit.token import Token
from prompt_toolkit.layout.lexers import Lexer

logger = logging.getLogger('lexer')


class Lexer(Lexer):
    """Lexer for url
    """

    def __init__(self):
        """Constructor.
        """

    def lex_document(self, cli, document):
        """
        """
        logger.debug(document)
        lines = document.lines

        return self.lex_url

    def lex_setting():
        pass

    def lex_url(lineno):
        return [
            (Token.Protocol, 'http://'),
            (Token.Host, 'my-domain'),
            (Token.PortSep, ':'),
            (Token.Port, '9200'),
            (Token, '/path'),
        ]
