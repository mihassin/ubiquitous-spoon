import matplotlib.image as mpimg
import numpy as np
import os


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Class preprocessor                                               '
' author: mihassin                                                 '
' attributes:                                                      '
'  - __data,   array containing image pixel arrays                 '
'  - __amount, amount of images                                    '
'  - __path, directory path to images                              '
' function:                                                        '
'  - count_data, returns the amount of images                      '
'  - get_path, returns the directory path as string                '
'  - get_data, returns an array containing images as pixel arrays  '
'  - get_data_as_1d, returns data as 2d matrix                     '
'  - __read_data, private function to gather data                  '
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


class preprocessor:

	def __init__(self):
		self.__data = []
		self.__amount = 0
		self.__path = ""


	def count_data(self):
		return self.__amount


	def get_path(self):
		return self.__path


	def get_data(self, path):
		if self.count_data() == 0 or self.__path != path:
			self.__path = path
			self.__data = self.__read_data()
			self.__amount = len(self.__data)
		return self.__data  


	def get_data_as_2d(self, path):
		tmp = self.get_data(path)
		return [tmp[i].reshape(np.product(tmp[i].shape)) for i in range(len(tmp))]

	#data/pics
	def __read_data(self):
		data = []
		for root, dirs, files in os.walk(self.__path):
			for file in files:
				data.append(mpimg.imread(os.path.join(root,file)))
		return data