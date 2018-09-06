import csv

cr = csv.reader(open("data/source/counts.csv","rU"))
o = ["assault","homicide","kidnapping","robbery","sexassault","otherviol","drugposs","drugtraff","otherdrug","arson","burglary","fraud","larceny","mvtheft","otherprop","dwi","weapons","public_oth"]

f = {"1" : "Alabama","2" : "Alaska","4" : "Arizona","5" : "Arkansas","6" : "California","8" : "Colorado","9" : "Connecticut","10" : "Delaware","11" : "District of Columbia","12" : "Florida","13" : "Geogia","15" : "Hawaii","16" : "Idaho","17" : "Illinois","18" : "Indiana","19" : "Iowa","20" : "Kansas","21" : "Kentucky","22" : "Louisiana","23" : "Maine","24" : "Maryland","25" : "Massachusetts","26" : "Michigan","27" : "Minnesota","28" : "Mississippi","29" : "Missouri","30" : "Montana","31" : "Nebraska","32" : "Nevada","33" : "New Hampshire","34" : "New Jersey","35" : "New Mexico","36" : "New York","37" : "North Carolina","38" : "North Dakota","39" : "Ohio","40" : "Oklahoma","41" : "Oregon","42" : "Pennsylvania","44" : "Rhode Island","45" : "South Carolina","46" : "South Dakota","47" : "Tennessee","48" : "Texas","49" : "Utah","50" : "Vermont","51" : "Virginia","53" : "Washington","54" : "West Virginia","55" : "Wisconsin","56":"Wyoming"}

h = cr.next()

d = {}
for row in cr:
	state = row[1]
	off = row[2]
	if state not in d:
		d[state] = []
	d[state].append(off)

for s in d:
	l1 = set(d[s])
	l2 = set(o)

	print f[s]
	print l2 - l1

