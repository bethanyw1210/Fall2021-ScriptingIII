import maya.cmds as cmds
import AssignColor
import importlib
importlib.reload(AssignColor)


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
        AssignColor.ColorChanger(input)

