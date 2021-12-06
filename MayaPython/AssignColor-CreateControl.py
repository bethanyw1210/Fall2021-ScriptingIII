import maya.cmds as cmds

def colorChanger(color):
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


def createAndGroupControl(input):
    sels = cmds.ls(sl=True)

    for sel in sels:
        name = list(sel.rpartition("_"))
        while("" in name):
            name.remove("")
        ctrl = cmds.circle(normal = (0,1,0), name = f"{name[0]}_Ctrl")[0]
        grp = cmds.group(ctrl, name = f"{name[0]}_Ctrl_Grp")
        cmds.matchTransform(grp, sel)
        cmds.select(ctrl, replace = True)
        colorChanger(input)


createAndGroupControl(13)
