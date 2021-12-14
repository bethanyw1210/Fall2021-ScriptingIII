import maya.cmds as cmds

def Rename(name, countStart = 1):

    sels = cmds.ls(sl=True)

    numberOfCharacters = name.count("#")
    nameParts = name.partition("#" * numberOfCharacters)

    if not nameParts[2]:
        cmds.error("Argument requires at least one #. Additional # characters must be consecutive.")

    for index, sel in enumerate(sels, start = countStart):
         newName = nameParts[0] + str(index).zfill(numberOfCharacters) + nameParts[2]
         cmds.rename(sel, newName)