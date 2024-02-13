# import the rigid body motion module
import rbm
import math
import numpy as np

if __name__ == "__main__":
	halfpi = math.pi/2 #set psi, theta, phi to be pi/2
	x = rbm.rot_x(halfpi) #call rot_x from rbm.py
	y = rbm.rot_y(halfpi)
	z = rbm.rot_z(halfpi)
	firstRot = np.matmul(x, y)#matrix multiplication from numpy
	secRot = np.matmul(firstRot, z)

