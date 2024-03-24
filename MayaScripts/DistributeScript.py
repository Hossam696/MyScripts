
from PySide2 import QtCore, QtGui, QtWidgets
import maya.cmds as cmds
import maya.api.OpenMaya as om
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
        self.centralwidget = QtWidgets.QWidget(DistributionWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Distribute_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Distribute_btn.setObjectName("Distribute_btn")
        self.gridLayout.addWidget(self.Distribute_btn, 5, 0, 1, 1)
        self.txt_add_obj = QtWidgets.QLabel(self.centralwidget)
        self.txt_add_obj.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_add_obj.setObjectName("txt_add_obj")
        self.gridLayout.addWidget(self.txt_add_obj, 0, 0, 1, 1)
        self.ObjsLayout = QtWidgets.QHBoxLayout()
        self.ObjsLayout.setObjectName("ObjsLayout")
        self.Objlist = QtWidgets.QListWidget(self.centralwidget)
        self.Objlist.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.Objlist.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.Objlist.setObjectName("Objlist")
        self.ObjsLayout.addWidget(self.Objlist)
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
        self.txt_add_locs = QtWidgets.QLabel(self.centralwidget)
        self.txt_add_locs.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_add_locs.setObjectName("txt_add_locs")
        self.gridLayout.addWidget(self.txt_add_locs, 2, 0, 1, 1)
        self.LocationsLayout = QtWidgets.QHBoxLayout()
        self.LocationsLayout.setObjectName("LocationsLayout")
        self.Loclist = QtWidgets.QListWidget(self.centralwidget)
        self.Loclist.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.Loclist.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.Loclist.setObjectName("Loclist")
        self.LocationsLayout.addWidget(self.Loclist)
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
        self.RandomizationLayout = QtWidgets.QGridLayout()
        self.RandomizationLayout.setObjectName("RandomizationLayout")
        self.max_rotZ_spinbox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.max_rotZ_spinbox.setMaximum(360.0)
        self.max_rotZ_spinbox.setProperty("value", 360.0)
        self.max_rotZ_spinbox.setObjectName("max_rotZ_spinbox")
        self.max_rotZ_spinbox.setEnabled(False)
        self.RandomizationLayout.addWidget(self.max_rotZ_spinbox, 7, 2, 1, 1)
        self.min_rotZ_spinbox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.min_rotZ_spinbox.setMaximum(360.0)
        self.min_rotZ_spinbox.setObjectName("min_rotZ_spinbox")
        self.min_rotZ_spinbox.setEnabled(False)
        self.RandomizationLayout.addWidget(self.min_rotZ_spinbox, 7, 1, 1, 1)
        self.match_rot_chkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.match_rot_chkbox.setObjectName("match_rot_chkbox")
        self.RandomizationLayout.addWidget(self.match_rot_chkbox, 4, 0, 1, 1)
        self.min_rotX_spinbox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.min_rotX_spinbox.setMaximum(360.0)
        self.min_rotX_spinbox.setObjectName("min_rotX_spinbox")
        self.min_rotX_spinbox.setEnabled(False)
        self.RandomizationLayout.addWidget(self.min_rotX_spinbox, 5, 1, 1, 1)
        self.min_rotY_spinbox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.min_rotY_spinbox.setMaximum(360.0)
        self.min_rotY_spinbox.setObjectName("min_rotY_spinbox")
        self.min_rotY_spinbox.setEnabled(False)
        self.RandomizationLayout.addWidget(self.min_rotY_spinbox, 6, 1, 1, 1)
        self.max_rotY_spinbox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.max_rotY_spinbox.setMaximum(360.0)
        self.max_rotY_spinbox.setProperty("value", 360.0)
        self.max_rotY_spinbox.setObjectName("max_rotY_spinbox")
        self.max_rotY_spinbox.setEnabled(False)
        self.RandomizationLayout.addWidget(self.max_rotY_spinbox, 6, 2, 1, 1)
        self.random_rotY_chkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.random_rotY_chkbox.setObjectName("random_rotY_chkbox")
        self.RandomizationLayout.addWidget(self.random_rotY_chkbox, 6, 0, 1, 1)
        self.random_rotZ_chkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.random_rotZ_chkbox.setObjectName("random_rotZ_chkbox")
        self.RandomizationLayout.addWidget(self.random_rotZ_chkbox, 7, 0, 1, 1)
        self.max_rotX_spinbox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.max_rotX_spinbox.setMaximum(360.0)
        self.max_rotX_spinbox.setProperty("value", 360.0)
        self.max_rotX_spinbox.setObjectName("max_rotX_spinbox")
        self.max_rotX_spinbox.setEnabled(False)
        self.RandomizationLayout.addWidget(self.max_rotX_spinbox, 5, 2, 1, 1)
        self.random_rotX_chkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.random_rotX_chkbox.setObjectName("random_rotX_chkbox")
        self.RandomizationLayout.addWidget(self.random_rotX_chkbox, 5, 0, 1, 1)
        self.gridLayout.addLayout(self.RandomizationLayout, 4, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 1, 0, 1, 1)
        DistributionWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DistributionWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 421, 21))
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
        self.Distribute_btn.setText(_translate("DistributionWindow", "Distribute!"))
        self.txt_add_obj.setText(_translate("DistributionWindow", "Add Objects to Distribute"))
        self.obj_add_btn.setText(_translate("DistributionWindow", "Add"))
        self.obj_rmv_btn.setText(_translate("DistributionWindow", "Remove"))
        self.obj_clr_btn.setText(_translate("DistributionWindow", "Clear"))
        self.txt_add_locs.setText(_translate("DistributionWindow", "Add Distribute Locations"))
        self.Locs_add_btn.setText(_translate("DistributionWindow", "Add"))
        self.Locs_rmv_btn.setText(_translate("DistributionWindow", "Remove"))
        self.Locs_clr_btn.setText(_translate("DistributionWindow", "Clear"))
        self.match_rot_chkbox.setText(_translate("DistributionWindow", "Match Rotation to Normal"))
        self.random_rotY_chkbox.setText(_translate("DistributionWindow", "Random Rotation Y"))
        self.random_rotZ_chkbox.setText(_translate("DistributionWindow", "Random Rotation Z"))
        self.random_rotX_chkbox.setText(_translate("DistributionWindow", "Random Rotation X"))

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
            print(selection.getComponent(0)[1].apiType())
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

    def get_face_matrix_old(self,face):
        selection = om.MSelectionList()
        selection.add(face)
        if selection.getComponent(0)[1].apiType() != om.MFn.kMeshPolygonComponent:
            print(selection.getComponent(0)[1].apiType())
            return

        faceInfo = cmds.polyInfo(face,fn=1)[0]
        matches = re.findall('[-+]?[0-9]*\.?[0-9]+',faceInfo)
        faceNormal = map(float, matches[-3:])
        YAxis = om.MVector(faceNormal)
        XAxis = YAxis ^ om.MVector.kXaxisVector
        ZAxis = XAxis ^ YAxis
        ZPoint = om.MPoint(ZAxis.normalize())
        ZPoint.w = 0
        XPoint = om.MPoint(XAxis.normalize())
        XPoint.w = 0
        YPoint = om.MPoint(YAxis.normalize())
        YPoint.w = 0
        positions = cmds.xform(face,q=True,t=True,ws=True)
        positions_list = [positions[i:i+3] for i in range(0,len(positions),3)]
        sum_positions = om.MVector()
        for pos in positions_list:
            sum_positions += om.MVector(pos)
        
        position = sum_positions / len(positions_list)
        position = om.MPoint(position)
        Matrix = om.MMatrix([XPoint,YPoint,ZPoint,position])

        return Matrix

    def get_face_matrix(self,face):
        selection = om.MSelectionList()
        selection.add(face)
        if selection.getComponent(0)[1].apiType() != om.MFn.kMeshPolygonComponent:
            print(selection.getComponent(0)[1].apiType())
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
        # Matrix_parent = om.MMatrix(cmds.xform(curve_name,q=True,m=True,ws=True))
        # Matrix = Matrix_child * Matrix_parent
        return Matrix

    def get_ep_matrix(self,ep):
        selection = om.MSelectionList()
        selection.add(ep)
        if selection.getComponent(0)[1].apiType() != om.MFn.kCurveEPComponent:
            return
        curve_name = ep.split(".ep[")[0]
        sel = om.MSelectionList()
        sel.add(curve_name)
        Node = sel.getDependNode(0)
        dagPath = om.MDagPath.getAPathTo(Node)
        curveFn = om.MFnNurbsCurve(dagPath)
        ep_pos = om.MPoint(cmds.xform(ep,q=True,t=True,ws=True))
        closest_pnt, param = curveFn.closestPoint(ep_pos)
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
        elif selection.getComponent(0)[1].apiType() == om.MFn.kTransform:
            Mat = cmds.xform(loc,q=True,m=True,ws=True)
        return Mat

    def normalize_matrix_Axis(self,matrix):
        xAxis = om.MVector([matrix[i] for i in range(3)]).normalize()
        xAxis = om.MPoint(xAxis)
        xAxis.w = 0
        print(xAxis)
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

    def Distribute_old(self):
        objs=self.get_list_elements(self.Objlist)
        locs=self.get_list_elements(self.Loclist)
        for loc in locs:
            location=cmds.xform(loc,q=1,t=1,ws=1)
            obj=random.choice(objs)
            dup=cmds.duplicate(obj,rr=1)[0]
            cmds.xform(dup,m=om.MMatrix.kIdentity,ws=True)
            cmds.setAttr(dup+".offsetParentMatrix",self.get_vert_matrix(loc),typ="matrix")
        return

    @undo
    def Distribute(self):
        
        objs=self.get_list_elements(self.Objlist)
        locs=self.get_list_elements(self.Loclist)
        if not self.match_rot_chkbox.isChecked():
            for loc in locs:
                Positions=cmds.xform(loc,q=True,t=True,ws=True)
                PositionsList = [Positions[i:i+3] for i in range(0,len(Positions),3)]
                sumPos = om.MVector()
                for pos in PositionsList:
                    sumPos += om.MVector(pos)
                AvgPos = sumPos / len(PositionsList)
                obj=random.choice(objs)
                dup=cmds.duplicate(obj,rr=True)[0]
                cmds.xform(dup,t=AvgPos,ws=True)
                rot = self.get_rotation()
                cmds.setAttr(dup+".r",*rot)
            return
        
        for loc in locs:
            Matrix = self.get_Matrix(loc)
            obj=random.choice(objs)
            dup=cmds.duplicate(obj,rr=1)[0]
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