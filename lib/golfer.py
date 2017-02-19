
class Golfer(object):

	def __init__(self, rank, name, points):
		self.rank = rank
		self.name = name
		self.points = points

	def get_rank(self):
		return self.rank

	def get_name(self):
		return self.name

	def get_points(self):
		return self.points

	def string(self):
		print "NAME: %s RANK: %s POINTS: %s\n" % (self.name, self.rank, self.points)