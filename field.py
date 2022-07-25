from math import *
from model import Model, create_model
from vtk.vtkFiltersSources import vtkCubeSource, vtkCylinderSource

class Field:
	def __init__(self, n, typ, renderer):
		self.models = []
		self.x = 50
		self.type = typ.upper()
		self.types = {"FSR": (self.make_FSR, 	self.check_FSR),
					  "F2" : (self.make_F2_F4, 	self.check_F2_F4),
					  "F4" : (self.make_F2_F4, 	self.check_F2_F4),
					  "F3" : (self.make_F3, 	self.check_F3)}
		u = -5
		self.types[self.type][0](renderer, u)
		colors = [(255, 0, 0), (255, 128, 0), (255, 255, 0), (0, 255, 0), (255, 0, 255), (0, 255, 255)]
		for i in range(n):
			color = colors[i]
			self.models.append(Model(renderer, (-n/2+i*2, u, self.x/3), color, i))

	def step(self):
		for m in self.models:
			m.step()

	def make_FSR(self, renderer, u):
		for e in [(-self.x, u, 0), (self.x, u, 0), (0, u, -sqrt(3)*self.x)]:
			actor = create_model(vtkCylinderSource())
			actor.SetPosition(e)
			renderer.AddActor(actor)
	
	def make_F2_F4(self, renderer, u):
		self.make_FSR(renderer, u)
		x = self.x
		s3 = sqrt(3)
		data = [(-x-2, u, s3*2), (x+2, u, s3*2), (0, u, -s3*x-4), 
				(-2, u, 0), (2, u, 0), (-x/2-1, u, -s3*(x/2-1)), (-x/2+1, u, -s3*(x/2+1)), 
				(x/2+1, u, -s3*(x/2-1)), (x/2-1, u, -s3*(x/2+1))]
		for e in data:
			actor = create_model(vtkCylinderSource())
			actor.SetPosition(e)
			renderer.AddActor(actor)
	
	def make_F3(self, renderer, u):
		self.make_F2_F4(renderer, u)

	def check_FSR(self, renderer):
		pass

	def check_F2_F4(self, renderer):
		pass

	def check_F3(self, renderer):
		pass
