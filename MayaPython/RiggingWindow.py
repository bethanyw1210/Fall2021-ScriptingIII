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



window = cmds.window("Rigging Toolkit", height=250, width=250)
cmds.columnLayout(parent=window)
renameTextButton = cmds.textField("Rename", placeholderText="Joint Name", height=25, width=250)
renameButton = cmds.button("Rename Joints", width=250, command="Rename('Leg_##_Jnt', 1")
colorIndexButton = cmds.textField("Color", placeholderText="Which Color?", height=25, width=250)
controlButton = cmds.button("Create Control", width=250, command="createAndGroupControl(13)")
assignColor = cmds.button("Assign Color", width=250, command="colorChanger(13)")
cmds.showWindow(window)