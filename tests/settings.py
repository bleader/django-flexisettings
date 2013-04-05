import unittest2
from tests.base import BaseTestCase
import os

class SettingsTestCase(BaseTestCase):

    run_envvar = 'FLEXI_RUN_ENV'
    secret_key = 'adummysecretkey'

    def setUp(self):
        super(SettingsTestCase, self).setUp()
        os.environ.setdefault(self.envvar,
            "%s.settings" % self.test_project)

    def test_run_env(self):
        """Test running environment lookup"""
        import flexisettings.settings
        self.assertEqual(flexisettings.settings.FLEXI_RUN_ENV, None)

    def test_debug_settings(self):
        """Test proxyfied lookup without evaluation (settings.DEBUG)"""
        import flexisettings.settings
        self.assertTrue(flexisettings.settings.DEBUG)

    def test_security_settings(self):
        """Test proxyfied lookup with evaluation (settings.SECRET_KEY)"""
        import flexisettings.settings
        self.assertEqual(flexisettings.settings.SECRET_KEY, self.secret_key)

if __name__ == '__main__':
    unittest2.main()