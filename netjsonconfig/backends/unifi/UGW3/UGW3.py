from netjsonconfig.backends.base.backend import BaseBackend
from netjsonconfig.backends.base.renderer import BaseRenderer
from netjsonconfig.backends.base.parser import BaseParser

from netjsonconfig.schema import schema as default_schema


class UGW3(BaseBackend):
    schema = default_schema
    converters = []
    parser = BaseParser
    renderer = BaseRenderer
