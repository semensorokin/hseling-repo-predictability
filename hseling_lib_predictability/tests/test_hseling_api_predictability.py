import unittest

import hseling_api_predictability


class HSELing_API_PredictabilityTestCase(unittest.TestCase):

    def setUp(self):
        self.app = hseling_api_predictability.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertIn('Welcome to hseling_api_Predictability', rv.data.decode())


if __name__ == '__main__':
    unittest.main()
