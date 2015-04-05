import os

# GameState, entity for load and save games
class GameState:
	_tag = "GameState: "
	# turn & players
	actual_turn = -1
	actual_player = -1
	players = []

	#map
	map = None

	# unit blueprints and instances
	unit_skeletons = {}
	units = []

	# building blueprints and instances
	building_skeletons = {}
	buildings = []

	# items (not here yet)
	items = []

	# turn & player updates
	@classmethod
	def update_actual_turn(self, turn):
		self.actual_turn = turn
		print str(self._tag + "updated turn: " + turn)
	@classmethod
	def actual_turn(self):
		return self.actual_turn

	@classmethod
	def update_actual_player(self, actual_player):
		self.actual_player = actual_player
		print str(self._tag + "updated actual player: " + str(actual_player))
	@classmethod
	def actual_player(self):
		return self.actual_player

	@classmethod
	def update_player_list(self, players):
		self.players = players
		print str(self._tag + "updated player list: " + str(players))
	@classmethod
	def player_list(self):
		return self.players

	# map update
	@classmethod
	def set_actual_map(self, map):
		self.map = map
		print str(self._tag + "updated map: " + map.name)
	@classmethod
	def actual_map(self):
		return self.map

	# units update
	@classmethod
	def set_unit_skeletons(self, unit_skeletons):
		self.unit_skeletons = unit_skeletons
		print str(self._tag + "updated unit blueprints: " + str(unit_skeletons))
	@classmethod
	def unit_skeletons(self):
		return self.unit_skeletons

	@classmethod
	def update_unit_list(self, units):
		self.units = units
		print str(self._tag + "updated unit list: " + str(units))
	@classmethod
	def unit_list(self):
		return self.units

	# buildings unpdate
	@classmethod
	def set_bld_skeletons(self, bld_skeletons):
		self.building_skeletons = bld_skeletons
		print str(self._tag + "updated building blueprints: " + str(bld_skeletons))
	@classmethod
	def bld_skeletons(self):
		return self.building_skeletons

	@classmethod
	def update_bld_list(self, buildings):
		self.buildings = buildings
		print str(self._tag + "updated building list: " + str(buildings))
	@classmethod
	def bld_list(self):
		return self.buildings
