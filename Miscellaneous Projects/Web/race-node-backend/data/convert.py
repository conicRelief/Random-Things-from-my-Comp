import os
import re
import geopy
import numpy as np
from geopy.distance import distance as geopy_distance

print "\n \n ______Pre-processing initiated______ \n \n "


finalText = "{ \n \t \"tracks\": \n  \t ["
finalTextTail = "]}"

tracks = []

for subdir,dirs,files in os.walk('./race_tracks'):
  for x in dirs:
    track_name = x
    track_coordinates = ""
    for subdir2,dirs2,files2 in os.walk('./race_tracks/' + x):
      for f in files2:
        o = re.match(r'(.*).xml', f, re.M|re.I)
        if o:
          kml = open("./race_tracks" + "/" +x + "/" + f,'r')
          content = kml.readlines()
          kml.close()
          coordinates = ""
          boolean = False
          blocky = []
          for line in content:
            if boolean:
              if "</coordinates>" in line:
                boolean = False
              else:
                coordinates += line
                blocky.append(line)
            else:
              if "<coordinates>" in line:
                boolean = True
                tcount = 0
                cpair = []
                last = ""
          for z in coordinates.replace('\t',"").replace('\n',"").replace("0 ","").replace("\r","").split(","):
            if 0<len(z):
              if tcount%2 == 0:
                last = z
              else:
                cpair.append([float(last),float(z)])
                last = 0
              tcount = tcount + 1
          jsonarray = "\"coordinates\":["
          
          distance = 0
	  last_point = (cpair[0][0], cpair[0][1])
#	  lastPoint = geopy.Point( str(cpair[0][0]) + " " + str(cpair[0][1]))
	  for c in cpair:
#	    this_point = geopy.Point(str(c[0]) + " " + str(c[1]))
	    this_point = (c[0],c[1])
	    d = geopy_distance(this_point,last_point)
	    distance = distance + d.kilometers	
#	    distance = distance + geopy.distance.distance(last_point,this_point).kilometers
	    last_point = this_point
	  
	  print "Distance:  ", str(distance)
	  

          for c in cpair:
            jsonarray = jsonarray + str(c) + ','
          jsonarray = jsonarray + str(cpair[0])
          track_coordinates = jsonarray + "]"
          tracks.append("{\"name\": \n \"" + track_name + "\", \n" + track_coordinates + "}\n")

for t in tracks:
  finalText += t + ","
li = finalText.rsplit("m", 1)
finalText = "".join(li)
temp = finalText[:-1] + finalTextTail
temp = temp.replace("nae","name")
target = open("race_tracks.json" , 'w')
target.write(temp)
target.close()

print "\n \n =====Pre-processing Complete===== \n \n "

