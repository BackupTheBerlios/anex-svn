#!/usr/bin/python
from astronex.extensions.path import path
appath = path.getcwd() 
from astronex import nex
nex.main(appath)
