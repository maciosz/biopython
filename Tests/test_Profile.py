from Bio import Profile
import os

print "reading sample profiles..."	

try:
	a = Profile.Profile("Profile/sample_profile.sgr","sgr")
	b = Profile.Profile("Profile/sample_profile.wig", "wig")
	print "--- checked! ---"
except:
	print "--- failed :( ---"

print "checking metadata reading and editing..."

b_metadata = {"name" : "sample profile", "description" : "some random sample profile"}
failed=False
if a.metadata != {} or b.metadata != b_metadata:
	failed=True
a.addMetadata({"date" : "10.10.1010"})
if "date" not in a.metadata.keys() or a.metadata["date"] != "10.10.1010":
	failed = True
if failed:
	print "--- failed :( ---"
else:
	print "--- checked! ---"

print "writing to file..."

try:
	a.writeProfile("test.sgr","sgr")
	a.writeProfile("test.wig","wig")
	b.writeProfile("test1.sgr","sgr")
	b.writeProfile("test1.wig","wig")
	print "--- checked! ---"
	print "cleaning up"
	os.remove("test.sgr")
	os.remove("test.wig")
	os.remove("test1.sgr")
	os.remove("test1.wig")
except:
	print "--- failed :( ---"


