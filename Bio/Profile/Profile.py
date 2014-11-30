import ProfileIO

class Profile:

	def __init__(self, filename, format="sgr", **kvargs):
		ProfileIO.readProfile( self, filename, format, kvargs)

	def getResolution( self ):
		return self.resolution

	"""
	def setResolution( self, new_resolution ):
		self.resolution = new_resolution
		# of c jeszcze trzeba przerobic profil
	"""

	def getChromosomes( self ):
		chromosomes = self.values.keys()
		chromosomes.sort()
		return chromosomes


	def setChromosomeNames( self, chromosomes ):
		new_values = {}
		new_coordinates = {}
		old_chromosomes = self.getChromosomes()
		for chromosome_nr in xrange( len( chromosomes ) ):
			for new_dictionary, old_dictionary in [ (new_values, self.values), (new_coordinates, self.coordinates) ]:
				new_dictionary[ chromosomes[chromosome_nr] ] = old_dictionary[ old_chromosomes[chromosome_nr] ]
		self.values = new_values
		self.coordinates = new_coordinates


	def writeProfile( self, filename, format="sgr"):
		ProfileIO.writeProfile( self, filename, format )

	
	def addMetadata( self, metadata ):
		self.metadata.update( metadata )
		

