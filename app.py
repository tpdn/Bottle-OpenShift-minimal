#!/usr/bin/env python
import os
import bottle

@bottle.route('/')
def index():
    return 'qwerty'

if __name__ == '__main__':
    ip   = os.environ['OPENSHIFT_PYTHON_IP']
    port = 8080
    bottle.run(host=ip, port=port)

