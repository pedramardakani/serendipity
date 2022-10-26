# Convert Python dictionary to XML
#
# A quick pair programming challenge, solved with help of Victor.
#
# Pedram Ashofteh-Ardakani <pedramardakani@pm.me>


def parse_nested(items: list)->str:
    stack=""
    for item in items:
        stack+=f"<item>{item}</item>"
    return stack


def convert(data: dict)->str:
    stack=""
    for key, value in data.items():
        parsed_value = parse_nested(value) if type(value)==list else value
        stack+=f"<{key}>{parsed_value}</{key}>"
    return stack
