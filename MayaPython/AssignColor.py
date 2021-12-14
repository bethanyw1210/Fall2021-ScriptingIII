import maya.cmds as cmds

def ColorChanger(color):
    colors = ["Clear", "Black", "Dark Grey", "Maroon", "Dark Blue", "Light Blue", "DarkGreen",
              "Purple", "Lavender", "Light Brown", "Brown", "Rust", "Red", "Green", "Blue", "White",
              "Yellow", "Teal", "Seafoam", "Pink"]

    if isinstance(color, str):
        colIndex = colors.index(color)
    else:
        colIndex = color

    items = cmds.ls(sl=True)
    for i in items:
        shape = "".join(cmds.listRelatives(i, shapes = True))
        cmds.setAttr(shape + ".overrideEnabled", 1)
        cmds.setAttr(shape + ".overrideColor", colIndex)