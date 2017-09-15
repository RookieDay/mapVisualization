# -*- coding:utf-8 -*-
from math import radians, cos, sin, asin, sqrt

#计算两点间距离-m
def geodistance(lng1,lat1,lng2,lat2):
    lng1, lat1, lng2, lat2 = map(radians, [lng1, lat1, lng2, lat2])
    dlon=lng2-lng1
    dlat=lat2-lat1
    a=sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    dis=2*asin(sqrt(a))*6371*1000
    return dis

Lat_A=32.060255; Lng_A=118.796877 # 南京
Lat_B=39.904211; Lng_B=116.407395 # 北京
distance=geodistance(Lng_A,Lat_A,Lng_B,Lat_B)
print('(Lat_A, Lng_A)=({0:10.3f},{1:10.3f})'.format(Lat_A,Lng_A))
print('(Lat_B, Lng_B)=({0:10.3f},{1:10.3f})'.format(Lat_B,Lng_B))
print('Distance={0:10.3f} km'.format(distance))

places = {'Beijing':(39.85915479295669, 116.455078125),
          'Tianjin':(39.061849134291535, 117.235107421875),
          'Jinan':(36.59788913307022, 117.147216796875),
          'Shijiazhuang':(38.004819966413194, 114.521484375)
        }

for key in places:
    print(key )