# -*- coding:utf-8 -*-
import time
import random
from math import *
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import matplotlib.colors as clr
from matplotlib.patches import Polygon
from sqlalchemy import Column, String, Sequence, DECIMAL, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
start = time.clock()

# 数据库相关 - 创建对象的基类:
Base = declarative_base()

# 定义cityDistMsg对象:
class cityDistMsg(Base):
    # 表的名字:
    __tablename__ = 'cityDist'
    # 表的结构:
    id = Column(Integer, Sequence('id'),primary_key=True)
    start_city = Column(String(20))
    end_city = Column(String(20))
    start_lat = Column(DECIMAL(20))
    start_lon = Column(DECIMAL(20))
    end_lat = Column(DECIMAL(20))
    end_lon = Column(DECIMAL(20))
    dist_city = Column(DECIMAL(20))

#数据插入表中
def insertToTable(data_list):
    # 初始化数据库连接 数据库名：city_DistMSG
    engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/city_DistMSG')
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)
    # 创建session对象:
    session = DBSession()
    # 创建新PunishMsg对象:
    pun_msg = cityDistMsg(start_city = data_list[0].strip(),
                    end_city = data_list[1].strip(),
                    start_lat = data_list[2],
                    start_lon = data_list[3],
                    end_lat = data_list[4],
                    end_lon = data_list[5],
                    dist_city = data_list[6])
    # 添加到session:
    session.add(pun_msg)
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()

#计算经纬度 两点间距离
def calcDistance(Lat_A, Lng_A, Lat_B, Lng_B):
    ra = 6378.140  # 赤道半径 (km)
    rb = 6356.755  # 极半径 (km)
    flatten = (ra - rb) / ra  # 地球扁率
    rad_lat_A = radians(Lat_A)
    rad_lng_A = radians(Lng_A)
    rad_lat_B = radians(Lat_B)
    rad_lng_B = radians(Lng_B)
    pA = atan(rb / ra * tan(rad_lat_A))
    pB = atan(rb / ra * tan(rad_lat_B))
    xx = acos(sin(pA) * sin(pB) + cos(pA) * cos(pB) * cos(rad_lng_A - rad_lng_B))
    c1 = (sin(xx) - xx) * (sin(pA) + sin(pB)) ** 2 / cos(xx / 2) ** 2
    c2 = (sin(xx) + xx) * (sin(pA) - sin(pB)) ** 2 / sin(xx / 2) ** 2
    dr = flatten / 8 * (c1 - c2)
    distance = ra * (xx + dr)
    return distance

def visualMap():
    fig = plt.figure()
    ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
    map = Basemap(llcrnrlon=80.33,
                  llcrnrlat=3.01,
                  urcrnrlon=138.16,
                  urcrnrlat=56.123,
                 resolution='h', projection='lcc', lat_0 = 42.5,lon_0=120,ax=ax1)

    #保存获取颜色的十六进制值
    colorArrs = []
    for name, hex in clr.cnames.iteritems():
        colorArrs.append(hex)


    #绘制各省区域
    shp_info = map.readshapefile("CHN_adm_shp\CHN_adm1",'states',drawbounds=True) # CHN_adm1的数据是中国各省区域
    for nshape, seg in enumerate(map.states):
        color = colorArrs[random.randint(1,colorArrs.__len__() - 1)]
        # print(color)
        poly = Polygon(seg,facecolor=color,edgecolor=color, lw=1)
        ax1.add_patch(poly)

    #绘制台湾
    shp_infoTW = map.readshapefile("TWN_adm_shp\TWN_adm0",'taiwan',drawbounds=True) # CHN_adm1的数据是taiw台湾 for nshape, seg in enumerate(map.taiwan):
    for nshape, seg in enumerate(map.taiwan):
        polyTW = Polygon(seg,facecolor='coral',edgecolor='w', lw=1)
        ax1.add_patch(polyTW)

    map.drawcoastlines()    # 绘制海岸线
    map.drawcountries()     # 绘制国家

    # 处理经纬度
    places = {'Beijing':(39.85915479295669, 116.455078125),
              'Tianjin':(39.061849134291535, 117.235107421875),
              'Jinan':(36.59788913307022, 117.147216796875),
              'Shijiazhuang':(38.004819966413194, 114.521484375)
            }

    cities = [
               ('Beijing', 'Tianjin'),
               ('Beijing', 'Jinan'),
               ('Tianjin', 'Jinan'),
               ('Tianjin', 'Shijiazhuang'),
               ('Jinan', 'Shijiazhuang'),
               ('Shijiazhuang', 'Beijing')
               ]

    srcCity = ''
    for source, target in cities:
        data_list = []
        lat1, lon1 = places[source]
        lat2, lon2 = places[target]
        if abs(lon1 - lon2) < 180 and abs(lat1 - lat2) < 180:
            map.drawgreatcircle(lon1, lat1, lon2, lat2, linewidth=2, color='r')
            x1, y1 = map(lon1, lat1)
        if srcCity != source:
            srcCity = source
            plt.text(x1, y1, source,fontsize=9,fontweight='bold',
                        ha='left',va='center',color='k',
                    bbox=dict(facecolor='b', alpha=0.2))
        #计算距离
        distance = calcDistance(lat1,lon1,lat2,lon2)
        data_list.append(source)
        data_list.append(target)
        data_list.append(lat1)
        data_list.append(lon1)
        data_list.append(lat2)
        data_list.append(lon2)
        data_list.append(distance)
        #插入数据库中
        insertToTable(data_list)

if __name__ == '__main__':
    visualMap()
    plt.title('CHINA')
    end=time.clock()
    print(end-start)
    plt.show()