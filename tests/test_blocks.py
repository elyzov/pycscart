import requests_mock
import json
import unittest
from pycscart import CSCartClient
from pycscart import entities


@requests_mock.Mocker()
class BlockTestCase(unittest.TestCase):

    TEST_URL = 'http://example.com'
    TEST_BRAND = 'CS-Cart'
    TEST_VERSION = '4.4.1'

    def setUp(self):
        self.mock_client = CSCartClient(
            self.TEST_URL, brand=self.TEST_BRAND, version=self.TEST_VERSION
        )

    def test_get_block(self, m):
        fake_block_id = 38

        with open('tests/resources/get_block.json') as data:
            m.get('/api/blocks/%s' % fake_block_id, json=json.load(data))

            actual = self.mock_client.get_block(fake_block_id)
            expected = entities.CSCartBlock(
                block_id=str(fake_block_id),
                type="template",
                properties={
                    "template": "blocks/static_templates/404.tpl"
                },
                company_id="1",
                lang_code="en",
                name="404",
                content=""
            )

            assert actual == expected
