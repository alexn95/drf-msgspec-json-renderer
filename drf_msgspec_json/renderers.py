import uuid
from decimal import Decimal
from typing import Any

import msgspec
from django.utils.functional import Promise
from rest_framework.renderers import BaseRenderer


__all__ = ['MsgspecJSONRenderer', ]

from rest_framework.settings import api_settings


def enc_hook(obj: Any) -> Any:
    if isinstance(obj, dict):
        return dict(obj)
    elif isinstance(obj, list):
        return list(obj)
    elif isinstance(obj, Decimal):
        if api_settings.COERCE_DECIMAL_TO_STRING:
            return str(obj)
        else:
            return float(obj)
    elif isinstance(obj, (str, uuid.UUID, Promise)):
        return str(obj)
    elif hasattr(obj, "tolist"):
        return obj.tolist()
    elif hasattr(obj, "__iter__"):
        return list(item for item in obj)


class MsgspecJSONRenderer(BaseRenderer):
    media_type = 'application/json'
    format = 'json'
    ensure_ascii = True
    charset = None

    def render(self, data: Any, *args, **kwargs):
        if data is None:
            return bytes()

        encoder = msgspec.json.Encoder(enc_hook=enc_hook)
        return encoder.encode(data)
