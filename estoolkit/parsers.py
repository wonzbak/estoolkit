# coding: utf-8

"""Parsers for completion and hightlighting
"""
import sys
from pyparsing import (
    alphanums, Word, Literal, Optional, oneOf, OneOrMore, Group,
    delimitedList, ParseException
)


class Parser(object):
    """
    """

    def parse(self, input_str):
        return self.expr.parseString(input_str)


class EsParser(Parser):
    """
    """

    def __init__(self):
        """Constructor.
        """
        char_index = alphanums + '+-*'
        index = Word(char_index)
        indices = delimitedList(index, delim=',')
        self.es_indices = indices('indices')


class EsCatCommand(Parser):
    """
    """

    def __init__(self):
        """Constructor.
        """
        es_sub_commands = [
            'aliases',
            'allocation',
            {'name': 'count', 'query': ['index', 'type']},
            {'name': 'fielddata', 'params': [{'name': 'fields', 'values': 'ES_FIELDS'}]}
        ]


        slash = Literal('/').suppress()
        cmd = Word('_cat')

        sub_cmds = [
            Literal('aliases'),
            Literal('count'),
            Literal('fielddata')
        ]

        self.expr = slash + cmd('cmd') + slash + ()


def main():
    """Main entry point.
    """
    from pprint import pprint as pp
    # p = EsCatCommand()
    # r = p.parse('/_cat/aliases')

    string = 'index1, index2'
    if len(sys.argv) > 1:
        string = sys.argv[1]

    es_parser = EsParser()

    pp(es_parser.es_indices.parseString(string))


if __name__ == '__main__':
    main()
