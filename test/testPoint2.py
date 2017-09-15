# -*- coding:utf-8 -*-
import time
start = time.clock()
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
map = Basemap(llcrnrlon=80.33,
              llcrnrlat=3.01,
              urcrnrlon=138.16,
              urcrnrlat=56.123,
             resolution='h', projection='lcc', lat_0 = 42.5,lon_0=120,ax=ax1)

shp_info = map.readshapefile("CHN_adm_shp\CHN_adm1",'states',drawbounds=True) # CHN_adm1的数据是中国各省区域

for info, shp in zip(map.states_info, map.states):
    poly = Polygon(shp,facecolor='w',edgecolor='w', lw=1)
    ax1.add_patch(poly)

map.drawcoastlines()    # 绘制海岸线
map.drawcountries()     # 绘制国家
map.drawcounties()      # 绘制县
# map.bluemarble()

gpsLoc = [[39.85915479295669, 116.455078125],
          [39.061849134291535, 117.235107421875],
          [36.59788913307022, 117.147216796875],
          [38.004819966413194, 114.521484375]]

for index, value in enumerate(gpsLoc):
    lon= value[1]
    lat = value[0]
    x, y = map(lon,lat)
    print value
    map.scatter(x,y,s=100,marker='D',facecolors='r',edgecolors='r')


# start_lat = 39.85915479295669
# start_lon = 116.455078125
# end_lat = 39.061849134291535
# end_lon = 117.235107421875
#
# if abs(end_lat - start_lat) < 180 and abs(end_lon - start_lon) < 180:
#     map.drawgreatcircle(start_lon, start_lat, end_lon, end_lat, linewidth=1)
#




end=time.clock()
print(end-start)
plt.show()