from unittest import TestCase
from io import BytesIO

import msgspec
from django.conf import settings
from rest_framework.exceptions import ErrorDetail

settings.configure()

from drf_msgspec_json.parsers import MsgspecJSONParser
from drf_msgspec_json.renderers import MsgspecJSONRenderer


class MsgspecJSONRendererTests(TestCase):
    def setUp(self):
        self.renderer = MsgspecJSONRenderer()
        self.data = {
            'a': [1, 2, 3],
            'b': True,
            'c': 1.23,
            'd': 'test',
            'e': {'foo': 'bar'},
        }

    def test_basic_data_structures_rendered_correctly(self):
        rendered = self.renderer.render(self.data)
        reloaded = msgspec.json.decode(rendered)

        self.assertEqual(reloaded, self.data)

    def test_renderer_works_correctly_when_media_type_and_context_provided(self):
        rendered = self.renderer.render(
            data=self.data,
            media_type='application/json',
            renderer_context={},
        )
        reloaded = msgspec.json.decode(rendered)

        self.assertEqual(reloaded, self.data)

    def test_objects_render(self):
        data = {'error': ErrorDetail('detail')}
        rendered = self.renderer.render(data)
        self.assertEqual(b'{"error":"detail"}', rendered)


class MsgspecParserTests(TestCase):
    def setUp(self):
        self.parser = MsgspecJSONParser()
        self.data = {
            'a': [1, 2, 3],
            'b': True,
            'c': 1.23,
            'd': 'test',
            'e': {'foo': 'bar'},
        }

    def test_basic_data_structures_parsed_correctly(self):
        encoded = msgspec.json.encode(self.data)
        parsed = self.parser.parse(BytesIO(encoded))

        self.assertEqual(parsed, self.data)

    def test_parser_works_correctly_when_media_type_and_context_provided(self):
        encoded = msgspec.json.encode(self.data)
        parsed = self.parser.parse(
            stream=BytesIO(encoded),
            media_type='application/json',
            parser_context={},
        )

        self.assertEqual(parsed, self.data)
