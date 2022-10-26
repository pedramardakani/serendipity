# Convert Python dictionary to XML
#
# Originally, this was written by Victor and Serik, I made a few changes -
# nothing drastic.
#
# Pedram Ashofteh-Ardakani <pedramardakani@pm.me>


import unittest
from dictionary_to_xml import convert


class TestCases(unittest.TestCase):

    def test_convert_one_item(self):
        self.assertEqual(
            convert({"key": "value"}),
            "<key>value</key>"
        )

    def test_convert_multiple_items(self):
        self.assertEqual(
            convert({
                "key": "value",
                "key-1": "value-1"
            }), "<key>value</key><key-1>value-1</key-1>"
        )

    def test_convert_one_item_with_nested_list(self):
        self.assertEqual(
            convert({"key": [1, 2, 3]}),
            "<key><item>1</item><item>2</item><item>3</item></key>"
        )

    def test_convert_multiple_items_with_nested_list(self):
        self.assertEqual(
            convert({"key": [1, 2], "key-1": ["a", "b", 30]}),
            "<key><item>1</item><item>2</item></key><key-1><item>a</item><item>b</item><item>30</item></key-1>"
        )

if __name__ == "__main__":
    unittest.main()
