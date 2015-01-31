#!/usr/bin/env python
import os
import bottle

@bottle.route('/')
def index():
    return 'qwerty'

if __name__ == '__main__':
    ip   = os.environ['OPENSHIFT_PYTHON_IP']
    port = int(os.environ['OPENSHIFT_PYTHON_PORT'])
    bottle.run(host=ip, port=port)

