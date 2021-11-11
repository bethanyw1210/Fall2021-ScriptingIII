import maya.cmds as cmds

# cmds.ls(sl=1)
# def renameObjects(name):
#
#     for i in i++
#         "Leg_01_Jnt".count("1")
#         "Leg_01_Jnt".partition("01")
#         "Leg_0_1_Jnt".partition("01")
#
#         "Leg_01_Jnt" + string(i).zfill(count) + "Leg_0_1_Jnt"
#
# renameObjects("Leg_01_Jnt")


#Class solution
def Rename(name, countStart = 1):

    sels = cmds.ls(sl=True)

    numberOfCharacters = name.count("#")
    nameParts = name.partition("#" * numberOfCharacters)

    if not nameParts[2]:
        cmds.error("Argument requires at least one #. Additional # characters must be consecutive.")

    #loop through each selected object
    # index = 1
    # for sel in sels:
    #     newName = nameParts[0] + str(index).zfill(numberOfCharacters) + nameParts[2]
    #     cmds.rename(sel, newName)
    #     index += 1

    #enumerator loop version
    for index, sel in enumerate(sels, start = countStart):
         newName = nameParts[0] + str(index).zfill(numberOfCharacters) + nameParts[2]
         cmds.rename(sel, newName)

Rename("Leg_##_Jnt", 1)