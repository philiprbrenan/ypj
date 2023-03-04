from jinja2 import Template
template = Template('Hello {{ name }}!')
print(template.render(name='World'))

import yaml
document = """
name: World
greeting: Hello
"""


y = yaml.load(document)
print(yaml.dump(y))

for data in y:
  print(data)
