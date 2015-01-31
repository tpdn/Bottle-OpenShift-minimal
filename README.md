Bottle-OpenShift-minimal
========================

Bottle.py + Python3.3 + OpenShift with Minimal Configuration

Running on OpenShift Online
===========================
1. Create an account at https://www.openshift.com .
2. Create a python-3.3 application based on the code in this repo.

  ```
  rhc app create <YourAppName> python-3.3 \
    --from-code https://github.com/tpdn/Bottle-OpenShift-minimal.git
  ```
3. That's it.

  ```
    http://<YourAppName>-example.rhcloud.com
  ```
