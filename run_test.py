import sys
import os
from importlib import import_module

args = sys.argv

testsFolderContent = os.listdir("tests")

tests = []
for file in testsFolderContent:
    if "Test.py" in file:
        tests.append(file.split(".")[0])

testsToRun = []
if len(args) > 1:
    if args[1] not in tests:
        print("test not found")
    else:
        testsToRun.append(args[1])
else:
    testsToRun = tests

if len(testsToRun) > 0:
    for testFile in testsToRun:
        testName = testFile
        moduleName = "tests." + testName
        module = import_module(moduleName)
        testClass = getattr(module, testName)
        testClass()
