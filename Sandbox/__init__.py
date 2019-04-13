import os, sys
FRAMEWORK_NAMESPACE = os.sep + "AkamaiCC" + os.sep
### Checking if inside NAMESPACE hierarchy
if __file__.find(FRAMEWORK_NAMESPACE) == -1:
    print("Program does not located inside {0} hierarchy".format(FRAMEWORK_NAMESPACE))
    sys.exit(1)
### Adding Base Path from hierarchy to temporary PATH
__base_directory = __file__.split(FRAMEWORK_NAMESPACE)[0] + FRAMEWORK_NAMESPACE
sys.path.append(__base_directory)
os.environ.setdefault("AkamaiCC", __base_directory)

