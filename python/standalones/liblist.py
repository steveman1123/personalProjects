#when libraries were installed

import pkg_resources, os, time

for pkg in pkg_resources.working_set:
  print("%s: %s" % (pkg, time.ctime(os.path.getctime(pkg.location))))
