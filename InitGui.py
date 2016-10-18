import FreeCADGui as Gui
import FreeCAD as App
import Structural_rc
import src

try:
    from FreeCADGui import Workbench
except ImportError as e:
    App.Console.PrintWarning("you are using the StructuralWorkbench with an old version of FreeCAD (<0.16)")
    App.Console.PrintWarning("the class Workbench is loaded, allthough not imported: magic")

class StructuralWorkbench(Workbench):
    """glider workbench"""
    MenuText = "Structural"
    ToolTip = "Structural Workbench"
    Icon = ""

    def GetClassName(self):
        return "Gui::PythonWorkbench"

    def Initialize(self):

        from src import makeTable

        self.appendToolbar("Structural", ["makeTable"])
        self.appendMenu("Structural", ["makeTable"])
        #Gui.addIconPath(App.getHomePath()+"Mod/gear/icons/")
        Gui.addCommand('makeTable', makeTable())

    def Activated(self):
        pass


    def Deactivated(self):
        pass



Gui.addWorkbench(StructuralWorkbench())
