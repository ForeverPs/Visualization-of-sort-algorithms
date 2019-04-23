import os
import imageio
import numpy as np
import matplotlib.pyplot as plt


class sort(object):
	def __init__(self):
		self.img = []
		self.fig = plt.figure()
		plt.ion()
		self.count = 0
		self.path = 'sp/'
		if not os.path.lexists(self.path):
			os.mkdir(self.path)

	def merge_sort(self, s, start, end):
		if end - start < 2:
			return
		m = (end - start) // 2
		self.merge_sort(s, start, start + m)
		self.merge_sort(s, end - m, end)
		self.merge(start, m, end, s)

	def merge(self, start, m, end, s):
		i, j = start, m
		while i < m and j < end:
			if j == end or (i < m and s[i] < s[j]):
				i += 1
			else:
				s.insert(i, s[j])
				j += 1
				s.pop(j)
				self.draw(s, fun = 'MERGE SORT')


	def quick_sort(self, s, a, b):
		if a >= b:
			return
		base = s[b]
		left, right = a, b - 1
		while left <= right:
			while left <= right and s[left] < base:
				left += 1
			while left <= right and s[right] > base:
				right -= 1
			if left <= right:
				s[left], s[right] = s[right], s[left]
				left, right = left + 1, right - 1
		s[left], s[b] = s[b], s[left]
		if left != b:
			self.draw(s, fun = 'QUICK SORT')
		self.quick_sort(s, a, left - 1)
		self.quick_sort(s, left + 1, b)

	def select_sort(self, s):
		self.draw(s, fun = 'SELECTION SORT')
		for i in range(len(s)):
			if self.search(s, i):
				self.draw(s, fun = 'SELECTION SORT')

	def search(self, s, i):
		index, value = i, s[i]
		for j in range(i, len(s)):
			if s[j] < value:
				index, value = j, s[j]
		s[index], s[i] = s[i], s[index]
		return index != i

	def heap_adjust(self, s, m, length):
		j = 2 * m + 1
		# since index begins from 0, childs of father is 2*x+1 and 2*x+2
		if j == length - 1:
			if s[m] < s[j]:
				s[m], s[j] = s[j], s[m]
		while j <  length - 1:
			if s[j] < s[j + 1]:
				j += 1
			if s[m] > s[j]:
				break
			s[m], s[j], m, j= s[j], s[m], j, 2 * j + 1

	def heap_sort(self, s):
		i = len(s) // 2 - 1
		while i >= 0:
			self.heap_adjust(s, i, len(s))
			i -= 1
		i = len(s)
		while i > 0:
			s[0], s[i - 1], i = s[i - 1], s[0], i - 1
			self.draw(s, fun = 'HEAP SORT')
			self.heap_adjust(s, 0, i)

	def insert_sort(self, s):
		i = j = len(s)
		while i > 0:
			if self.insert_next(s, j - i):
				self.draw(s, fun = 'INSERT SORT')
			i -= 1

	def insert_next(self, s, k):
		index, value = k, s[k]
		for i in range(k, len(s)):
			if s[i] < value:
				index, value = i, s[i]
		s[k], s[index] = s[index], s[k]
		return index != k

	def shell_sort(self, s):
		count, t = 1, int(np.log2(len(s) + 1))
		while count <= t:
			delta = 2 ** (t - count + 1) - 1
			for i in range(0, len(s) - delta):
				if self.insert_shell(s, i, i + delta):
					self.draw(s, fun = 'SHELL SORT')
			count += 1

	def insert_shell(self, s, start, end):
		index, value = start, s[start]
		for i in range(start, end + 1):
			if s[i] < value:
				index, value = i, s[i]
		s[start], s[index] = s[index], s[start]
		return index != start

	def bubble_sort(self, s):
		n = len(s)
		for j in range(n - 1):
			for i in range(n - j - 1):
				if s[i] > s[i + 1]:
					s[i], s[i + 1] = s[i + 1], s[i]
					self.draw(s, fun = 'BUBBLE SORT')

	def draw(self, s, fun):
		if len(s):
			self.count += 1
			plt.clf()
			plt.bar(range(len(s)), s, width = 0.3, color = 'purple')
			plt.title(fun)
			plt.savefig('sp/' + str(self.count))
			plt.pause(0.01)

	def get_gif(self):
		name = os.listdir(self.path)
		name.sort(key=lambda x:int(x[:-4]))
		for ele in name:
			path = self.path + ele
			self.img.append(imageio.imread(path))
		imageio.mimsave('sort.gif', self.img, fps = 8)


if __name__ == '__main__':
	s = [100 - k for k in range(100)]
	p = sort()
	p.select_sort(list(s))
	p.heap_sort(list(s))
	p.quick_sort(list(s),0,len(s)-1)
	p.merge_sort(list(s), 0, len(s))
	p.insert_sort(list(s))
	p.shell_sort(list(s))
	#p.bubble_sort(list(s))
	p.get_gif()

