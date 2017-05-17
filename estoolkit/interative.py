# coding: utf-8
"""
"""
import sys
import os
import logging
from pprint import pprint as pp

from prompt_toolkit import prompt
from prompt_toolkit.token import Token

from estoolkit.completer import EsToolkitCompleter
from estoolkit.style import style
from estoolkit.lexer import LexerFactory

logger = logging.getLogger('intearactive_app')


class BreakInteractiveLoop(Exception):
    """Exit application
    """


class EstoolkitInteractiveApplication(object):

    def __init__(self):
        """Constructor.
        """
        # es session
        self.session = None
        self.prompt = "> "
        self.completer = EsToolkitCompleter()
        self.style = style
        self.lexer = LexerFactory()

    def app_loop(self):
        """Enter interactive application loop.
        """
        logging.debug("enter interactive loop")
        while True:
            try:
                input_ = prompt(
                    self.prompt,
                    completer=self.completer,
                    lexer=self.lexer,
                    get_bottom_toolbar_tokens=self.get_bottom_toolbar_tokens,
                    # get_prompt_tokens=get_prompt_tokens,
                    style=style
                )
                logger.debug("input '{}'".format(input_))
                self.process_input(input_)
            except (EOFError, BreakInteractiveLoop):
                break

        self.exit()

    def get_bottom_toolbar_tokens(self, cli):
        """Get tokens f toolbar

        Args:
            cli (CommandLineInterface): cli intances

        Returns:
            List: list of tupple token and name
        """
        if self.session is None:
            session_msg = 'session: no session'
        else:
            session_msg = str(self.session)

        return [(Token.Toolbar, session_msg)]

    def process_input(self, input_):
        """Do somthing with input
        """
        input_ = input_.strip()
        logger.info("process input '{}'".format(input_))
        if "exit" == input_:
            raise BreakInteractiveLoop()

    def exit(self):
        """Exit application.
        """
        print("bye")


def main():
    """Main entry point.
    """
    app = EstoolkitInteractiveApplication()
    app.app_loop()


if __name__ == '__main__':
    main()
