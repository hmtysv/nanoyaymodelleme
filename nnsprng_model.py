import math 
import os
import nnsprng_io as inout
import nnsprng_database as db
import nnsprng_calculation as cal

###3d yay Formuller
###x(u,v)=(R+rcosv)*cosu
###y(u,v)=(R+cosv)*sinu
###z(u,v)=rsinv+((P*u)/pi)
def nanospring(shell,liste):
    print(liste)
    print(shell)
    atomlist=[]
    isiml=[]
    al=[]
    rl=[]
    tl=[];tl.append(0)
    latticel=[]

##    print("Yay Kaç katmandan atomdan oluşuyor")

    for s in range(0,shell):
        
        element,lattice0,a0,R,t,p,N = liste[s]
        isiml.append(element)
        al.append(a0)
        tl.append(t)
        latticel.append(lattice0)
        
        
    pi=math.pi
    Nust=N+1
    Ps = p/2
    rl.append(0)
    for s in range(0,shell):
        rtotal=0
        for ra in range(0,s+2):
            
            rtotal=rtotal+tl[ra]
        rl.append(rtotal)
    print(rl)

    toplam = 0


    for s in range(0,shell):
        lattice=latticel[s]
        isim=isiml[s]
        a=al[s]
        r=rl[s+1]    
       
        cordzust=(Ps/pi)*((N*2*pi)+(r*pi/Ps))-r

        ustlimit=r+((Ps*((-r*pi/Ps)+(N*2*pi)))/pi)

        xf= int((r+R)/a);  xi=-xf
        yf=int((r+R)/a);  yi=-yf
        zf=int(r/a)+int((p*N)/a);  zi=0
         
        lowz =4;highz=4

       
        cell,lname,nearest = db.use_vector(lattice)
        
        ############iki malzeme arasında mesafe
        if shell>1:
            if s==0:
                rmin=rl[0]
                rmax=r-(nearest*a)
            elif s==shell-1:
                rmin=rl[s]+a*nearest
                rmax=r
            else:
                rmin=rl[s]+(al[s-1])*nearest
                rmax=r-(nearest*a)
        else:
            
            rmin=0;rmax=r
            
        ################## Bulk üretimi. Yayı içine alabilecek küp atomlar ile dolduruluyor    
        print(rmin,rmax)

        for i in range(xi-1,xf+1):
            
            for j in range(yi-1,yf+1):
            
                for k in range (zi,zf+1):
                    
                    for l in range (0,len(cell)):
                   
                            cordx =(i*a)+(a*cell[l][0])
                            cordy =(j*a)+(a*cell[l][1])
                            cordz =(k*a)+(a*cell[l][2])
                            
                            xyr=math.sqrt((cordx*cordx)+(cordy*cordy))

                            
                            if xyr<(R-r) or xyr>(R+r) :
                                continue
                            if cordz<0:
                                continue
                            if cordz > ustlimit:
                                continue

                            # x  ve y 0 olduğunda trigonometrik fonk. hata veriyor.Hatadan kaçınmak için
                            if 0.00001 > cordx > -0.00001:
                                cordx=0.1
                            if 0.00001 > cordy > -0.00001:
                                cordy=0.1
                                
##                          if cordz<a:
##                                continue

                            #finding u
                            u1=math.atan2(cordy,cordx)
                           
                            for m in range(0,int(Nust)):
                                
                             
                                zmerkez=(Ps*u1)/pi
                                fark=abs((cordz-zmerkez))
                               
                                if fark>r:
                                    u1=u1+(2*pi)
                            u=u1;
                            #finding v
                            v1=(cordz - (Ps*(u/pi)))
                            v2=(cordx / math.cos(u)) - R
                            v = math.atan2(v1,v2)
                            if v<0:
                                v=v+(2*pi)
             
                            rtest = ((cordx / math.cos(u)) - R )/ math.cos(v)
                            
                            
                            
                            #Atom yayın içinde ise atomliste ekleniyor 
                            
                            if rmax>rtest and rtest>=rmin:

                                #eksen yeniden oluşturuluyor
                                cordx,cordy,cordz=cal.spring_axis(cordx,cordy,cordz,R,a)
                                
     
                                if highz<cordz:
                                    highz=cordz
                                if cordz<lowz:
                                    lowz=cordz
                            
                                toplam+=1
                                atomlist.append((toplam,s+1,isim,cordx,cordy,cordz,shell))

    ##for atom in atomlist:
    ##    print(atom)

    inout.output_spring(atomlist,isiml,latticel,R,r,p,N,lowz,highz,a,Ps,rl)





