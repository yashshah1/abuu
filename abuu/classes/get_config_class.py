from typing import Dict, Generic, TypeVar, Union
import json

V = TypeVar("V")

class ConfigClass(Generic[V]):
    """
    A lot of config usually exists as JSON objects, when parsed in Python,
    it results in a dict being generated which can be accessed as dict['key']

    However, this looks less cleaner than writing config.key, which is more elegant.
    This function aims to convert a given config dict into a class which can be accessed as above.
    """

    _data: Dict[str, V]

    def __init__(self, data: Union[str, Dict[str, V]]) -> None:
        """Can accept a dict or json string"""
        # we dont check that the keys are strings for 2 reasons
        # 1) it is shown in the type hints that it must be a string, so users should make sure of that them self.
        # 2) this is expected to take json, and json always has str keys
        if isinstance(data, str):
            self._data = json.loads(data)
        elif isinstance(data, dict):
            self._data = data
        else:
            raise ValueError("data must be either a JSON string or a python dict")

    def __getattr__(self, key: str) -> V:
        """Try and get the attribute from data"""
        try:
            return self._data[key]
        except KeyError as e:
            raise AttributeError(f"no attribute {key}.") from e



get_config_class = ConfigClass  # for backwards compatibility.
