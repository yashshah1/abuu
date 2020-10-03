from typing import Dict, Any

class ConfigClass:
    pass

"""
A lot of config usually exists as JSON objects, when parsed in Python,
it results in a dict being generated which can be accessed as dict['key']

However, this looks less cleaner than writing config.key, which is more elegant.
This function aims to convert a given config dict into a class which can be accessed as above.
"""
def get_config_class(config: Dict[str, Any]) -> ConfigClass:
    config_class = ConfigClass()
    for key, value in config.items():
        assert isinstance(key, str), "The keys of config must be `str`. Invalid key: {}".format(key)
        setattr(config_class, key, value)
    return config_class