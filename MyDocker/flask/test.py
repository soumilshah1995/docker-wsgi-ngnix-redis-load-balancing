try:
    from run import app
    import unittest

except Exception as e:
    print("Some Modules are  Missing {} ".format(e))


class FlaskTestCase(unittest.TestCase):

    # Check if Response is 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/fo")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # check if content return is application/json
    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get("/fo")
        self.assertEqual(response.content_type, "application/json")

    # check for Data returned
    def test_index_data(self):
        tester = app.test_client(self)
        response = tester.get("/fo")
        self.assertTrue(b'Message' in response.data)


if __name__ == "__main__":
    unittest.main()