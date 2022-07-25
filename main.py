#!/usr/bin/env python


import vtk.vtkInteractionStyle
import vtk.vtkRenderingOpenGL2


from field import Field
from vtk import vtkCommand
from vtk.vtkCommonColor import vtkNamedColors
from vtk.vtkRenderingCore import (
	vtkActor,
	vtkPolyDataMapper,
	vtkLight,
	vtkRenderWindow,
	vtkRenderWindowInteractor,
	vtkRenderer
)


class vtkTimerCallback(vtkCommand):
	def __new__(self, caller, eventId):
		global field
		if ("TimerEvent" == eventId):
			field.step()
			caller.Render()
		return self


def main():
	global field
	colors = vtkNamedColors()
	bkg = map(lambda x: x / 255.0, [0, 0, 255, 255])
	colors.SetColor("BkgColor", *bkg)

	ren = vtkRenderer()
	renWin = vtkRenderWindow()
	renWin.AddRenderer(ren)
	iren = vtkRenderWindowInteractor()
	iren.SetRenderWindow(renWin)

	ren.SetBackground(colors.GetColor3d("BkgColor"))
	renWin.SetSize(1920, 1080)
	renWin.SetWindowName('Trainer')

	renWin.Render()
	iren.Initialize()
	field = Field(1, "Fsr", ren)
	cb = vtkTimerCallback(iren, None)
	iren.AddObserver(vtkCommand.TimerEvent, cb);
	iren.CreateRepeatingTimer(10)
	iren.Start()


if __name__ == '__main__':
	main()
