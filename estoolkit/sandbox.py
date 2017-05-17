# coding: utf-8

import os
import logging

from pygments.lexers import HtmlLexer
from prompt_toolkit import prompt
from prompt_toolkit.layout.lexers import PygmentsLexer

from prompt_toolkit.contrib.completers import WordCompleter
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.history import InMemoryHistory
from completer import EsToolkitCompleter

logging.basicConfig(
    filename="{}/{}".format(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'estoolkit.log'),
    level=logging.DEBUG
)

completer = WordCompleter(['set', 'connect', 'GET', 'PUT'])


class MyCustomCompleter(Completer):
    def get_completions(self, document, complete_event):
        logging.debug("text=%s", document.text)
        logging.debug("text_before_cursor=%s", document.text_before_cursor)
        yield Completion('completion', start_position=0)


def main():
    """
    """
    history = InMemoryHistory()
    while True:
        text = prompt(
            '> ',
            lexer=PygmentsLexer(HtmlLexer),
            completer=EsToolkitCompleter(),
            history=history
        )
        print('You said: %s' % text)


if __name__ == '__main__':
    main()
