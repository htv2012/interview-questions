from StringIO import StringIO
from pprint import pprint

SEPARATOR = ','

def serialize(string_list):
    buf = StringIO()
    for s in string_list:
        buf.write(str(len(s)) + SEPARATOR + s + SEPARATOR)
    buf.write('-1' + SEPARATOR)
    serialized_string = buf.getvalue()
    return serialized_string

def deserialize(serialized_string):
    string_list = []
    string_start = 0
    while True:
        separator_position =  serialized_string.find(SEPARATOR, string_start)
        string_length = int(serialized_string[string_start:separator_position])
        if string_length == -1:
            break
        string_start = separator_position + 1
        string_list.append(serialized_string[string_start:string_start+string_length])
        string_start += string_length + 1
    return string_list

#
# Main
#

string_list = [
    'Once Upon a Time, in the West',
    'Gone "with" the Wind',
    '',
    'Bliss',
]

# string_list = []

serialized_string = serialize(string_list)
print '>{}<'.format(serialized_string)

string_list = deserialize(serialized_string)
pprint(string_list)