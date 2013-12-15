import MK_ARTOOLS as mk
from MK_ARTOOLS import log, c

"""tool based from Softimage Python Rigging"""
def addCnsCurve(parent, name, centers, close = False, degree = 1):
"""add curve constraint to selected objects"""
    #convert centers to list
    centers = list(centers)
    points = []
    for center in centers:

        points.append(center.Kinematics.Global.Transform.PosX)
        points.append(center.Kinematics.Global.Transform.PosY)
        points.append(center.Kinematics.Global.Transform.PosZ)
        points.append(1)
    #add curve
    curve = parent.AddNurbsCurve(points, None, close, degree,
                                c.siNonUniformParameterization, c.siSINurbs, name)


    for i, center in enumerate(centers):
        cls = curve.ActivePrimitive.Geometry.AddCluster(c.siVertexCluster, "center_"+ str(i), [i])
        xsi.ApplyOp("ClusterCenter", cls.FullName+";"+ center.FullName)


    return curve
