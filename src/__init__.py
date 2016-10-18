import FreeCAD
import FreeCADGui as Gui
from ._Classes import *


class makeTable():
    """create an involute gear"""
    def __init__(self):
        pass

    def GetResources(self):
        return {'Pixmap': '', 'MenuText': 'Table', 'ToolTip': 'Table'}

    def IsActive(self):
        if FreeCAD.ActiveDocument is None:
            return False
        else:
            return True

    def Activated(self):
        a=FreeCAD.ActiveDocument.addObject("Part::FeaturePython","Table")
        Table(a)
        ViewProviderBox(a.ViewObject)
        FreeCAD.ActiveDocument.recompute()
        Gui.SendMsgToActiveView("ViewFit")
