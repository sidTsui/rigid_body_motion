import math
import numpy as np
#used "Basic Homogenous Transformation" side 46 formulas
def transformx(a): 
	transx = np.array([[1.0,  0.0, 0.0, a],
				    [0.0, 1.0, 0.0, 0.0],
				    [0.0, 0.0, 1.0, 0.0],
					[0.0, 0.0, 0.0, 1.0]])
	return transx

def transformy(b):
	transy = np.array([[1.0,  0.0, 0.0, 0.0],
				    [0.0, 1.0, 0.0, b],
				    [0.0, 0.0, 1.0, 0.0],
					[0.0, 0.0, 0.0, 1.0]])
	return transy

def transformz(c):
	transz = np.array([[1.0,  0.0, 0.0, 0.0],
				    [0.0, 1.0, 0.0, 0.0],
				    [0.0, 0.0, 1.0, c],
					[0.0, 0.0, 0.0, 1.0]])
	return transz

def rotationx(a): #alpha
	rotx = np.array([[1.0,  0.0, 0.0, 0.0],
				    [0.0, math.cos(a), -math.sin(a), 0.0],
					[0.0, math.sin(a), math.cos(a), 0.0],
					[0.0,  0.0, 0.0, 1.0]])
	return rotx
	
def rotationy(b): #beta
	roty = np.array([[math.cos(b),  0.0, math.sin(b), 0.0],
				    [0.0, 1.0, 0.0, 0.0],
					[-math.sin(b), 0.0, math.cos(b), 0.0],
					[0.0,  0.0, 0.0, 1.0]])
	return roty
	
def rotationz(g): #gamma
	rotz = np.array([[math.cos(g),  -math.sin(g), 0.0, 0.0],
				    [math.sin(g), math.cos(g), 0.0, 0.0],
					[0.0, 0.0, 1.0, 0.0],
					[0.0,  0.0, 0.0, 1.0]])
	return rotz
