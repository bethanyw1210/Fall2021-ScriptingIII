import maya.cmds as cmds

sels = cmds.ls(sl=True)

cmds.circle(name="_Ctrl")
cmds.group("_Ctrl", name="_Ctrl_Grp")

cmds.setAttr("_Ctrl.overrideEnabled", True)
cmds.setAttr("_Ctrl.overrideColor", 5)

cmds.matchTransform("_Ctrl", "joint1")