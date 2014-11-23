class Profile:

	def __init__(self, filename, format="sgr"):
		self.readProfile( filename, format)

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

	def readProfile( self, filename, format):
		if not checkIfFileExist( filename ):
			return None
		if format=="sgr":
			#return
			self.readSgr( filename )
		elif format=="wig":
			#return
			self.readWig( filename )
		else:
			print "unsupported format"



	def readSgr( self, filename ):
		sgr_file = file2List( filename )
		
	

	def readWig( self, filename ):
		wig_file = file2List( filename )
		metadata = self.readWigMetadata( wig_file )
		self.name = metadata['name']
		self.description = metadata['description']
		self.resolution = self.readWigResolution( wig_file )
		self.values = self.readWigValues( wig_file )
		self.coordinates = self.readWigCoordinates( wig_file )

		
	def readWigMetadata( self, wig_file ):
		metadata = wig_file[0]
		metadata_dictionary = {"name":"", "description":""}
		if len(metadata) > 1:
			for field in metadata[1:]:
				field = field.strip().split("=")
				metadata_dictionary[ field[0] ] = field[1]
		return metadata_dictionary	
	
	def readWigResolution( self, wig_file ):
		return int( wig_file[1][-1].strip().split('=')[1] )


	def readWigValues( self, wig_file ):
		return self.readWigValuesOrCoordinates( wig_file, "values")

	def readWigCoordinates( self, wig_file ):
		return self.readWigValuesOrCoordinates( wig_file, "coordinates")

	def readWigValuesOrCoordinates( self, wig_file, values_or_coordinates ):
		if values_or_coordinates == "values":
			nr_of_field = 1
			changeOfType = float
		elif values_or_coordinates == "coordinates":
			nr_of_field = 0
			changeOfType = int
		values = {}
		for line in wig_file:
			if line[0].startswith("track"):
				pass
			elif line[1].startswith('chrom='):
				chromosome = line[1].split('=')[1]
			else:
				if chromosome not in values:
					values[chromosome] = []
				values[chromosome].append( changeOfType(line[ nr_of_field ] ))
		return values

			

	def writeProfile( self, filename, format ):
		writer = open(filename, 'w')
		if format=="sgr":
			self.writeSgr( writer )
		if format=="wig":
			self.writeWig( writer )
		writer.close()

	def writeSgr( self, writer ):
		for chromosome in self.getChromosomes():
			print chromosome
			print type(self.values)
			for index in xrange( len( self.values[ chromosome ] )):
				value = self.values[ chromosome ][index]
				coordinate = self.coordinates[ chromosome ][index]
				line = chromosome + '\t' + str(coordinate) + "\t" + str(value) + "\n"
				writer.write( line )

	def writeWig( self, writer ):
		header = self.createHeader()
		for chromosome in self.getChromosomes():
			chromosome_description = "variableStep\t" + chromosome + "\tstep=" + str(self.resolution) + "\n"
			writer.write( header )
			writer.write( chromosome_description )
			values_to_write = [ str(coordinate)+"\t"+str(value)+"\n" for (coordinate, value) in zip(self.coordinates[ chromosome ], self.values[ chromosome ]) ]
			writer.writelines( values_to_write )


	def createHeader( self ):
		return "track name=" + self.name + " description=" + self.description + "\n"
				
		
		

def file2List( filename ):
	my_file = open(filename).readlines()
	for line_nr in xrange( len( my_file )):
		my_file[ line_nr ] = my_file[ line_nr ].strip().split()
	return my_file
	
def checkIfFileExist( filename ):
	try:
		open(filename)
	except IOError:
		print "file " + filename + " doesn\'t exist or can\'t be opened for reading"
		return False
	return True

