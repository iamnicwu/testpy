# -*- coding: utf-8 -*-  
import pandas as pd

#1880 - 2010 的数据统计
years = range(1880, 2011)

pieces = []
columns = names= ['name', 'sex', 'births']

for year in years:
	path = 'names/yob%d.txt' % year
	frame  = pd.read_csv(path, names = columns)
	frame['year'] = year
	pieces.append(frame)
	
#利用pd.concat 连接数据，将所有数据整合到单个DataFrame中
#注意利用ignore_index = True 可以忽略read_csv 所返回的原始行号
names = pd.concat(pieces, ignore_index = True)