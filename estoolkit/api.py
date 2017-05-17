# coding: utf-8

"""Represent es api
"""
import logging
import json
from pathlib import Path

logger = logging.getLogger('es_api')


class EsApiError(Exception):
    pass


class EsApi(object):
    """
    """

    def __init__(self, resources_folder):
        """Constructor.

        Args:
            resources_folder (str): json api file directory
        """
        self.api = None
        self.base_path = resources_folder

    def load_api(self, resources_folder=None):
        """Load api definitions files recursivey.

        Args:
            resources_folder(str) : folder name of api difinition
        """
        if resources_folder is None:
            resources_folder = self.base_path

        base_path = Path(resources_folder)
        if not base_path.exists():
            raise EsApiError("resource api directory not found '{}'".format(base_path))

        verbs_filename = base_path / 'verbs.json'
        verbs = self.load_api_file(verbs_filename)

        # load resource command
        for i, verb in enumerate(verbs['verbs']):
            for j, command in enumerate(verb['commands']):
                if 'resource' in command:
                    resource_file = base_path / command['resource']
                    cmd = self.load_api_file(resource_file)
                    new_cmd = cmd['command'].copy()
                    new_cmd.update(command)
                    #  new_cmd = {**command, **cmd['command']}  python 3.5 way
                    verbs['verbs'][i]['commands'][j] = new_cmd

                break

        self.api = verbs

    def load_api_file(self, filename):
        """Loads api definition from file.

        Args:
            filename(Path): filename of resource

        Returns:
            dict: Description of api

        Raises:
            EsApiError
        """
        api_definiton = None

        if not filename.exists():
            raise EsApiError("resource {} not found in '{}'".format(filename, 'base'))

        try:
            with open(str(filename)) as f:
                api_definiton = json.load(f)
                logger.debug("load api definiton of {}".format(filename))
        except Exception as e:
            logger.exception(e)
            raise EsApiError("unable to deserialise '{}'".format(filename))

        return api_definiton

    def get_verbs(self, prefix=""):
        """Get list of commands.

        Args:
            prefix(str): if given, filters commands that starts with prefix

        Returns:
            list: list of available commands
        """
        if len(prefix) > 0:
            return [
                verbs['name']
                for verbs in self.api['verbs']
                if verbs['name'].startswith(prefix)
            ]

        return [verbs['name'] for verbs in self.api['verbs']]

    def get_commands(self, verb_name, prefix=""):
        """
        """
        if verb_name not in self.get_verbs():
            return []

        for verb in self.api['verbs']:
            if verb_name == verb['name']:
                for command in verb['commands']:
                    print(command['name'])


def main():
    """Main entry point.
    """

    api = EsApi('estoolkit/api')
    api.load_api()

    print(api.get_verbs())
    print(api.get_commands('GET'))


if __name__ == '__main__':
    main()
