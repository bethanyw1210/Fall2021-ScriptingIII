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



window = cmds.window("Rigging Toolkit", height=250, width=400
                     )
cmds.columnLayout(parent=window)
cmds.rowColumnLayout(numberOfColumns = 2)

renameText = cmds.textField("Rename", placeholderText="Joint Name",
                                  height=50, width=200)
renameButton = cmds.button("Rename Joints", height=50, width=200,
                           command="Rename('Leg_##_Jnt', 1")

controlButton = cmds.button("Create Control", height=50, width=200,
                            command="createAndGroupControl(13)")

##Colors
assignColorGray = cmds.button("Default (0)", backgroundColor = (.273,.273,.273), width=100,
                          command="colorChanger(0)")
assignColorBlack = cmds.button("Black (1)", backgroundColor = (0,0,0), width=100,
                          command="colorChanger(1)")
assignColorDarkGray = cmds.button("Dark Gray (2)", backgroundColor = (.113,.113,.113), width=100,
                          command="colorChanger(2)")
assignColorLightGray = cmds.button("Light Gray (3)", backgroundColor = (.273,.273,.273), width=100,
                          command="colorChanger(3)")
assignColorDarkRed = cmds.button("Dark Red (4)", backgroundColor = (.348,.057,.064), width=100,
                          command="colorChanger(4)")
assignColorDarkBlue = cmds.button("Dark Blue (5)", backgroundColor = (.029,.016,.186), width=100,
                          command="colorChanger(5)")
assignColorBlue = cmds.button("Blue (6)", backgroundColor = (.100,.031,3.658), width=100,
                          command="colorChanger(6)")
assignColorDarkGreen = cmds.button("Dark Green (7)", backgroundColor = (.059,.121,.045), width=100,
                          command="colorChanger(7)")
assignColorPurple = cmds.button("Purple (8)", backgroundColor = (.052,.013,.114), width=100,
                          command="colorChanger(8)")
assignColorMagent = cmds.button("Magenta (9)", backgroundColor = (.531,.091,.768), width=100,
                          command="colorChanger(9)")
assignColorBrown = cmds.button("Brown (10)", backgroundColor = (.288,.145,.088), width=100,
                          command="colorChanger(10)")
assignColorDarkBrown = cmds.button("Dark Brown (11)", backgroundColor = (.096,.058,.049), width=100,
                          command="colorChanger(11)")
assignColorSienna = cmds.button("Sienna (12)", backgroundColor = (.333,.089,.016), width=100,
                          command="colorChanger(12)")
assignColorAxisRed = cmds.button("Axis Red (13)", backgroundColor = (1.240,.106,.018), width=100,
                          command="colorChanger(13)")
assignColorAxisGreen = cmds.button("Axis Green (14)", backgroundColor = (.294,5.113,0), width=100,
                          command="colorChanger(14)")
assignColorAxisBlue = cmds.button("Axis Blue (15)", backgroundColor = (.081,.115,.404), width=100,
                          command="colorChanger(15)")
assignColorWhite = cmds.button("White (16)", backgroundColor = (16.3,16.3,16.3), width=100,
                          command="colorChanger(16)")
assignColorYellow = cmds.button("Yellow (17)", backgroundColor = (6.71,12.505,0), width=100,
                          command="colorChanger(17)")
assignColorLightBlue = cmds.button("Light Blue (18)", backgroundColor = (.432,1.213,8.659), width=100,
                          command="colorChanger(18)")
assignColorPastelTurquoise = cmds.button("Pastel Turquoise (19)", backgroundColor = (.351,5.519,.408), width=100,
                          command="colorChanger(19)")
assignColorPalePink = cmds.button("Pale Pink (20)", backgroundColor = (2.320,.606,.574), width=100,
                          command="colorChanger(20)")
assignColorFlesh = cmds.button("Flesh (21)", backgroundColor = (1.094,.572,.285), width=100,
                          command="colorChanger(21)")
assignColorPaleYellow = cmds.button("Pale Yellow (22)", backgroundColor = (7.271,12.877,0), width=100,
                          command="colorChanger(22)")
assignColorDarkTurquoise = cmds.button("Dark Turquoise (23)", backgroundColor = (.175,.402,.174), width=100,
                          command="colorChanger(23)")
assignColorLightBrown = cmds.button("Light Brown (24)", backgroundColor = (.384,.237,.089), width=100,
                          command="colorChanger(24)")
assignColorSage = cmds.button("Sage (25)", backgroundColor = (.443,.469,.104), width=100,
                          command="colorChanger(25)")
assignColorGreen = cmds.button("Green (26)", backgroundColor = (.286,.455,.104), width=100,
                          command="colorChanger(26)")
assignColorTurquoise = cmds.button("Turquoise (27)", backgroundColor = (.210,.448,.198), width=100,
                          command="colorChanger(27)")
assignColorRobinBlue = cmds.button("Robin Blue (28)", backgroundColor = (.223,.450,.473), width=100,
                          command="colorChanger(28)")
assignColorFrenchBlue = cmds.button("French Blue (29)", backgroundColor = (.147,.211,.456), width=100,
                          command="colorChanger(29)")
assignColorViolet = cmds.button("Violet (30)", backgroundColor = (.208,.096,.447), width=100,
                          command="colorChanger(30)")
assignColorPlum = cmds.button("Plum (31)", backgroundColor = (.350,.109,.219), width=100,
                          command="colorChanger(31")

cmds.showWindow(window)