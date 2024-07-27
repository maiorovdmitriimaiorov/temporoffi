import json

data = '''
{
    "title": "Welcome",
    "caption": "This is the caption text.",
    "body": "Here is the body of the text."
}
'''

parsed_data = json.loads(data)

# Accessing the caption
print("Caption:", parsed_data['caption'])
