from jinja2 import Template
import yaml

document = """                                                                  # Some sample yml
name: World
greeting: Hello
"""

y = yaml.load(document, Loader=yaml.FullLoader)                                 # Load the yml document

print(y["greeting"]+" "+y["name"])                                              # Print directly
print(Template("The greeting is this:\n{{greeting}}\n{{name}}\n").render        # Print via template
 (greeting=y["greeting"],name=y["name"]))
