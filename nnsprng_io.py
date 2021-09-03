import os
import math
import nnsprng_calculation as calc
import nnsprng_database as db

def input_spring():
    print("Element kısaltmasını girin\n")
    isim=input()
    print(isim + " birim hücre yapısını seçin\n"
          "SC  için 0\n"
          "BCC için 1\n"
          "FCC için 2\n"
          "Elmas için 3\n")
    lattice=int(input())
    print("Angstrom olarak lattice uzunluğunu giriniz\n")
    a=float(input())
    print("Helix'in yaricapini giriniz\n")
    R=float(input())
    print("Yayin yaricapini giriniz\n")
    r=float(input())
    print("Yayin araligini giriniz\n")
    p=float(input())
    print("Dönme sayısını giriniz\n")
    N=int(input())
    print("calculating... \n")

    return(isim,lattice,a,R,r,p,N)



def output_spring(atomlist,isiml,lname,R,r,p,N,lowz,highz,a,Ps,rl):
    isim=""
    for i in range(len(isiml)):
        isim=isim+isiml[i]+"_r"+str(rl[i+1]-rl[i])+"."+str(lname[i])+"-"

    outxyz = open("Nanospring-{0}-R{1}-r{2}-p{3}-N{4}.xyz".format(isim,R,r,p,N), "w")
    outxml = open("Nanospring-{0}-R{1}-r{2}-p{3}-N{4}.xml".format(isim,R,r,p,N), "w")
    outlmp = open("Nanospring-{0}-R{1}-r{2}-p{3}-N{4}.lmp".format(isim,R,r,p,N), "w")
    
    num=1
    
    yarigraphic = a/8   
    toplam=len(atomlist)
    
    boxx,boxy,boxz1,boxz2=calc.sim_box(R,lowz,highz,a)
    
    alan=calc.spring_cross_section(boxz2,r,Ps,R)

    
    
################################################

    print("writing file \n")
    
    
    outxml.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n"
                 "<Model xmlns=\"http://atom.fourelem.com/ns/2016\">\n"
                 "<Group>\n")
    
    outlmp.write("#simbox x={0:9.5f} y={1:9.5f} z={2:9.5f}-{3:9.5f} \\\\ kesit alanı{4:9.3f}\n\n".format(boxx,boxy,boxz1,boxz2,alan))
    outlmp.write("{0:9d}  atoms\n"
                  "         {1}  atom types\n\n"
                  "0.00000      {2:9.5f}  xlo xhi\n"
                  "0.00000      {3:9.5f}  ylo yhi\n"
                  "{4:9.5f}      {5:9.5f}  zlo zhi\n".format(toplam,len(isiml),boxx,boxy,boxz1,boxz2))
    outlmp.write("\nMasses\n\n")
    for s in range(0,len(isiml)):
        
        weight=db.get_atomic_weight(isiml[s])              
        outlmp.write(             "{0:2d} {1:3.8f}  #{2}\n".format(s+1,weight,isiml[s]))

    outlmp.write("\nAtoms # atomic\n\n")
    
    outxyz.write(str(toplam)+"\nsimbox x={0:9.5f} y={1:9.5f} z={2:9.5f}-{3:9.5f} \\\\ Yatay kesit alanı{4:9.3f}\n".format(boxx,boxy,boxz1,boxz2,alan))
    ##
    for n in range (0,toplam):
        outlmp.write("{0:9d}    {1:2d}    {2:9.5f}      {3:9.5f}      {4:9.5f}\n".format(atomlist[n][0],atomlist[n][1],atomlist[n][3],atomlist[n][4],atomlist[n][5]))
        outxml.write('<Ball Id=\"{0}{1}\" Position=\"{2:9.5f},{3:9.5f},{4:9.5f}\" Radius=\"{5:9.5f}\" Color=\"Orange\"/>\n'.format(atomlist[n][2],atomlist[n][0],atomlist[n][3],atomlist[n][4],atomlist[n][5],yarigraphic))
        outxyz.write("{0} {1:9.5f} {2:9.5f} {3:9.5f}\n".format(atomlist[n][2],atomlist[n][3],atomlist[n][4],atomlist[n][5]))

    outxml.write("</Group>\n</Model>")
    outxml.close()
    outxyz.close()
    outlmp.close()
    print("\nişlem tamamlandı")

def output_spring1(atomlist,isim,lname,R,r,p,N,lowz,highz,a,Ps):
    num=1
    weight=db.get_atomic_weight(isim)
    yarigraphic = a/8
    
    toplam=len(atomlist)
    print(toplam)
    print(atomlist)
    boxx=(4*(R+r));boxy=(4*(R+r));boxz1=lowz;boxz2=highz+a
    alan=calc.spring_cross_section(boxz2,r,Ps,R)
    
    outxyz = open("{0}-nanospring-{1}-{2}-{3}-{4}-{5}.xyz".format(isim,lname,R,r,p,N), "w")
    outxml = open("{0}-nanospring-{1}-{2}-{3}-{4}-{5}.xml".format(isim,lname,R,r,p,N), "w")
    outlmp = open("{0}-nanospring-{1}-{2}-{3}-{4}-{5}.lmp".format(isim,lname,R,r,p,N), "w")
################################################

    print("writing file \n")
    
    outxml.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n"
                 "<Model xmlns=\"http://atom.fourelem.com/ns/2016\">\n"
                 "<Group>\n")
    
    outlmp.write("#simbox x={0:9.5f} y={1:9.5f} z={2:9.5f}-{3:9.5f} \\\\ kesit alanı{4:9.3f}\n\n".format(boxx,boxy,boxz1,boxz2,alan))
    outlmp.write ("{0:9d}  atoms\n"
                  "         1  atom types\n\n"
                  "0.00000      {1:9.5f}  xlo xhi\n"
                  "0.00000      {2:9.5f}  ylo yhi\n"
                  "{3:9.5f}      {4:9.5f}  zlo zhi\n".format(toplam,boxx,boxy,boxz1,boxz2))
    outlmp.write("\nMasses\n\n    {0:2d} {1:3.8f}  #{2}\n\n"
                 "Atoms # atomic\n\n".format(num,weight,isim))
    
    outxyz.write(str(toplam)+"\nsimbox x={0:9.5f} y={1:9.5f} z={2:9.5f}-{3:9.5f} \\\\  yatay kesit alanı {4:9.3f}\n".format(boxx,boxy,boxz1,boxz2,alan))

    for n in range (0,toplam):
        outlmp.write("{0:9d}    1    {1:9.5f}      {2:9.5f}      {3:9.5f}\n".format(atomlist[n][0],atomlist[n][1],atomlist[n][2],atomlist[n][3]))
        outxml.write('<Ball Id=\"A{0}\" Position=\"{1:9.5f},{2:9.5f},{3:9.5f}\" Radius=\"{4:9.5f}\" Color=\"Orange\"/>\n'.format(atomlist[n][0],atomlist[n][1],atomlist[n][2],atomlist[n][3],yarigraphic))
        outxyz.write(isim+" {0:9.5f} {1:9.5f} {2:9.5f}\n".format(atomlist[n][1],atomlist[n][2],atomlist[n][3]))

    outxml.write("</Group>\n</Model>")
    outxml.close()
    outxyz.close()
    outlmp.close()
    print("\nişlem tamamlandı")
