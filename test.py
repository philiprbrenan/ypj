from jinja2 import Template
import yaml

document = """                                                                  # Some sample yml
name: World
greeting: Hello
"""

y = yaml.load(document, Loader=yaml.FullLoader)                                 # Load the yml document

print("Direct  : "+y["greeting"]+" "+y["name"])                                 # Print directly
print(Template("Template: {{greeting}} {{name}}").                              # Print via template
  render(greeting=y["greeting"],name=y["name"]))
