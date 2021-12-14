import AssignColor
import CreateControl
import RenameObjects
import maya.cmds as cmds
import importlib

class RiggingWindowToolkit():
    def __init__(self):
        self.window = 'RiggingWindow'
        pass

    def createWin(self):
        self.delete()

        self.window = cmds.window("Rigging Toolkit", height=250, width=400)
        cmds.rowColumnLayout(numberOfColumns=1)

        renameText = cmds.textFieldButtonGrp(label='Rename Tool', placeholderText='ex. L_Leg_01_Jnt', buttonLabel='Rename',
                                             buttonCommand=lambda *x: RenameObjects.Rename(cmds.textFieldButtonGrp(renameText, q=True, text=True)))

        controlButton = cmds.button("Create Control", height=25, width=200,
                                    command=lambda x: CreateControl.createAndGroupControl(cmds.colorIndexSliderGrp(colorSlider, q=True, value=True)-1))

        colorSlider = cmds.colorIndexSliderGrp(label='Select Color', min=0, max=20, value=15,)

        assignColorButton = cmds.button("Assign Color", height=25, width=200,
                                        command=lambda x: AssignColor.ColorChanger(cmds.colorIndexSliderGrp(colorSlider, q=True, value=True)-1))

        cmds.showWindow(self.window)


    def delete(self):
        if cmds.window(self.window, exists=True):
            cmds.deleteUI(self.window)

daWindow = RiggingWindowToolkit()
daWindow.createWin()

