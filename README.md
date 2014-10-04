Bottle-OpenShift-minimal
========================

Bottle.py + Python3.3 + OpenShift with Minimal Configuration

Running on OpenShift Online
===========================
1. Create an account at https://www.openshift.com
2. Create a python-3.3 application

  ```
  rhc app create <YourAppName> python-3.3
  ```
3. Add this repo

  ```
  cd <YourAppName>
  git remote add minimal git://github.com/tpdn/Bottle-OpenShift-minimal.git
  git pull -s recursive minimal master
  ```
4. Then push the repo to OpenShift

  ```
  git push
  ```
