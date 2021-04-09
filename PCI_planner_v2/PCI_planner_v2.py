import csv
import math
import os
cwd = os.getcwd()

f = open('cells_new.csv')
csvf = csv.reader(f,delimiter = ';')

sitenames = []
lon = []
lat = []
cellnames = []

next(csvf)
for row in csvf:
    sitenames.append(row[0])
    lon.append(row[1])
    lat.append(row[2])
    cellnames.append(row[4])
    
    
f.close()



#PCI Allocation A
NCells = len(cellnames)

PCIalloc = [None] * NCells
allocount =[0]*99
PCIlist = [x for x in range(0, 99)]
for cid,item in enumerate(cellnames):
    for pcid,item2 in enumerate(PCIlist):
        if allocount[pcid] == 0:
            PCIalloc[cid] = item2
            allocount[pcid] = allocount[pcid] + 1
            break
    

for cid,item in enumerate(cellnames):
    dist = []
    if PCIalloc[cid] == None:
        for cid2,item2 in enumerate(cellnames):
            if PCIalloc[cid2] != None:
                maxround = max(allocount)
                minround = min(allocount)
                PCIchk = PCIalloc[cid2]
                if maxround != minround and allocount[PCIchk] == maxround:
                    disttemp = 0
                    dist.append(disttemp)
                else:
                    disttemp = (((float(lon[cid])-float(lon[cid2]))**(2)) + ((float(lat[cid])-float(lat[cid2]))**(2)))**(0.5)

                    dist.append(disttemp)
            else:
               
                maxvalue = max(dist)
                maxindex = dist.index(maxvalue)
                PCI = PCIalloc[maxindex]
                PCIalloc[cid] = PCI
                pcid = PCIlist.index(PCI)
                allocount[pcid] = allocount[pcid] + 1
                break
    

PCIallocA = PCIalloc
#Average Reuse Distance Per Code
PCIreuseDist = [0] * len(PCIlist)

for pcid,item in enumerate(PCIlist):
    
    indices = [i for i, xx in enumerate(PCIalloc) if xx == item]
    indices2 = indices 
    dist = []
    for j,cidx1 in enumerate(indices):
        for k,cidx2 in enumerate(indices2):
            if j != k:
                lat1 = float(lat[cidx1])
                lat2 = float(lat[cidx2])
                lon1 = float(lon[cidx1])
                lon2 = float(lon[cidx2])

                lat1 = lat1*(math.pi)/180
                lat2 = lat2*(math.pi)/180
                lon1 = lon1*(math.pi)/180
                lon2 = lon2*(math.pi)/180

                deltaLat = lat2-lat1
                deltaLon = lon2-lon1

                x = deltaLon*(math.cos((lat1+lat2)/2))
                y = deltaLat

                d = 6371*math.sqrt(x*x + y*y)
                dist.append(d)
    distavg = sum(dist) / len(dist)
    PCIreuseDist[pcid] = distavg

PCIreuseDistAvg = sum(PCIreuseDist) / len(PCIreuseDist)

PCIreuseDistAvgA = PCIreuseDistAvg

#PCI Allocation B
NCells = len(cellnames)

PCIalloc = [None] * NCells
allocount =[0]*99
PCIlist = [x for x in range(0, 99)]
for cid,item in enumerate(cellnames):
    for pcid,item2 in enumerate(PCIlist):
        if allocount[pcid] == 0:
            PCIalloc[cid] = item2
            allocount[pcid] = allocount[pcid] + 1
            break
    

for cid,item in enumerate(cellnames):
    dist = []
    if PCIalloc[cid] == None:
        for cid2,item2 in enumerate(cellnames):
            if PCIalloc[cid2] != None:
                maxround = max(allocount)
                minround = min(allocount)
                PCIchk = PCIalloc[cid2]
                if maxround != minround and allocount[PCIchk] == maxround:
                    disttemp = 0
                    dist.append(disttemp)
                else:
                    #disttemp = (((float(lon[cid])-float(lon[cid2]))**(2)) + ((float(lat[cid])-float(lat[cid2]))**(2)))**(0.5)

                    lat1 = float(lat[cid])
                    lat2 = float(lat[cid2])
                    lon1 = float(lon[cid])
                    lon2 = float(lon[cid2])

                    lat1 = lat1*(math.pi)/180
                    lat2 = lat2*(math.pi)/180
                    lon1 = lon1*(math.pi)/180
                    lon2 = lon2*(math.pi)/180

                    deltaLat = lat2-lat1
                    deltaLon = lon2-lon1

                    x = deltaLon*(math.cos((lat1+lat2)/2))
                    y = deltaLat

                    disttemp = 6371*math.sqrt(x*x + y*y) 

                    


                    dist.append(disttemp)
            else:
               
                maxvalue = max(dist)
                maxindex = dist.index(maxvalue)
                PCI = PCIalloc[maxindex]
                PCIalloc[cid] = PCI
                pcid = PCIlist.index(PCI)
                allocount[pcid] = allocount[pcid] + 1
                break
    

