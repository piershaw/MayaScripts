
"""
Created by Pier Shaw on 01/09/2017
Copyright © 2016 Pier Shaw. All rights reserved.
Simple Python 2D array no Modules needed
piershaw@gmail.com
Maya Switch Texture Paths from OSX to PC
Use to move textures from upgrade or OSX Maya to PC
"""

import maya.cmds as cmds
import maya.mel as mel
import os

fileTextures = cmds.ls(typ="file")
yourPathToTextures = "\Volumes\untitled"
yourMainDrive = "C:/"

def findPath():
    for textrue in fileTextures:
        path = cmds.getAttr("%s.fileTextureName" % (textrue))
        result = os.path.exists(path)
        print("tex " + str(result))
        if textrue == True:
            print("queryPath " + str(path))
            splitPath = str(path).replace(yourPathToTextures,yourMainDrive)
            print("splitPath " + splitPath)

    cmds.setAttr("%s.fileTextureName" % (textrue), splitPath, type="string")

findPath()
