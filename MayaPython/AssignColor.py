import maya.cmds as cmds

def ColorChanger(color):
    colors = ["Clear", "Black", "Dark Grey", "Maroon", "Dark Blue", "Light Blue", "DarkGreen",
              "Purple", "Lavender", "Light Brown", "Brown", "Rust", "Red", "Green", "Blue", "White",
              "Yellow", "Teal", "Seafoam", "Pink"]

    if isinstance(color, str):
        color = colors.index(color)

    sels = cmds.ls(sl=True)
    print(sels)

    for sel in sels:
        shape = "".join(cmds.listRelatives(sel, shapes = True))
        print(shape)
        cmds.setAttr(shape + ".overrideEnabled", True)
        cmds.setAttr(shape + ".overrideColor", color)

ColorChanger(5)