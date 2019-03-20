from django.test import TestCase
import sys, os
os.environ['DJANGO_SETTINGS_MODULE'] = 'taxpaas.settings'


class PreprocessingTest(TestCase):
    NOT_IMPLEMENTED = "The Test is not implemented"

    def test_w2(self):
        # self.fail(self.NOT_IMPLEMENTED)
        pass

    def test_1099_G(self):
        self.fail(self.NOT_IMPLEMENTED)

    def test(self):
        assert(1 == 2)