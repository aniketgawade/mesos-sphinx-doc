
# -*- coding: utf-8 -*-
#

import sys
import os

sys.path.insert(0, os.path.abspath('../src/'))
autodoc_mock_imports = [
    'gevent',
    'gevent.queue',
    'cfgm_common',
    'cfgm_common.vnc_amqp',
    'mesos_manager.mesos_consts',
    'vnc_api.vnc_api',
    'config_db',
    'reaction_map',
    'db',
    '*',
    '*',
]
extensions = ['sphinx.ext.autodoc']
source_suffix = '.rst'
master_doc = 'index'
project = u'Sphinx Autodoc Example'
copyright = u'Ondrej Sika, ondrej@ondrejsika.com'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
html_theme = 'default'
autoclass_content = "both"
