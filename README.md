Django Rest Framework msgspec Renderer
==================


Django Rest Framework renderer using [msgspec](https://github.com/jcrist/msgspec)

## Installation

`pip install drf-msgspec-json-renderer`

You can then set the `MsgspecJSONRenderer` class as your default renderer in your `settings.py`

```python
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'drf_msgspec_json.renderers.MsgspecJSONRenderer',
    ),
    ...
}
```

Also you can set the `MsgspecJSONParser` class as your default parser in your `settings.py`

```python
REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': (
        'drf_msgspec_json.parsers.MsgspecJSONParser',
    ),
    ...
}
```
