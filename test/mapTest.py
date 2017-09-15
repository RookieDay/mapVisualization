#-*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon

plt.figure(figsize=(16,8))
map = Basemap(llcrnrlon=77,
            llcrnrlat=14,
            urcrnrlon=140,
            urcrnrlat=51,
            projection='lcc',
            lat_1=33,
            lat_2=45,
            lon_0=100)

map.drawcountries(linewidth=1.5)
map.drawcoastlines()
map.readshapefile('CHN_adm_shp/CHN_adm1', 'states', drawbounds=True)
# map.etopo() # 绘制地形图，浮雕样式
ax = plt.gca()
for nshape, seg in enumerate(map.states):
    # print seg
    color = 'r'
    poly = Polygon(seg, facecolor=color)
    ax.add_patch(poly)

map.drawcoastlines()
# map.shadedrelief() # 绘制阴暗的浮雕图


plt.show()