PCIallocB = PCIalloc
#Average Reuse Distance Per Code
PCIreuseDist = [0] * len(PCIlist)

for pcid,item in enumerate(PCIlist):
    
    indices = [i for i, xx in enumerate(PCIalloc) if xx == item]
    indices2 = indices 
    dist = []
    for j,cidx1 in enumerate(indices):
        for k,cidx2 in enumerate(indices2):
            if j != k:
                lat1 = float(lat[cidx1])
                lat2 = float(lat[cidx2])
                lon1 = float(lon[cidx1])
                lon2 = float(lon[cidx2])

                lat1 = lat1*(math.pi)/180
                lat2 = lat2*(math.pi)/180
                lon1 = lon1*(math.pi)/180
                lon2 = lon2*(math.pi)/180

                deltaLat = lat2-lat1
                deltaLon = lon2-lon1

                x = deltaLon*(math.cos((lat1+lat2)/2))
                y = deltaLat

                d = 6371*math.sqrt(x*x + y*y)
                dist.append(d)
    distavg = sum(dist) / len(dist)
    PCIreuseDist[pcid] = distavg

PCIreuseDistAvg = sum(PCIreuseDist) / len(PCIreuseDist)

PCIreuseDistAvgB = PCIreuseDistAvg
#Random PCI Allocation
totpci = len(PCIlist)
totcells = len(PCIalloc)
extra = totcells % totpci
reps = math.floor(totcells/totpci)
PCIallocRand = []
for fill in range(0, reps):
    PCIallocRand = PCIallocRand + PCIlist
PCIallocRand = PCIallocRand + PCIlist[0:extra]


#Average Reuse Distance Per Code for Random Scheme
PCIreuseDistrand = [0] * len(PCIlist)

for pcid,item in enumerate(PCIlist):
    
    indices = [i for i, xx in enumerate(PCIallocRand) if xx == item]
    indices2 = indices 
    dist = []
    for j,cidx1 in enumerate(indices):
        for k,cidx2 in enumerate(indices2):
            if j != k:
                lat1 = float(lat[cidx1])
                lat2 = float(lat[cidx2])
                lon1 = float(lon[cidx1])
                lon2 = float(lon[cidx2])

                lat1 = lat1*(math.pi)/180
                lat2 = lat2*(math.pi)/180
                lon1 = lon1*(math.pi)/180
                lon2 = lon2*(math.pi)/180

                deltaLat = lat2-lat1
                deltaLon = lon2-lon1

                x = deltaLon*(math.cos((lat1+lat2)/2))
                y = deltaLat

                d = 6371*math.sqrt(x*x + y*y)
                dist.append(d)
    distavg = sum(dist) / len(dist)
    PCIreuseDistrand[pcid] = distavg

PCIreuseDistAvgRand = sum(PCIreuseDistrand) / len(PCIreuseDistrand)

file = open('results.csv', 'w', newline='')
writer = csv.writer(file,delimiter = ';')

writer.writerow(['Cell_ID', 'PCI_A','PCI_B','PCI_Rand'])

NCells = len(cellnames)
for w in range(NCells):
    writer.writerow([cellnames[w],PCIallocA[w],PCIallocB[w],PCIallocRand[w]])

file.close()

print ("Average Reuse Distance per code for scheme A is",round(PCIreuseDistAvgA, 3), "km.")
print ("Average Reuse Distance per code for scheme B is",round(PCIreuseDistAvgB, 3), "km.")
print ("Average Reuse Distance per code for scheme Rand is",round(PCIreuseDistAvgRand, 3), "km.")