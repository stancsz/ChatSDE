import unittest
from ChatSDE.assistant_api import OpenAIAssistant

class TestOpenAIAssistantManager(unittest.TestCase):

    def setUp(self):
        # Set up with a dummy API key for testing
        self.manager = OpenAIAssistant(api_key="dummy_key")

    def test_initialization(self):
        # Test initialization with an API key
        self.assertEqual(self.manager.api_key, "dummy_key")

    def test_load_yaml_config(self):
        # Test loading a YAML config
        # You should have a valid YAML file for testing this method
        yaml_path = "assistant.yml"
        config = self.manager.load_yaml_config(yaml_path)
        self.assertIsNotNone(config)

    def test_create_assistant_from_yaml(self):
        # Test creating an assistant from a YAML file
        # Ensure you have a valid YAML file and the necessary setup to create an assistant
        yaml_path = "assistant.yml"
        assistant = self.manager.create_assistant_from_yaml(yaml_path)
        self.assertIsNotNone(assistant)

if __name__ == '__main__':
    unittest.main()
