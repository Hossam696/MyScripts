'''
This Script created by Hossam Eldin Nasser

This script is used to check if the selected guides are inside the selected mesh

if no mesh is selected then it'll take the mesh of the description

tolerance variable represents the minimum distance considered as it's inside the mesh
change it to adjust how far from mesh you want the guide to be

'''

import maya.cmds as cmds
import maya.mel as mel
import maya.api.OpenMaya as om

cmds.undoInfo(openChunk = True)
tolerance = 0.1     #change it to adjust how far from mesh you want the guide to be
#get selected guides
def filterGuides(to_be_filtered):
    mesh = None
    selGuides = []
    sel = to_be_filtered
    for guide in sel:
        gShape = cmds.listRelatives(guide,shapes=True , noIntermediate=True)
        gShape = cmds.ls(gShape , typ= "xgmSplineGuide")
        if not gShape:
            continue
        selGuides.append(guide)

    if len(selGuides)<1:
        raise RuntimeError("No Guides Selected")

    for obj in sel:
        objShape = cmds.listRelatives(obj , shapes=True , noIntermediate=True)
        objShape = cmds.ls(objShape , typ= "mesh")
        if objShape :
            mesh = objShape[0]
            break
    if not mesh:
        mesh = cmds.ls(cmds.listHistory(selGuides),typ="mesh")[0]

    cmds.select(selGuides,r=True)
    return selGuides , mesh

Guides , mesh = filterGuides(cmds.ls(sl=1))

mel.eval("xgmCreateCurvesFromGuides 1 1;")
#list guides that converted to curves
Guides_as_Curves = cmds.ls(sl=1)

#loop on cvs and move the inside ones out
closestNode = cmds.createNode("closestPointOnMesh")
cmds.connectAttr(mesh+".outMesh",closestNode+".inMesh",f=True)

for cur in Guides_as_Curves:
    CVs = cmds.ls(cur+".cv[*]",fl=True)
    for idx , cv in enumerate(CVs):
        if idx == 0:    #skip root cv
            continue
        position = cmds.xform(cv,q=True,ws=True,t=True)
        # print("Position >> "+str(position))
        vector_position = om.MVector(position)
        cmds.setAttr(closestNode+".inPosition",position[0],position[1],position[2])
        nearestPosition = cmds.getAttr(closestNode+".position")[0]
        vector_nearestPosition = om.MVector(nearestPosition)
        #globalizing nearest position
        meshTransform = cmds.listRelatives(mesh,parent=True,type="transform")[0]
        vector_nearestPosition[0]*=cmds.getAttr(meshTransform+".scaleX")
        vector_nearestPosition[1]*=cmds.getAttr(meshTransform+".scaleY")
        vector_nearestPosition[2]*=cmds.getAttr(meshTransform+".scaleZ")
        # print("nearest Position >> "+str(vector_nearestPosition))
        vector_to_nearest = vector_position - vector_nearestPosition
        # print("vector to nearest Position >> "+str(vector_to_nearest))
        outNormal = cmds.getAttr(closestNode+".normal")[0]
        vector_outNormal = om.MVector(outNormal)
        dotProduct = vector_to_nearest * vector_outNormal
        if dotProduct < tolerance:
            cmds.move(tolerance - vector_to_nearest.x , tolerance - vector_to_nearest.y , tolerance - vector_to_nearest.z , cv, ws =True , r=True )

cmds.delete(closestNode)

#select the listed guides that converted to curves
cmds.select(Guides_as_Curves,r=True)
mel.eval("xgmGuidesAsCurvesToolAccept;")
cmds.select(Guides,r=1)
cmds.undoInfo(closeChunk = True)