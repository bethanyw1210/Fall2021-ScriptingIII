import maya.cmds as cmds

cmds.polyCube(axis=[0, 1, 0],
              constructionHistory=1,
              createUVs=4,
              depth=2,
              height=0.5,
              width=3,
              subdivisionsDepth=1,
              subdivisionsHeight=1,
              subdivisionsWidth=1,
              name="Base")
cmds.move(0, 0.75, 0)

cmds.polyCylinder(axis=[0, 1, 0],
                  constructionHistory=1,
                  createUVs=3,
                  height=2,
                  radius=0.5,
                  subdivisionsX=10,
                  subdivisionsY=1,
                  subdivisionsZ=1,
                  name="Spine")
cmds.move(0, 2, 0)

cmds.polyCube(axis=[0, 1, 0],
              constructionHistory=1,
              createUVs=4,
              depth=2.5,
              height=4,
              width=3.5,
              subdivisionsDepth=1,
              subdivisionsHeight=1,
              subdivisionsWidth=1,
              name="Body")
cmds.move(0, 5, 0)

cmds.polyCylinder(axis=[1, 0, 0],
                  constructionHistory=1,
                  createUVs=3,
                  height=0.5,
                  radius=0.5,
                  subdivisionsX=10,
                  subdivisionsY=1,
                  subdivisionsZ=1,
                  name="WheelCenter")
cmds.move(0, 0.45, 0)

cmds.polyCylinder(axis=[1, 0, 0],
                  constructionHistory=1,
                  createUVs=3,
                  height=0.5,
                  radius=0.5,
                  subdivisionsX=10,
                  subdivisionsY=1,
                  subdivisionsZ=1,
                  name="WheelLeft")
cmds.move(1, 0.45, 0)

cmds.polyCylinder(axis=[1, 0, 0],
                  constructionHistory=1,
                  createUVs=3,
                  height=0.5,
                  radius=0.5,
                  subdivisionsX=10,
                  subdivisionsY=1,
                  subdivisionsZ=1,
                  name="WheelRight")
cmds.move(-1, 0.45, 0)

cmds.polyCube(axis=[0, 1, 0],
              constructionHistory=1,
              createUVs=4,
              depth=1.5,
              height=3,
              width=1,
              subdivisionsDepth=1,
              subdivisionsHeight=1,
              subdivisionsWidth=1,
              name="LeftArm")
cmds.move(2.75, 5.5, 0)

cmds.polyCube(axis=[0, 1, 0],
              constructionHistory=1,
              createUVs=4,
              depth=1.5,
              height=3,
              width=1,
              subdivisionsDepth=1,
              subdivisionsHeight=1,
              subdivisionsWidth=1,
              name="RightArm")
cmds.move(-2.75, 5.5, 0)

cmds.polyCylinder(axis=[1, 0, 0],
                  constructionHistory=1,
                  createUVs=3,
                  height=0.75,
                  radius=0.5,
                  subdivisionsX=10,
                  subdivisionsY=1,
                  subdivisionsZ=1,
                  name="LeftShoulder")
cmds.move(2, 6.25, 0)

cmds.polyCylinder(axis=[1, 0, 0],
                  constructionHistory=1,
                  createUVs=3,
                  height=0.75,
                  radius=0.5,
                  subdivisionsX=10,
                  subdivisionsY=1,
                  subdivisionsZ=1,
                  name="RightShoulder")
cmds.move(-2, 6.25, 0)

cmds.polyCylinder(axis=[0, 1, 0],
                  constructionHistory=1,
                  createUVs=3,
                  height=1,
                  radius=0.5,
                  subdivisionsX=10,
                  subdivisionsY=1,
                  subdivisionsZ=1,
                  name="Neck")
cmds.move(0, 7.25, 0)

cmds.polyCube(axis=[0, 1, 0],
              constructionHistory=1,
              createUVs=4,
              depth=2,
              height=1.75,
              width=2,
              subdivisionsDepth=1,
              subdivisionsHeight=1,
              subdivisionsWidth=1,
              name="Head")
cmds.move(0, 8.5, 0)

cmds.polyCylinder(axis=[0, 0, 1],
                  constructionHistory=1,
                  createUVs=3,
                  height=0.5,
                  radius=0.25,
                  subdivisionsX=10,
                  subdivisionsY=1,
                  subdivisionsZ=1,
                  name="LeftEye")
cmds.move(0.55, 8.75, 1)

cmds.polyCylinder(axis=[0, 0, 1],
                  constructionHistory=1,
                  createUVs=3,
                  height=0.5,
                  radius=0.25,
                  subdivisionsX=10,
                  subdivisionsY=1,
                  subdivisionsZ=1,
                  name="RightEye")
cmds.move(-0.55, 8.75, 1)

cmds.polyCube(axis=[0, 1, 0],
              constructionHistory=1,
              createUVs=4,
              depth=0.5,
              height=0.5,
              width=1.25,
              subdivisionsDepth=1,
              subdivisionsHeight=1,
              subdivisionsWidth=1,
              name="Mouth")
cmds.move(0, 8, 1)

cmds.group("LeftEye", "RightEye", "Mouth", name="Face")

cmds.parent("Face", "Head")
cmds.parent("Head", "Neck")

cmds.parent("LeftArm", "LeftShoulder")
cmds.parent("RightArm", "RightShoulder")

cmds.parent("LeftShoulder", "RightShoulder", "Neck", "Body")

cmds.parent("WheelCenter", "WheelLeft", "WheelRight", "Base")
cmds.parent("Base", "Spine")

cmds.group("Body", "Spine", name="Robot")
