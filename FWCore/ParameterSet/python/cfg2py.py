import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.parseConfig as cmsParse
from sys import argv

print "import FWCore.ParameterSet.Config as cms"

fileInPath = argv[1]

if fileInPath.endswith('cfg'):
    print cmsParse.parseCfgFile(fileInPath).dumpPython()
else:
    print cmsParse.parseCffFile(fileInPath).dumpPython()

