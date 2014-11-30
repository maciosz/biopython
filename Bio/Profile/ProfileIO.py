def readProfile( self, filename, format, args):
	if not checkIfFileExist( filename ):
		return None
	if format=="sgr":
		readSgr( self, filename )
	elif format=="wig":
		readWig( self, filename, args )
	else:
		print "unsupported format"
	if 'addMetadata' in args.keys():
		self.metadata.update( args['addMetadata'] )





def readSgr( self, filename ):
	sgr_file = file2List( filename )
	self.values, self.coordinates, self.metadata = {}, {}, {}
	for line in sgr_file:
		chromosome, coordinate, value = line
		if chromosome not in self.values.keys():
			self.values[ chromosome ] = []
			self.coordinates[ chromosome ] = []
		self.values[ chromosome ].append( float(value) )
		self.coordinates[ chromosome ].append( int(coordinate) )
	self.resolution = readSgrResolution( self )

def readSgrResolution( profile ):
	return profile.coordinates.values()[0][1] - profile.coordinates.values()[0][0]				
		
	

def readWig( self, filename, args ):
	wig_file = file2List( filename )
	if "readMetadata" in args.keys() and args['readMetadata'] == False:
		self.metadata = {}
	else:
		self.metadata = readWigMetadata( wig_file )
	self.resolution = readWigResolution( wig_file )
	self.values = readWigValues( wig_file )
	self.coordinates = readWigCoordinates( wig_file )

		
def readWigMetadata( wig_file ):
	metadata = wig_file[0]
	metadata_dictionary = {}
	#metadata_dictionary = {"name":"", "description":""}
	if len(metadata) > 1:
		#for field in metadata[1:]:
		#	field = field.strip().split("=")
		#	metadata_dictionary[ field[0] ] = field[1]
		metadata_dictionary = wigMetadata2Dictionary( metadata )
	return metadata_dictionary

def wigMetadata2Dictionary( metadata ):
	if metadata[0] == "track":
		metadata = metadata[1:]
	else:
		print "wig file should start with 'track', something's wrong"
	metadata = " ".join( metadata )
	metadata = metadata.split('" ')
	metadata_dictionary = {}
	for field in metadata:
		key, value = field.split('="')
		metadata_dictionary[ key ] = value
	return metadata_dictionary
	
	
def readWigResolution( wig_file ):
	return int( wig_file[1][-1].strip().split('=')[1] )


def readWigValues( wig_file ):
	return readWigValuesOrCoordinates( wig_file, "values")

def readWigCoordinates( wig_file ):
	return readWigValuesOrCoordinates( wig_file, "coordinates")

def readWigValuesOrCoordinates( wig_file, values_or_coordinates ):
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
		writeSgr( self, writer )
	if format=="wig":
		writeWig( self, writer )
	writer.close()

def writeSgr( self, writer ):
	for chromosome in self.getChromosomes():
		for index in xrange( len( self.values[ chromosome ] )):
			value = self.values[ chromosome ][index]
			coordinate = self.coordinates[ chromosome ][index]
			line = chromosome + '\t' + str(coordinate) + "\t" + str(value) + "\n"
			writer.write( line )

def writeWig( self, writer ):
	header = createHeader(self)
	for chromosome in self.getChromosomes():
		chromosome_description = "variableStep\t" + chromosome + "\tstep=" + str(self.resolution) + "\n"
		writer.write( header )
		writer.write( chromosome_description )
		values_to_write = [ str(coordinate)+"\t"+str(value)+"\n" for (coordinate, value) in zip(self.coordinates[ chromosome ], self.values[ chromosome ]) ]
		writer.writelines( values_to_write )


def createHeader( self ):
	header = "track"
	for key in self.metadata:
		header += " " + key + '="' + self.metadata[ key ].strip('"') + '"'
	header += "\n"
	return header
				
		
		

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

