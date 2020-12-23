from collections import OrderedDict

import yaml


class YamlOrderedDictLoader(yaml.SafeLoader):
  pass

YamlOrderedDictLoader.add_constructor(
  yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
  lambda loader, node: OrderedDict(loader.construct_pairs(node))
)
