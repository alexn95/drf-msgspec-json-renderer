import msgspec
from django.conf import settings
from rest_framework.exceptions import ParseError
from rest_framework.parsers import BaseParser

__all__ = ['MsgspecJSONParser', ]


class MsgspecJSONParser(BaseParser):
    media_type = 'application/json'

    def parse(self, stream, media_type=None, parser_context=None):
        """
        Parses the incoming bytestream as JSON and returns the resulting data.
        """
        parser_context = parser_context or {}
        encoding = parser_context.get('encoding', settings.DEFAULT_CHARSET)

        try:
            data = stream.read().decode(encoding)
            return msgspec.json.decode(data)
        except msgspec.DecodeError as exc:
            raise ParseError(f'JSON parse error - {exc}')
