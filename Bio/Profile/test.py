import Profile

a = Profile.Profile("sample_profile.sgr","sgr")
b = Profile.Profile("sample_profile.wig", "wig")
print "nazwy i rozdzielczosci wczytanych profili sample_profile*:"
print a.name, a.description, a.resolution
print b.name, b.description, b.resolution
print "zapisuje sample_profile.sgr na proba.sgr i .wig, sample_profile.wig na proba1.sgr, .wig"
a.writeProfile("proba.sgr","sgr")
a.writeProfile("proba.wig","wig")
b.writeProfile("proba1.sgr","sgr")
b.writeProfile("proba1.wig","wig")
print "wczytuje nieistniejacy plik"
c = Profile.Profile("ala ma kota", "wig")
print "podaje zly format"
c = Profile.Profile("sample_profile.sgr","ala ma kota")
