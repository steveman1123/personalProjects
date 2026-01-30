#install the flatpak version of freecad
#create a freecad triangle sketch, extrude, then save and export to stl
#run in freecad "flatpak run org.freecad.FreeCAD --console ./triangle-test.py"

import sys

sys.path.append("/var/lib/flatpak/app/org.freecad.FreeCAD/current/active/files/lib")
sys.path.append("/var/lib/flatpak/app/org.freecad.FreeCAD/current/active/files/freecad/bin")
sys.path.append("/var/lib/flatpak/app/org.freecad.FreeCAD/current/active/files/freecad/Mod")

import FreeCAD as fc
import Part, Sketcher, Mesh

print(dir(fc))

docTest = fc.newDocument('test')

# Create a sketch
s = docTest.addObject("Sketcher::SketchObject","TriangleSketch")
s.Placement = fc.Placement(fc.Vector(0,0,0),fc.Rotation(0,0,0))

# Define triangle points
p1 = fc.Vector(0, 0, 0)
p2 = fc.Vector(50, 0, 0)
p3 = fc.Vector(25, 40, 0)

# Add triangle edges
s.addGeometry(Part.LineSegment(p1, p2), False)
s.addGeometry(Part.LineSegment(p2, p3), False)
s.addGeometry(Part.LineSegment(p3, p1), False)

docTest.recompute()


# Pad (extrude) the sketch
pad = docTest.addObject("PartDesign::Pad", "Pad")
pad.Profile = s
pad.Length = 10.0
pad.Reversed = False

docTest.recompute()

# Save FreeCAD file
fcfile = "~/triangleTest.FCStd"
docTest.saveAs(fcfile)

# Export to STL
stlfile = "~/triangle_pad.stl"
Mesh.export([pad], stlfile)

print("Saved FreeCAD file:", fcfile)
print("Exported STL file:", stlfile)
