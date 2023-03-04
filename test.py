from jinja2 import Template
template = Template('Hello {{ name }}!')
print(template.render(name='World'))

import yaml
document = """
name: World
greeting: Hello
"""
print yaml.dump(yaml.load(document))
