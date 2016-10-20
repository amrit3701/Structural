import FreeCAD as App

__all__=["ViewProviderBox",
         "Table"]


import FreeCAD, Part, math
from FreeCAD import Base
from pivy import coin

#class PartFeature:
#    def __init__(self, obj):
#        obj.Proxy = self

class Table():
    def __init__(self, obj):
        #PartFeature.__init__(self, obj)
        ''' Add some custom properties to our box feature '''
        obj.addProperty("App::PropertyLength","L_Length","Slab","Length of the slab").L_Length=10.0
        obj.addProperty("App::PropertyLength","L_Width","Slab","Width of the slab").L_Width=10.0
        obj.addProperty("App::PropertyLength","L_Height","Slab", "Height of the slab").L_Height=1.0
        obj.addProperty("App::PropertyLength","S_Length","Leg","Length of the leg").S_Length=1.0
        obj.addProperty("App::PropertyLength","S_Width","Leg","Width of the leg").S_Width=1.0
        obj.addProperty("App::PropertyLength","S_Height","Leg", "Height of the leg").S_Height=8.0
        obj.Proxy = self

    def onChanged(self, fp, prop):
        ''' Print the name of the property that has changed '''
        FreeCAD.Console.PrintMessage("Change property: " + str(prop) + "\n")
        slab = Part.makeBox(fp.L_Length,fp.L_Width,fp.L_Height)
        leg1 = Part.makeBox(fp.S_Length,fp.S_Width,fp.S_Height)
        leg2 = Part.makeBox(fp.S_Length,fp.S_Width,fp.S_Height)
        leg3 = Part.makeBox(fp.S_Length,fp.S_Width,fp.S_Height)
        leg4 = Part.makeBox(fp.S_Length,fp.S_Width,fp.S_Height)
        if prop == "L_Length" or prop == "L_Width" or prop == "L_Height" or prop == "S_Length" or prop == "S_Width" or prop == "S_Height":
            slab.Placement = App.Placement(App.Vector(0,0,fp.S_Height),App.Rotation(App.Vector(0,0,1),0))
            leg1.Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))
            leg2.Placement = App.Placement(App.Vector((fp.L_Length-fp.S_Length),0,0),App.Rotation(App.Vector(0,0,1),0))
            leg3.Placement = App.Placement(App.Vector((fp.L_Length-fp.S_Length),(fp.L_Width-fp.S_Width),0),App.Rotation(App.Vector(0,0,1),0))
            leg4.Placement = App.Placement(App.Vector(0,(fp.L_Width-fp.S_Width),0),App.Rotation(App.Vector(0,0,1),0))
            fusion1 = slab.fuse(leg1)
            fusion2 = fusion1.fuse(leg2)
            fusion3 = fusion2.fuse(leg3)
            fp.Shape = fusion3.fuse(leg4)


    def execute(self, fp):
        # Print a short message when doing a recomputation, this method is mandatory
        FreeCAD.Console.PrintMessage("Recompute Python Box feature\n")
        slab = Part.makeBox(fp.L_Length,fp.L_Width,fp.L_Height)
        leg1 = Part.makeBox(fp.S_Length,fp.S_Width,fp.S_Height)
        leg2 = Part.makeBox(fp.S_Length,fp.S_Width,fp.S_Height)
        leg3 = Part.makeBox(fp.S_Length,fp.S_Width,fp.S_Height)
        leg4 = Part.makeBox(fp.S_Length,fp.S_Width,fp.S_Height)
        slab.Placement = App.Placement(App.Vector(0,0,fp.S_Height),App.Rotation(App.Vector(0,0,1),0))
        leg1.Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))
        leg2.Placement = App.Placement(App.Vector((fp.L_Length-fp.S_Length),0,0),App.Rotation(App.Vector(0,0,1),0))
        leg3.Placement = App.Placement(App.Vector((fp.L_Length-fp.S_Length),(fp.L_Width-fp.S_Width),0),App.Rotation(App.Vector(0,0,1),0))
        leg4.Placement = App.Placement(App.Vector(0,(fp.L_Width-fp.S_Width),0),App.Rotation(App.Vector(0,0,1),0))
        fusion1 = slab.fuse(leg1)
        fusion2 = fusion1.fuse(leg2)
        fusion3 = fusion2.fuse(leg3)
        fp.Shape = fusion3.fuse(leg4)




class ViewProviderBox:
    def __init__(self, obj):
        ''' Set this object to the proxy object of the actual view provider '''
        obj.Proxy = self

    def attach(self, obj):
        ''' Setup the scene sub-graph of the view provider, this method is mandatory '''
        return

    def updateData(self, fp, prop):
        ''' If a property of the handled feature has changed we have the chance to handle this here '''
        return

    def getDisplayModes(self,obj):
        ''' Return a list of display modes. '''
        modes=[]
        return modes

    def getDefaultDisplayMode(self):
        ''' Return the name of the default display mode. It must be defined in getDisplayModes. '''
        return "FlatLines"

    def setDisplayMode(self,mode):
        ''' Map the display mode defined in attach with those defined in getDisplayModes.
        Since they have the same names nothing needs to be done. This method is optinal.
        '''
        return mode

    def onChanged(self, vp, prop):
        ''' Print the name of the property that has changed '''
        FreeCAD.Console.PrintMessage("Change property: " + str(prop) + "\n")

    def getIcon(self):
        ''' Return the icon in XMP format which will appear in the tree view. This method is optional
        and if not defined a default icon is shown.
        '''
        return """
                    /* XPM */
                    static const char * ViewProviderBox_xpm[] = {
                    "16 16 6 1",
                    "   c None",
                    ".  c #141010",
                    "+  c #615BD2",
                    "@  c #C39D55",
                    "#  c #000000",
                    "$  c #57C355",
                    "        ........",
                    "   ......++..+..",
                    "   .@@@@.++..++.",
                    "   .@@@@.++..++.",
                    "   .@@  .++++++.",
                    "  ..@@  .++..++.",
                    "###@@@@ .++..++.",
                    "##$.@@$#.++++++.",
                    "#$#$.$$$........",
                    "#$$#######      ",
                    "#$$#$$$$$#      ",
                    "#$$#$$$$$#      ",
                    "#$$#$$$$$#      ",
                    " #$#$$$$$#      ",
                    "  ##$$$$$#      ",
                    "   #######      "};
                    """

    def __getstate__(self):
        ''' When saving the document this object gets stored using Python's cPickle module.
        Since we have some un-pickable here -- the Coin stuff -- we must define this method
        to return a tuple of all pickable objects or None.
        '''
        return None

    def __setstate__(self,state):
        ''' When restoring the pickled object from document we have the chance to set some
        internals here. Since no data were pickled nothing needs to be done here.
        '''
        return None


