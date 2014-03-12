import unittest

from nose.tools import raises

from fedora.client import AuthError
from bodhi.client import BodhiClient

BASE_URL = 'http://127.0.0.1:6543'


class TestBodhiClient(unittest.TestCase):

    def setUp(self):
        self.client = BodhiClient(BASE_URL, openid_insecure=True)
        # TODO: fire up bodhi wsgi app

    @raises(AuthError)
    def test_failed_login(self):
        self.client.login('test', 'test')

    def test_query(self):
        self.client.query(status='testing')
