import parser

a = parser.Profile("sample_profile.wig", "wig")
print a.name, a.description, a.resolution
#print a.values
a.writeProfile("proba.sgr","sgr")
a.writeProfile("proba.wig","wig")
