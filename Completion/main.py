# -*- coding: utf-8 -*-

import base64

# Contents of the 'encrypted' tag given after completing level 5
message = ''

# Username as seen in the foobar shell
key = ''

result = []
for i, c in enumerate(base64.b64decode(message)):
    result.append(chr(c ^ ord(key[i % len(key)])))

print(''.join(result))
