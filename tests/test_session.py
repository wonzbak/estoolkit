# coding: utf-8

"""Test session
"""
import unittest
import pytest

from estoolkit.session import Session, SessionException


class Test_Session(unittest.TestCase):
    """
    """

    def test___init__(self):
        session = Session('http', 'domain')
        assert 'domain' == session.host
        assert 'http' == session.protocol
        assert session.port == 9200

        session = Session('https', 'domain', 9201)
        assert 'https' == session.protocol
        assert 'domain' == session.host
        assert session.port == 9201

    def test_from_string(self):
        session = Session.from_string('http://my-domain')
        assert 'http' == session.protocol
        assert 'my-domain' == session.host
        assert session.port == 9200

        session = Session.from_string('http://my-domain.tld')
        assert 'http' == session.protocol
        assert 'my-domain.tld' == session.host
        assert session.port == 9200

        session = Session.from_string('https://my.sub.domain.tld')
        assert 'https' == session.protocol
        assert 'my.sub.domain.tld' == session.host
        assert session.port == 9200

        session = Session.from_string('     http://striped-domain.tld  ')
        assert 'http' == session.protocol
        assert 'striped-domain.tld' == session.host
        assert session.port == 9200

        with pytest.raises(SessionException) as excinfo:
            session = Session.from_string('htps://bad_protocol')
        assert 'string does not match a session' in str(excinfo.value)

        with pytest.raises(SessionException) as excinfo:
            session = Session.from_string('htps://bad_domain.')
        assert 'string does not match a session' in str(excinfo.value)

        with pytest.raises(SessionException) as excinfo:
            session = Session.from_string('htps://bad_port:3a3')
        assert 'string does not match a session' in str(excinfo.value)
