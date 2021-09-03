import nnsprng_model as spring
import os
import csv

def get_file_list(dirname):
    dir_list=[]
    os.chdir((os.path.abspath(dirname)))
    for directory in os.listdir():
        dir_list.append(directory)
    return dir_list

def csv_to_list(file_name):
    datalist=[]
    with open(file_name, encoding="utf8", newline='') as csvfile:
        
      
        spamreader = csv.reader(csvfile, delimiter=',')
        
        for row in spamreader:
            
            datalist.append(row)

    return datalist


files=get_file_list("batch")

for file in files:
    if "csv" in file:
        print(file)
print("\n--------------------")
secn=input("dosya ismini yaz\n")

for file in files:
    if secn in file:
        nanospring_list=csv_to_list(file)
for ns in range(1,len(nanospring_list)):
    st=[]
    shell=int((len(nanospring_list[ns])-3)/4)
    R=float(nanospring_list[ns][0])
    p=float(nanospring_list[ns][1])
    N=float(nanospring_list[ns][2])
    for s in range(0,shell):
        if nanospring_list[ns][(s*4)+3]=="":
            continue
        name=nanospring_list[ns][(s*4)+3]
        lattice=nanospring_list[ns][(s*4)+4]
        a=float(nanospring_list[ns][(s*4)+5])
        r=float(nanospring_list[ns][(s*4)+6])
        st.append([name,lattice,a,R,r,p,N])
    spring.nanospring(len(st),st)
        
        
    
        
        
#çıktı=[isim,lttc,a,R,r,p,N]
outlist=[["Al","fcc",2,40,10,50,2],["Cu","fcc",2.5,40,10,50,2]]
print(nanospring_list)
#spring.build(len(outlist),outlist)
