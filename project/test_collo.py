import collo
import unittest


class ColloTestCase(unittest.TestCase):

    def setUp(self):
        collo.app.config['TESTING'] = True
        self.app = collo.app.test_client()

    def test_index_200(self):
        rv = self.app.get('/')
        self.assertEqual(200, rv._status_code)

    def test_index_uses_template(self):
        rv = self.app.get('/')
        assert b'<html lang="pt-br">' in rv.data

if __name__ == '__main__':
    unittest.main()

