# coding: utf-8
"""
"""
import sys
import os
import logging

from collections import OrderedDict

from pprint import pprint as pp

logging.basicConfig(level=logging.DEBUG)


class CatApi(object):
    def __init__(self):
        """Constructor.
        """
        self.query_params = OrderedDict({
            'pretty': None,
            'v': None,
            'help': None,
            'h': None,
            'format': ['json', 'smile', 'ymal', 'cbor'],
            's': '',
            'time': ['d', 'h', 'm', 's', 'ms', 'micros', 'nano'],
            'bytes': ['b', 'kb', 'mb', 'gb', 'tb', 'pb'],

        })

    def loaf_definition(self):
        """
        """

    def get_part(self, method, num_part, prefix, previous_parts):
        """
        """
        if method != "GET":
            return None

        if num_part == 0:
            name = "_cat"
            if name.startswith(prefix) or prefix == "":
                return {
                    "value": self.get_name(),
                    "help": "cat API",
                    "query_params": [],
                    "method": ["GET"]
                }
        elif num_part == 1:
            self.get_sub_command(prefix),

        return None

    def get_name(self):
        return '_cat'

    def get_sub_command(self):
        """
        """
        return [
            {
                "help": "aliases information",
                "value": "aliases",
                "next": self.get_alias_name,
                "query_params": {}
            },
            "allocation",
            "count",
            "fielddata",
            "health",
            "indices",
            "master",
            "nodeattrs",
            "nodes",
            "pending tasks",
            "plugins",
            "recovery",
            "repositories",
            "thread pool",
            "shards",
            "segments",
            "snapshots",
            "templates",
        ]








