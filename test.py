import unittest

from logReader import ip_grabber, url_grabber, line_splitter, dict_sorter


class TestGrabber(unittest.TestCase):
    
    def test_ip_grabber_success(self):
        """
        Test that an ip is grabbed and that the grabbed ip contains only numbers and periods and is returned as an object with a counter value
        """
        data = """177.71.128.21"""
        result = ip_grabber(data, {})
        self.assertEqual(result, {'177.71.128.21': 1})

    def test_ip_grabber_failure(self):
        """
        Test that when an ip is grabbed and any character is not equal to either a number or period it will return invalid line
        """
        data = """177.A1.128.21"""
        result = ip_grabber(data, {})
        self.assertEqual(result, "Invalid_Line")

    def test_url_grabber_success(self):
        """
        Test that a url is grabbed and that the first character is either a '/' or 'h' and is returned as an object with a counter value
        """
        data = """/intranet-analytics/"""
        result = url_grabber(data, {})
        self.assertEqual(result, {'/intranet-analytics/': 1})

    def test_url_grabber_failure(self):
        """
        Test that an a url is grabbed and the first character does not equal a '/' or a 'h' the function will return nothing
        """
        data = """\intranet-analytics/"""
        result = url_grabber(data, {})
        self.assertEqual(result, "Invalid_Line")


    def test_line_splitter_failure(self):
        """
        Test that when a line is passed in that fails the first check "Invalid_Line" will be returned
        """
        data = """177.71.128.21 - - [10/Jul/2018:22:21:28 +0200] "-" "GET /intranet-analytics/ HTTP/1.1" 200 3574 "-" "Mozilla/5.0 (X11; U; Linux x86_64; fr-FR) AppleWebKit/534.7 (KHTML, like Gecko) Epiphany/2.30.6 Safari/534.7\""""
        result = line_splitter(data)
        self.assertEqual(result, "Invalid_Line")


    def test_dict_sorter_success(self):
        """
        Test for the dictionary sorter function that sorts the log into the top 3 most active ip addresses 
        and in the case of a tie for 3rd place will extend the array to include those elements
        """
        data = """177.71.128.21 - - [10/Jul/2018:22:21:28 +0200] "-" "GET /intranet-analytics/ HTTP/1.1" 200 3574 "-" "Mozilla/5.0 (X11; U; Linux x86_64; fr-FR) AppleWebKit/534.7 (KHTML, like Gecko) Epiphany/2.30.6 Safari/534.7\""""
        result = dict_sorter({'168.41.191.40': 12, '177.71.128.21': 7, '50.112.00.11': 6, '168.41.191.34': 6, '168.41.191.43': 6, '72.44.32.10': 6, '168.41.191.41': 6, '168.41.191.9': 1, '50.112.00.28': 1, '72.44.32.11': 1, '79.125.00.21': 1})
        self.assertEqual(result, {'168.41.191.40': 12, '177.71.128.21': 7, '50.112.00.11': 6, '168.41.191.34': 6, '168.41.191.43': 6, '72.44.32.10': 6, '168.41.191.41': 6})

if __name__ == '__main__':
    unittest.main()
