# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.colors import rgb2hex

map = Basemap()

map.drawcoastlines()

plt.show()
plt.savefig('test.png')
