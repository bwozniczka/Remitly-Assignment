from unittest import TestCase
from json_validator import JsonValidator


class CorrectOutput(TestCase):
    def test_is_JsonValidator_return_correct_output(self):
        self.assertFalse(JsonValidator("resources/false_file.json"))

    def test_is_JsonValidator_return_correct_output1(self):
        self.assertTrue(JsonValidator("resources/true_file1.json"))

    def test_is_JsonValidator_return_correct_output2(self):
        self.assertTrue(JsonValidator("resources/true_file2.json"))


class PolicyNameTest(TestCase):
    def test_incorrect_PolicyName_regex_mismatch(self):
        self.assertRaises(Exception, JsonValidator, "resources/incorrect_PolicyName1.json")

    def test_incorrect_PolicyName_is_empty(self):
        self.assertRaises(Exception, JsonValidator, "resources/incorrect_PolicyName2.json")

    def test_incorrect_PolicyName_is_int(self):
        self.assertRaises(Exception, JsonValidator, "resources/incorrect_PolicyName3.json")

    def test_incorrect_PolicyName_is_too_long(self):
        self.assertRaises(Exception, JsonValidator, "resources/incorrect_PolicyName4.json")


class PolicyDocumentTest(TestCase):
    def test_incorrect_Policy_Document_is_empty(self):
        self.assertRaises(Exception, JsonValidator, "resources/incorrect_PolicyDocument.json")

    def test_version_in_Policy_Document_is_undefined(self):
        self.assertRaises(Exception, JsonValidator, "resources/incorrect_PolicyDocument2.json")

    def test_statement_in_Policy_Document_is_undefined(self):
        self.assertRaises(Exception, JsonValidator, "resources/incorrect_PolicyDocument3.json")

    def test_statement_in_Policy_Document_is_not_array(self):
        self.assertRaises(Exception, JsonValidator, "resources/incorrect_PolicyDocument4.json")

    def test_statement_in_Policy_Document_is_empty(self):
        self.assertRaises(Exception, JsonValidator, "resources/incorrect_PolicyDocument5.json")


class JsonFileTest(TestCase):
    def test_is_json_file_valid(self):
        self.assertTrue(JsonValidator("resources/true_file1.json"))

    def test_is_json_file_invalid(self):
        self.assertRaises(Exception, JsonValidator, "resources/invalid_json.json")
