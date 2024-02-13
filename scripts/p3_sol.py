#import problem 2 code
import p2_sol
import math
import numpy as np

def H_1():
	#Current axis'
	translationx = p2_sol.transformx(2.5) #translation of 2.5 on x
	translationz = p2_sol.transformz(0.5)#trans .5 on z
	translationy = p2_sol.transformy(-1.5)#trans -1.5 on y
	
	result = translationx @ translationz @ translationy #calculate matrices product

def H_2():
	#current axis'
	translationz = p2_sol.transformz(0.5)#trans of 0.5 on z
	translationx = p2_sol.transformx(2.5)#translation of 2.5 
	translationy = p2_sol.transformy(-1.5)#trans of -1.5 on y
	
	result = translationz @ translationx @ translationy #calculate mult matrices

def H_3():
	#fixed frame
	translationy = p2_sol.transformy(-1.5)
	translationz = p2_sol.transformz(0.5)
	translationx = p2_sol.transformx(2.5)

	result = translationy @ translationz @ translationx #multiply inverse

def H_4():
	#fixed frame
	translationy = p2_sol.transformy(-1.5)
	translationx = p2_sol.transformx(2.5)
	translationz = p2_sol.transformz(0.5)
	
	result = translationy @ translationx @ translationz#mult inverse

def H_5():
	rotationx = p2_sol.rotx(math.pi/2) #rotate x at pi/2
	translationx = p2_sol.transformx(3.0) #trans x by 3.0
	translationz = p2_sol.transformz(-3.0) #trans z by 3.0
	rotationz = p2_sol.rotz(-(math.pi/2)) #rotate z by -pi/2

	result = rotationx @ translationx @ translationz @ rotationz
