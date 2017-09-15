# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, create_engine, Integer,Float,DECIMAL, Sequence, MetaData, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/city_DistMSG',echo=True)
metadata = MetaData(engine)
Base.metadata.drop_all(engine)

user_table = Table('cityDist', metadata,
        Column('id', Integer, primary_key=True),
        Column('start_city', String(20)),
        Column('end_city', String(20)),
        Column('start_lat', DECIMAL(15)),
        Column('start_lon', DECIMAL(15)),
        Column('end_lat', DECIMAL(15)),
        Column('end_lon', DECIMAL(15)),
        Column('dist_city', DECIMAL(24))
        )
metadata.create_all()
