# coding: utf-8
import logging

from prompt_toolkit.completion import Completer, Completion

logger = logging.getLogger('completion')


class EsToolkitCompleter(Completer):
    """ Provides completions
    """

    def __init__(self):
        """constructor
        """
        super().__init__()
        self.commands = [
            {"connect": "connect to a es server"},
            {"set": "define config parameter"},
            {"GET": "perform a HTTP get query"},
            {"DELETE": "perform a HTTP delete query"},
            {"PUT": "perform a HTTP put query"},
        ]

    def get_completions(self, document, complete_event):
        """Yields completions.
        """
        word_before_cursor = document.text_before_cursor
        for command in self.commands:
            cmd = list(command)[0]
            logger.debug("check command '{}'".format(cmd))
            if cmd.startswith(word_before_cursor):
                logger.info("command '{}'' completed".format(cmd))
                meta = list(command.values())[0]
                yield Completion(cmd, -len(word_before_cursor), display_meta=meta)
