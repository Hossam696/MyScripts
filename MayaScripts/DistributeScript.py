
from PySide2 import QtCore, QtGui, QtWidgets
import maya.cmds as cmds
import maya.api.OpenMaya as om
import maya.mel as mel
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
import random
import re

def undo(func):
	def wrapper(*args, **kwargs):
		cmds.undoInfo(openChunk=True)
		try:
			ret = func(*args, **kwargs)
		finally:
			cmds.undoInfo(closeChunk=True)
		return ret
	return wrapper

class Ui_DistributionWindow(object):
    def setupUi(self, DistributionWindow):
        DistributionWindow.setObjectName("DistributionWindow")
        DistributionWindow.resize(394, 652)
        self.centralwidget = QtWidgets.QWidget(DistributionWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.ObjsLayout = QtWidgets.QHBoxLayout()
        self.ObjsLayout.setObjectName("ObjsLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.txt_add_obj = QtWidgets.QLabel(self.centralwidget)
        self.txt_add_obj.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_add_obj.setObjectName("txt_add_obj")
        self.verticalLayout_2.addWidget(self.txt_add_obj)
        self.Objlist = QtWidgets.QListWidget(self.centralwidget)
        self.Objlist.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.Objlist.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.Objlist.setObjectName("Objlist")
        self.verticalLayout_2.addWidget(self.Objlist)
        self.ObjsLayout.addLayout(self.verticalLayout_2)
        self.ObjbtnsLayout_2 = QtWidgets.QVBoxLayout()
        self.ObjbtnsLayout_2.setObjectName("ObjbtnsLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.ObjbtnsLayout_2.addItem(spacerItem)
        self.obj_add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.obj_add_btn.setObjectName("obj_add_btn")
        self.ObjbtnsLayout_2.addWidget(self.obj_add_btn)
        self.obj_rmv_btn = QtWidgets.QPushButton(self.centralwidget)
        self.obj_rmv_btn.setObjectName("obj_rmv_btn")
        self.ObjbtnsLayout_2.addWidget(self.obj_rmv_btn)
        self.obj_clr_btn = QtWidgets.QPushButton(self.centralwidget)
        self.obj_clr_btn.setObjectName("obj_clr_btn")
        self.ObjbtnsLayout_2.addWidget(self.obj_clr_btn)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.ObjbtnsLayout_2.addItem(spacerItem1)
        self.ObjsLayout.addLayout(self.ObjbtnsLayout_2)
        self.gridLayout.addLayout(self.ObjsLayout, 1, 0, 1, 1)
        self.Distribute_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Distribute_btn.setObjectName("Distribute_btn")
        self.gridLayout.addWidget(self.Distribute_btn, 6, 0, 1, 1)
        self.RandomizationLayout = QtWidgets.QGridLayout()
        self.RandomizationLayout.setObjectName("RandomizationLayout")
        self.random_rotZ_chkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.random_rotZ_chkbox.setObjectName("random_rotZ_chkbox")
        self.RandomizationLayout.addWidget(self.random_rotZ_chkbox, 7, 0, 1, 1)
        self.max_rotZ_spinbox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.max_rotZ_spinbox.setMaximum(360.0)
        self.max_rotZ_spinbox.setProperty("value", 360.0)
        self.max_rotZ_spinbox.setObjectName("max_rotZ_spinbox")
        self.RandomizationLayout.addWidget(self.max_rotZ_spinbox, 7, 2, 1, 1)
        self.min_rotZ_spinbox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.min_rotZ_spinbox.setMaximum(360.0)
        self.min_rotZ_spinbox.setObjectName("min_rotZ_spinbox")
        self.RandomizationLayout.addWidget(self.min_rotZ_spinbox, 7, 1, 1, 1)
        self.min_rotX_spinbox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.min_rotX_spinbox.setMaximum(360.0)
        self.min_rotX_spinbox.setObjectName("min_rotX_spinbox")
        self.RandomizationLayout.addWidget(self.min_rotX_spinbox, 5, 1, 1, 1)
        self.min_rotY_spinbox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.min_rotY_spinbox.setMaximum(360.0)
        self.min_rotY_spinbox.setObjectName("min_rotY_spinbox")
        self.RandomizationLayout.addWidget(self.min_rotY_spinbox, 6, 1, 1, 1)
        self.match_rot_chkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.match_rot_chkbox.setObjectName("match_rot_chkbox")
        self.RandomizationLayout.addWidget(self.match_rot_chkbox, 4, 0, 1, 1)
        self.max_rotX_spinbox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.max_rotX_spinbox.setMaximum(360.0)
        self.max_rotX_spinbox.setProperty("value", 360.0)
        self.max_rotX_spinbox.setObjectName("max_rotX_spinbox")
        self.RandomizationLayout.addWidget(self.max_rotX_spinbox, 5, 2, 1, 1)
        self.random_rotY_chkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.random_rotY_chkbox.setObjectName("random_rotY_chkbox")
        self.RandomizationLayout.addWidget(self.random_rotY_chkbox, 6, 0, 1, 1)
        self.max_rotY_spinbox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.max_rotY_spinbox.setMaximum(360.0)
        self.max_rotY_spinbox.setProperty("value", 360.0)
        self.max_rotY_spinbox.setObjectName("max_rotY_spinbox")
        self.RandomizationLayout.addWidget(self.max_rotY_spinbox, 6, 2, 1, 1)
        self.random_rotX_chkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.random_rotX_chkbox.setObjectName("random_rotX_chkbox")
        self.RandomizationLayout.addWidget(self.random_rotX_chkbox, 5, 0, 1, 1)
        self.instance_chkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.instance_chkbox.setObjectName("instance_chkbox")
        self.RandomizationLayout.addWidget(self.instance_chkbox, 4, 1, 1, 1)
        self.gridLayout.addLayout(self.RandomizationLayout, 5, 0, 1, 1)
        self.LocationsLayout = QtWidgets.QHBoxLayout()
        self.LocationsLayout.setObjectName("LocationsLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.txt_add_locs = QtWidgets.QLabel(self.centralwidget)
        self.txt_add_locs.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_add_locs.setObjectName("txt_add_locs")
        self.verticalLayout.addWidget(self.txt_add_locs)
        self.Loclist = QtWidgets.QListWidget(self.centralwidget)
        self.Loclist.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.Loclist.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.Loclist.setObjectName("Loclist")
        self.verticalLayout.addWidget(self.Loclist)
        self.LocationsLayout.addLayout(self.verticalLayout)
        self.LocsbtnsLayout = QtWidgets.QVBoxLayout()
        self.LocsbtnsLayout.setObjectName("LocsbtnsLayout")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.LocsbtnsLayout.addItem(spacerItem2)
        self.Locs_add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Locs_add_btn.setObjectName("Locs_add_btn")
        self.LocsbtnsLayout.addWidget(self.Locs_add_btn)
        self.Locs_rmv_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Locs_rmv_btn.setObjectName("Locs_rmv_btn")
        self.LocsbtnsLayout.addWidget(self.Locs_rmv_btn)
        self.Locs_clr_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Locs_clr_btn.setObjectName("Locs_clr_btn")
        self.LocsbtnsLayout.addWidget(self.Locs_clr_btn)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.LocsbtnsLayout.addItem(spacerItem3)
        self.LocationsLayout.addLayout(self.LocsbtnsLayout)
        self.gridLayout.addLayout(self.LocationsLayout, 3, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        DistributionWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DistributionWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 394, 21))
        self.menubar.setObjectName("menubar")
        DistributionWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DistributionWindow)
        self.statusbar.setObjectName("statusbar")
        DistributionWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DistributionWindow)
        QtCore.QMetaObject.connectSlotsByName(DistributionWindow)

    def retranslateUi(self, DistributionWindow):
        _translate = QtCore.QCoreApplication.translate
        DistributionWindow.setWindowTitle(_translate("DistributionWindow", "DistributionWindow"))
        self.txt_add_obj.setText(_translate("DistributionWindow", "Add Objects to Distribute"))
        self.obj_add_btn.setText(_translate("DistributionWindow", "Add"))
        self.obj_rmv_btn.setText(_translate("DistributionWindow", "Remove"))
        self.obj_clr_btn.setText(_translate("DistributionWindow", "Clear"))
        self.Distribute_btn.setText(_translate("DistributionWindow", "Distribute!"))
        self.random_rotZ_chkbox.setText(_translate("DistributionWindow", "Random Rotation Z"))
        self.match_rot_chkbox.setText(_translate("DistributionWindow", "Match Rotation to Normal"))
        self.random_rotY_chkbox.setText(_translate("DistributionWindow", "Random Rotation Y"))
        self.random_rotX_chkbox.setText(_translate("DistributionWindow", "Random Rotation X"))
        self.instance_chkbox.setText(_translate("DistributionWindow", "Instanced Objects"))
        self.txt_add_locs.setText(_translate("DistributionWindow", "Add Distribute Locations"))
        self.Locs_add_btn.setText(_translate("DistributionWindow", "Add"))
        self.Locs_rmv_btn.setText(_translate("DistributionWindow", "Remove"))
        self.Locs_clr_btn.setText(_translate("DistributionWindow", "Clear"))
        self.label.setText(_translate("DistributionWindow", "©CreatedBy Hossam Eldin Nasser"))

class DistributionScript(MayaQWidgetDockableMixin,QtWidgets.QMainWindow,Ui_DistributionWindow):
    
    ForbiddenItems = [om.MFn.kMeshVertComponent,
                        om.MFn.kMeshEdgeComponent,
                        om.MFn.kMeshPolygonComponent,
                        om.MFn.kCurveCVComponent,
                        om.MFn.kCurveEPComponent]

    
    def __init__(self):
        self.deleteWorkSpaceControl()
        super(DistributionScript,self).__init__()
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        self.setupUi(self)
        self.connectSignals()

    def connectSignals(self):
        self.random_rotX_chkbox.clicked.connect(lambda : self.toggle_spinBoxes(self.random_rotX_chkbox,[self.min_rotX_spinbox,self.max_rotX_spinbox]))
        self.random_rotY_chkbox.clicked.connect(lambda : self.toggle_spinBoxes(self.random_rotY_chkbox,[self.min_rotY_spinbox,self.max_rotY_spinbox]))
        self.random_rotZ_chkbox.clicked.connect(lambda : self.toggle_spinBoxes(self.random_rotZ_chkbox,[self.min_rotZ_spinbox,self.max_rotZ_spinbox]))
        self.obj_add_btn.clicked.connect(lambda : self.add_items_to_list(self.Objlist))
        self.Locs_add_btn.clicked.connect(lambda : self.add_items_to_list(self.Loclist))
        self.obj_rmv_btn.clicked.connect(lambda : self.remove_items_from_list(self.Objlist))
        self.Locs_rmv_btn.clicked.connect(lambda : self.remove_items_from_list(self.Loclist))
        self.obj_clr_btn.clicked.connect(self.Objlist.clear)
        self.Locs_clr_btn.clicked.connect(self.Loclist.clear)
        self.Distribute_btn.clicked.connect(self.Distribute)
        return

    def toggle_spinBoxes(self,chkbox,spinBoxes):
        isActive = chkbox.isChecked()
        for box in spinBoxes:
            box.setEnabled(isActive)

    def get_list_elements(self,Qlist):
        all_elements = []
        for row in range(Qlist.count()):
            item = Qlist.item(row)
            if item is not None:
                all_elements.append(item.text())
        return all_elements
    
    def add_items_to_list(self,Qlist):
        existItems = self.get_list_elements(Qlist)
        for item in cmds.ls(sl=1,fl=1):
            if item not in existItems:
                Qlist.addItem(item)
        if Qlist == self.Objlist:
            self.refresh_list(Qlist,filter=self.ForbiddenItems)
    
    def remove_items_from_list(self,Qlist):
        selected_items = Qlist.selectedItems()
        for item in selected_items:
            Qlist.takeItem(Qlist.row(item))

    def refresh_list(self,Qlist,filter):
        Items = []
        for row in range(Qlist.count()):
            item = Qlist.item(row)
            Items.append(item)
        for item in Items:
            selection = om.MSelectionList()
            selection.add(item.text())
            if selection.getComponent(0)[1].apiType() in filter:
                Qlist.takeItem(Qlist.row(item))

    def get_vert_matrix(self,vert):
        selection = om.MSelectionList()
        selection.add(vert)
        if selection.getComponent(0)[1].apiType() != om.MFn.kMeshVertComponent:
            return
        mesh_name = vert.split(".vtx[")[0]
        normals = cmds.polyNormalPerVertex(vert,q=1,xyz=1)
        vectors = []
        sumNormals = om.MVector()
        for i in range(0,len(normals),3):
            x = normals[i]
            y = normals[i + 1]
            z = normals[i + 2]
            single_normal = [x,y,z]
            Asvector = om.MVector(single_normal)
            sumNormals += Asvector
            vectors.append(vectors)
        vertex_normal = sumNormals/len(vectors)
        YAxis = vertex_normal
        XAxis = YAxis ^ om.MVector.kXaxisVector
        if XAxis == om.MVector.kZeroVector:
            XAxis = YAxis ^ om.MVector.kYaxisVector
        ZAxis = XAxis ^ YAxis
        ZPoint = om.MPoint(ZAxis.normalize())
        ZPoint.w = 0
        XPoint = om.MPoint(XAxis.normalize())
        XPoint.w = 0
        YPoint = om.MPoint(YAxis.normalize())
        YPoint.w = 0
        position = cmds.xform(vert,q=True,t=True)
        position.append(1)
        Matrix_child = om.MMatrix([XPoint,YPoint,ZPoint,position])
        Matrix_parent = om.MMatrix(cmds.xform(mesh_name,q=True,m=True,ws=True))
        Matrix = Matrix_child * Matrix_parent
        Matrix = self.normalize_matrix_Axis(Matrix)
        return Matrix

    def get_edge_matrix(self,edge):
        selection = om.MSelectionList()
        selection.add(edge)
        if selection.getComponent(0)[1].apiType() != om.MFn.kMeshEdgeComponent:
            return
        edgeToVtx = cmds.polyInfo(edge,ev=1)[0]
        matches = re.findall('[-+]?[0-9]*\.?[0-9]+',edgeToVtx)
        VtxIDs = map(int, matches[-2:])
        Verts = []
        for v in VtxIDs:
            Verts.append("{}.vtx[{}]".format(edge.split(".e[")[0],v))
        
        v1 = self.get_vert_matrix(Verts[0])
        v2 = self.get_vert_matrix(Verts[1])
        
        avgMat = (v1 + v2) * 0.5
        Matrix = self.normalize_matrix_Axis(avgMat)
        return Matrix

    def get_face_matrix(self,face):
        selection = om.MSelectionList()
        selection.add(face)
        if selection.getComponent(0)[1].apiType() != om.MFn.kMeshPolygonComponent:
            return

        faceToVtx = cmds.polyInfo(face,fv=1)[0]
        matches = re.findall('[-+]?[0-9]*\.?[0-9]+',faceToVtx)
        VtxIDs = map(int, matches[1:])
        Verts = []
        for v in VtxIDs:
            Verts.append("{}.vtx[{}]".format(face.split(".f[")[0],v))
        MatSum = om.MMatrix([0] * 16)
        for v in Verts:
            MatSum+=self.get_vert_matrix(v)
        
        avgMat = MatSum * (1.0/len(Verts))
        Matrix = self.normalize_matrix_Axis(avgMat)
        return Matrix

    def get_CV_matrix(self,CV):
        selection = om.MSelectionList()
        selection.add(CV)
        if selection.getComponent(0)[1].apiType() != om.MFn.kCurveCVComponent:
            return
        curve_name = CV.split(".cv[")[0]
        cvID = int(re.search('\[(\d+)\]',CV).group(1))
        sel = om.MSelectionList()
        sel.add(curve_name)
        Node = sel.getDependNode(0)
        dagPath = om.MDagPath.getAPathTo(Node)
        curveFn = om.MFnNurbsCurve(dagPath)
        cv_pos = curveFn.cvPosition(cvID, om.MSpace.kWorld)
        closest_pnt, param = curveFn.closestPoint(cv_pos,space=om.MSpace.kWorld)
        domain = curveFn.knotDomain
        if param >= domain[1]:
            param-= 0.00001
        elif param <= domain[0]:
            param = 0.00001
        normal = curveFn.normal(param,om.MSpace.kWorld).normalize()
        tangent = curveFn.tangent(param,om.MSpace.kWorld).normalize()
        bitangent = (tangent ^ normal).normalize()
        YAxis = om.MPoint(normal)
        YAxis.w = 0
        XAxis = om.MPoint(tangent)
        XAxis.w = 0
        ZAxis = om.MPoint(bitangent)
        ZAxis.w = 0
        Matrix = om.MMatrix([XAxis,YAxis,ZAxis,closest_pnt])
        return Matrix

    def get_ep_matrix(self,ep):
        selection = om.MSelectionList()
        selection.add(ep)
        if selection.getComponent(0)[1].apiType() != om.MFn.kCurveEPComponent:
            return
        curve_name = ep.split(".ep[")[0]
        selection.clear()
        selection.add(curve_name)
        Node = selection.getDependNode(0)
        dagPath = om.MDagPath.getAPathTo(Node)
        curveFn = om.MFnNurbsCurve(dagPath)
        ep_pos = om.MPoint(cmds.xform(ep,q=True,t=True,ws=True))
        closest_pnt, param = curveFn.closestPoint(ep_pos)
        domain = curveFn.knotDomain
        if param >= domain[1]:
            param-= 0.00001
        elif param <= domain[0]:
            param = 0.00001
        normal = curveFn.normal(param,om.MSpace.kWorld).normalize()
        tangent = curveFn.tangent(param,om.MSpace.kWorld).normalize()
        bitangent = (tangent ^ normal).normalize()
        YAxis = om.MPoint(normal)
        YAxis.w = 0
        XAxis = om.MPoint(tangent)
        XAxis.w = 0
        ZAxis = om.MPoint(bitangent)
        ZAxis.w = 0
        Matrix = om.MMatrix([XAxis,YAxis,ZAxis,ep_pos])
        return Matrix

    def get_Matrix(self,loc):
        Mat = om.MMatrix.kIdentity
        selection = om.MSelectionList()
        selection.add(loc)
        if selection.getComponent(0)[1].apiType() == om.MFn.kMeshVertComponent:
            Mat = self.get_vert_matrix(loc)
        elif selection.getComponent(0)[1].apiType() == om.MFn.kMeshEdgeComponent:
            Mat = self.get_edge_matrix(loc)
        elif selection.getComponent(0)[1].apiType() == om.MFn.kMeshPolygonComponent:
            Mat = self.get_face_matrix(loc)
        elif selection.getComponent(0)[1].apiType() == om.MFn.kCurveCVComponent:
            Mat = self.get_CV_matrix(loc)
        elif selection.getComponent(0)[1].apiType() == om.MFn.kCurveEPComponent:
            Mat = self.get_ep_matrix(loc)
        else:
            cmds.xform(loc,cpc=True)
            self.bakeCustomToolPivot(loc)
            Mat = cmds.xform(loc,q=True,m=True,ws=True)
        return Mat

    def normalize_matrix_Axis(self,matrix):
        xAxis = om.MVector([matrix[i] for i in range(3)]).normalize()
        xAxis = om.MPoint(xAxis)
        xAxis.w = 0
        yAxis = om.MVector([matrix[i] for i in range(4,7)]).normalize()
        yAxis = om.MPoint(yAxis)
        yAxis.w = 0
        zAxis = om.MVector([matrix[i] for i in range(8,11)]).normalize()
        zAxis = om.MPoint(zAxis)
        zAxis.w = 0
        position = om.MPoint([matrix[i] for i in range(12,16)])
        Matrix = om.MMatrix([xAxis,yAxis,zAxis,position])
        return Matrix

    def get_rotation(self):
        rot_x,rot_y,rot_z = 0 , 0 , 0

        if self.random_rotX_chkbox.isChecked():
            minX = self.min_rotX_spinbox.value()
            maxX = self.max_rotX_spinbox.value()
            rot_x = random.SystemRandom().uniform(minX,maxX)
        if self.random_rotY_chkbox.isChecked():
            minY = self.min_rotY_spinbox.value()
            maxY = self.max_rotY_spinbox.value()
            rot_y = random.SystemRandom().uniform(minY,maxY)
        if self.random_rotZ_chkbox.isChecked():
            minZ = self.min_rotZ_spinbox.value()
            maxZ = self.max_rotZ_spinbox.value()
            rot_z = random.SystemRandom().uniform(minZ,maxZ)
        
        return [rot_x , rot_y , rot_z]

    def bakeCustomToolPivot(self,obj, pos=1, ori=1):

        objects = cmds.ls(obj, transforms=1)
        shapes = cmds.ls(obj, shapes=1)
        if len(shapes) > 0:
            transforms = cmds.listRelatives(path=1, parent=1, type='transform')
            objects += transforms

        if len(objects) == 0:
            cmds.error("m_bakeCustomToolPivot.kNoObjectsSelectedError")
            return None

        currentCtx = cmds.currentCtx()
        customOri = []
        otherToolActive = 0
        pivotModeActive = 0
        customModeActive = 0
        if currentCtx == "moveSuperContext" or currentCtx == "manipMoveContext":
            customOri = cmds.manipMoveContext('Move', q=1, orientAxes=1)
            pivotModeActive = cmds.manipMoveContext('Move', q=1, editPivotMode=1)
            customModeActive = cmds.manipMoveContext('Move', q=1, mode=1) / 6
        elif currentCtx == "RotateSuperContext" or currentCtx == "manipRotateContext":
            customOri = cmds.manipRotateContext('Rotate', q=1, orientAxes=1)
            pivotModeActive = cmds.manipRotateContext('Rotate', q=1, editPivotMode=1)
            customModeActive = cmds.manipRotateContext('Rotate', q=1, mode=1) / 3
        elif currentCtx == "scaleSuperContext" or currentCtx == "manipScaleContext":
            customOri = cmds.manipScaleContext('Scale', q=1, orientAxes=1)
            pivotModeActive = cmds.manipScaleContext('Scale', q=1, editPivotMode=1)
            customModeActive = cmds.manipScaleContext('Scale', q=1, mode=1) / 6
        else:
            customOri = cmds.manipMoveContext('Move', q=1, orientAxes=1)
            pivotModeActive = cmds.manipMoveContext('Move', q=1, editPivotMode=1)
            customModeActive = cmds.manipMoveContext('Move', q=1, mode=1) / 6
            otherToolActive = 1

        if ori and not pos and not customModeActive:
            if otherToolActive:
                cmds.error("m_bakeCustomToolPivot.kWrongAxisOriToolError")
            else:
                cmds.error("m_bakeCustomToolPivot.kWrongAxisOriModeError")
            return None

        # Get custom orientation
        if ori and customModeActive:
            customOri[0] = mel.eval('rad_to_deg({})'.format(customOri[0]))
            customOri[1] = mel.eval('rad_to_deg({})'.format(customOri[1]))
            customOri[2] = mel.eval('rad_to_deg({})'.format(customOri[2]))
            # Set object(s) rotation to the custom one (preserving child transform positions and geometry positions)
            cmds.rotate(customOri[0], customOri[1], customOri[2], objects, a=1, pcp=1, pgp=1, ws=1, fo=1)

        if pos:
            for object in objects:
                # Get pivot in parent space
                # object = 'pSphere4'            
                old = [0, 0, 0]
                m = cmds.xform(object, q=1, m=1)
                p = cmds.xform(object, q=1, os=1, sp=1)
                old[0] = (p[0] * m[0] + p[1] * m[4] + p[2] * m[8] + m[12])
                old[1] = (p[0] * m[1] + p[1] * m[5] + p[2] * m[9] + m[13])
                old[2] = (p[0] * m[2] + p[1] * m[6] + p[2] * m[10] + m[14])

                # Zero out pivots
                cmds.xform(objects, zeroTransformPivots=1)

                # Translate object(s) back to previous pivot (preserving child transform positions and geometry positions)
                new = cmds.getAttr(object + ".translate")[0]
                cmds.move((old[0] - new[0]), (old[1] - new[1]), (old[2] - new[2]), object, pcp=1, pgp=1, ls=1, r=1)

        # Exit pivot mode
        if pivotModeActive:
            mel.eval('ctxEditMode;')

        # Set the axis orientation mode back to object
        if ori and customModeActive:
            if currentCtx == "moveSuperContext" or currentCtx == "manipMoveContext":
                cmds.manipMoveContext('Move', e=1, mode=0)
            elif currentCtx == "RotateSuperContext" or currentCtx == "manipRotateContext":
                cmds.manipRotateContext('Rotate', e=True, mode=0)
            elif currentCtx == "scaleSuperContext" or currentCtx == "manipScaleContext":
                cmds.manipScaleContext('Scale', e=1, mode=0)
            else:
                cmds.manipPivot(moveToolOri = 0)
                cmds.manipPivot(ro = 1)

    @undo
    def Distribute(self):
        
        objs=self.get_list_elements(self.Objlist)
        locs=self.get_list_elements(self.Loclist)
        if not self.match_rot_chkbox.isChecked():
            for loc in locs:
                try:
                    cmds.xform(loc,cpc=True)
                    self.bakeCustomToolPivot(loc)
                except:
                    pass
                Positions=cmds.xform(loc,q=True,t=True,ws=True)
                PositionsList = [Positions[i:i+3] for i in range(0,len(Positions),3)]
                sumPos = om.MVector()
                for pos in PositionsList:
                    sumPos += om.MVector(pos)
                AvgPos = sumPos / len(PositionsList)
                obj=random.choice(objs)
                if self.instance_chkbox.isChecked():
                    dup=cmds.duplicate(obj,rr=True,ilf=True)[0]
                else:
                    dup=cmds.duplicate(obj,rr=True)[0]
                cmds.xform(dup,cpc=True)
                self.bakeCustomToolPivot(dup)
                cmds.xform(dup,t=AvgPos,ws=True)
                rot = self.get_rotation()
                cmds.setAttr(dup+".r",*rot)
            return
        
        for loc in locs:
            Matrix = self.get_Matrix(loc)
            obj=random.choice(objs)
            if self.instance_chkbox.isChecked():
                dup=cmds.duplicate(obj,rr=True,ilf=True)[0]
            else:
                dup=cmds.duplicate(obj,rr=True)[0]
            cmds.xform(dup,cpc=True)
            self.bakeCustomToolPivot(dup)
            cmds.xform(dup,m=om.MMatrix.kIdentity,ws=True)
            cmds.setAttr(dup+".offsetParentMatrix",Matrix,typ="matrix")
            objScale = cmds.getAttr(obj+".s")[0]
            cmds.setAttr(dup+".s",*objScale)
            rot = self.get_rotation()
            cmds.setAttr(dup+".r",*rot)

        return

    def deleteWorkSpaceControl(self):
        try:
            cmds.deleteUI("DistributionWindowWorkspaceControl")
        except:
            pass

    @staticmethod
    def create():
        global Win
        # try:
        #     Win.close()
        # except:
        #     pass
        Win = DistributionScript()
        Win.show(dockable=True)
        
        return Win

DistributionScript.create()