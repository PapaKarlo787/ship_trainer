from math import *
from manipulator import Manipulator
from vtk.vtkFiltersSources import vtkCubeSource
from vtk.vtkCommonColor import vtkNamedColors
from vtk.vtkIOGeometry import vtkSTLReader

from vtk.vtkRenderingCore import (
	vtkActor,
	vtkPolyDataMapper,
	vtkRenderWindow,
	vtkRenderWindowInteractor
)

def create_model(source):
	modelMapper = vtkPolyDataMapper()
	modelMapper.SetInputConnection(source.GetOutputPort())
	
	actor = vtkActor()
	actor.SetMapper(modelMapper)
	return actor
 

class Model:
	def __init__(self, renderer, pos, color, n):
		reader = vtkSTLReader()
		reader.SetFileName("ship.stl")
		self.actor = create_model(reader)
		self.actor.SetPosition(pos)
		self.actor.SetScale(0.05)
		self.actor.GetProperty().SetColor(color)
		renderer.AddActor(self.actor)
		self.manip = Manipulator(n)
		self.pos = pos
		self.ungle = 0

	def step(self):
		mdata = self.manip.get_data()
		speed = mdata[0]*2
		c = lambda f, n: self.pos[n] - speed * f(self.ungle)
		self.pos = (c(sin, 0), self.pos[1], c(cos, 2))
		ungle = asin(mdata[1]*speed*speed/2)
		self.ungle += ungle
		self.actor.RotateY(ungle/pi*180)
		self.actor.SetPosition(self.pos)
