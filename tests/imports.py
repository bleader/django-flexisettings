import unittest2
import sys
import os

from tests.base import BaseTestCase


class ImportTestCase(BaseTestCase):

    def test_import_without_env(self):
        """Test importing flexisettings without setting environment
        variable FLEXI_WRAPPED_MODULE
        """
        try:
            import flexisettings.settings
        except ImportError, e:
            if "Flexisettings cannot be imported, because env" in str(e):
                pass
            else:
                raise
        except:
            raise
        else:
            self.fail(
                "No 'ImportError' exception when FLEXI_WRAPPED_MODULE not set"
            )

    def test_import(self):
        """Test importing flexisettings with environment variable set"""
        os.environ.setdefault(self.envvar,
            "%s.settings" % self.test_project)
        try:
            import flexisettings.settings
        except:
            self.fail(sys.exc_info()[1])

    def test_import_local(self):
        """Check if local settings was imported"""
        import flexisettings.settings
        self.assertIn(
            '.'.join([self.test_project, 'settings_t']),
            flexisettings.settings._wrapped_modules
        )

def suite():
    # it is necessary to run those tests in that order to avoid
    # namespace pollution with imported module
    tests = ['test_import_without_env', 'test_import', 'test_import_local']
    return unittest2.TestSuite(map(ImportTestCase, tests))

if __name__ == "__main__":
    runner = unittest2.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)