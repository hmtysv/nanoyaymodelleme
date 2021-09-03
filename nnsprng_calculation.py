import math
import os
import nnsprng_calculation as cal

def spring_cross_section(boxz2,r,Ps,R):
    pi=math.pi
    u1=((boxz2-r)/Ps)*pi
    u2=((boxz2+r)/Ps)*pi
    unet=u2-u1
    elipsa=unet*R/2
    alan=elipsa*r*pi
    return(alan)
def spring_axis(x,y,z,R,gap):
    x=x+(3*R)
    y=y+(3*R)
    z=z+gap
    return(x,y,z)
def sim_box(R,lowz,highz,gap):
    boxx=6*R
    boxy=6*R
    boxz1=lowz
    boxz2=highz+gap


    return(boxx,boxy,boxz1,boxz2)
    

