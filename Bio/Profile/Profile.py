import ProfileIO

class Profile:

	def __init__(self, filename, format="sgr"):
		ProfileIO.readProfile( self, filename, format)

	def getResolution( self ):
		return self.resolution

	def setResolution( self, new_resolution ):
		self.resolution = new_resolution
		# of c jeszcze trzeba przerobic profil

	def getName( self ):
		return self.name

	def setName( self, new_name ):
		self.name = new_name

	def getChromosomes( self ):
		chromosomes = self.values.keys()
		chromosomes.sort()
		return chromosomes


	def changeChromosomeNames( self, chromosomes ):
		new_values = {}
		old_chromosomes = self.getChromosomes()
		for chromosome_nr in xrange( len( chromosomes ) ):
			new_values[ chromosomes[chromosome_nr] ] = self.values[ old_chromosomes[chromosome_nr] ]
		self.values = new_values


	def writeProfile( self, filename, format="sgr"):
		ProfileIO.writeProfile( self, filename, format )

