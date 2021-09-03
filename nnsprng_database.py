import os
import math
def use_vector(lattice):
    cell=()
    lname=""
    nearest=1
    sc=((0,0,0))
    
    bcc=((0,0,0),\
         (0.5,0.5,0.5))
    
    fcc=((0,0,0),\
      (0.5,0,0.5),\
      (0,0.5,0.5),\
      (0.5,0.5,0))
    
    diamond=((0,0,0),\
      (0.5,0,0.5),\
      (0,0.5,0.5),\
      (0.5,0.5,0),\
      (0.25,0.25,0.25),\
      (0.75,0.75,0.25),\
      (0.75,0.25,0.75),\
      (0.25,0.75,0.75))
    
    if lattice=="sc":
        cell=sc
        lname="scubic"
        nearest=(1/2)
    if lattice=="bcc":
        cell=bcc
        lname="bccubic"
        nearest=(0.866/2)
    if lattice=="fcc":
        cell=fcc
        lname="fccubic"
        nearest=(0.70/2)
    if lattice=="diamond":
        cell=diamond
        lname="diamond"
        nearest=(0.433/2)
    
    
    return(cell,lname,nearest)

def get_atomic_weight(isim):
    w={'H':1.008,'He':4.002,'Li':6.94,'Be':9.012,'B':10.81,'C':12.011,'N':14.007,'O':15.99,'F':18.998,\
       'Ne':20.179,'Na':22.989,'Mg':24.304,'Al':26.982,'Si':28.085,'P':30.973,'S':32.060,'Cl':35.450,'Ar':39.948,'K':39.098,\
       'Ca':40.078,'Sc':44.955,'Ti':47.867,'V':50.941,'Cr':51.996,'Mn':55.938,'Fe':55.845,'Co':58.933,'Ni':58.693,'Cu':63.546,\
       'Zn':65.38,'Ga':69.723,'Ge':72.630,'As':74.921,'Se':78.971,'Br':79.904,'Kr':83.798,'Rb':85.467,'Sr':87.62,'Y':88.905,\
       'Zr':91.224,'Nb':92.906,'Mo':95.95,'Tc':97,'Ru':101.07,'Rh':102.905,'Pd':106.42,'Ag':107.868,'Cd':112.414,'In':114.818,\
       'Sn':118.710,'Sb':121.760,'Te':127.60,'I':126.904,'Xe':131.293,'Cs':132.905,'Ba':137.327,'La':138.905,'Ce':140.116,'Pr':140.907,\
       'Nd':144.242,'Pm':145,'Sm':150.36,'Eu':151.964,'Gd':157.25,'Tb':158.925,'Dy':162.500,'Ho':164.930,'Er':167.259,'Tm':168.934,\
       'Yb':173.045,'Lu':174.966,'Hf':178.486,'Ta':180.947,'W':183.84,'Re':186.207,'Os':190.23,'Ir':190.217,'Pt':195.084,'Au':196.966,\
       'Hg':200.952,'Tl':204.38,'Pb':207.2,'Bi':208.980,'Po':209,'At':210,'Rn':222,'Fr':223,'Ra':226,'Ac':227,\
       'Th':232.0377,'Pa':231.035,'U':238.028,'Np':237,'Pu':244,'Am':243,'Cm':247,'Bk':247,'Cf':251,'Es':252,\
       'Fm':257,'Md':258,'No':259,'Lr':262,'Rf':267,'Db':270,'Sg':269,'Bh':270,'Hs':270,'Mt':278,\
       'Ds':281,'Rg':281,'Cn':285,'Nh':286,'Fl':289,'Mc':289,'Lv':293,'Ts':293,'Og':294}



    weight=w.get(isim)
    return(weight)