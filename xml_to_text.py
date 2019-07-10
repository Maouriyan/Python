import xml.etree.ElementTree as ET
import os
name = ""
count = 0
filelist=os.listdir('/home/nibi/Desktop/Training_Images/vehicle_cargo_labeled/')
for fichier in filelist[:]: # filelist[:] makes a copy of filelist.
    if (fichier.endswith(".xml")):
        name = str(fichier)
        
        o_name = name[:-4]
        tree = ET.parse('/home/nibi/Desktop/Training_Images/vehicle_cargo_labeled/'+name)
        root = tree.getroot()

        cord = []

        for elem in root:
            for subelem in elem:
                for new in subelem:
                    str1 = (new.text)
                    val = int(str1)
                    cord.append(val)

        # print("xmin,ymin",cord[0],cord[1]) 
        # print("xmax,ymin",cord[2],cord[1])
        # print("xmax,ymax",cord[2],cord[3])

        # print("xmin,ymax",cord[0],cord[3])
        xmin =str(cord[0])
        ymin =str(cord[1])
        xmax =str(cord[2])
        ymax =str(cord[3])

        str2 = (xmin+","+ymin+","+xmax+","+ymin+","+xmax+","+ymax+","+xmin+","+ymax+",")
        #print (str2)
        text_file = open("/home/nibi/Desktop/vehicle_cargo_resized_with_text/"+o_name+".txt", "w")
        #print("Written,",o_name)
        count = count +1
        text_file.write(str2)
        text_file.close()
#print(name)     
print(count)  
#print(filelist)
#text_file = open("/home/nibi/Desktop/vehicle_cargo_resized/"+o_name+".txt", "w")

