Bottle-OpenShift-minimal
========================

Bottle.py + Python3.3 + OpenShift with Minimal Configuration

Running on OpenShift Online
===========================
1. Create an account at https://www.openshift.com
2. Create a python-3.3 application

  ```
  rhc app create <YourAppName> python-3.3
  ...
  ...
  ...
  Your application '<YourAppName>' is now available.

  URL:        http://<YourAppName>-example.rhcloud.com/
  SSH to:     exampleexample@<YourAppName>-example.rhcloud.com
  Git remote: ssh://exampleexampleexample@<YourAppName>-example.rhcloud.com/~/git/<YourAppName>.git/
  ```
4. Clone OpenShift repo
  
  ```
  git clone ssh://exampleexampleexample@<YourAppName>-example.rhcloud.com/~/git/<YourAppName>.git/
  ```

5. Add this repo

  ```
  cd <YourAppName>
  git remote add minimal git://github.com/tpdn/Bottle-OpenShift-minimal.git
  git pull minimal master
  ```
6. Then push the repo to OpenShift

  ```
  git push
  ```
