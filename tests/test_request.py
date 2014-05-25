import unittest
import gulper.request


class TestRequest(unittest.TestCase):
    def test_request(self):
        request = gulper.request.Request('somepath', client_id='client_id', api_key='api_key')
        for element in ('somepath', 'client_id=client_id', 'api_key=api_key'):
            self.assertTrue(element in request.rq)


if __name__ == '__main__':
    unittest.main()
