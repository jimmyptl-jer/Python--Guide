olympians = [("John Aalberg", 31, "Cross Country Skiing"),
             ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]

outfile = open("reduced_olympics.csv", "w")
# output the header row
outfile.write('Name,Age,Sport')
outfile.write('\n')
# output each of the rows:
for olympian in olympians:
    row_string = '{},{},{}'.format(olympian[0], olympian[1], olympian[2])
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()


with open("reduced_olympics.csv","r") as jabber:
  for jab in jabber:
    print(jab)

fileconnection = open("reduced_olympics.txt", 'r')
lines  = fileconnection.readlines()
header = lines[0]
field_names = header.strip().split(',')
print(field_names)
for row in lines[1:]:
     vals = row.strip().split(',')
     if vals[5] != "NA":
         print("{}: {}; {}".format(
                 vals[0],
                 vals[4],
                 vals[5]))

