inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

for akey in inventory.keys():     # the order in which we get the keys is not defined
    print("Got key", akey, "which maps to value", inventory[akey])

ks = list(inventory.keys())
print(ks)
print()
print()

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

for k in inventory:
    print("Got key", k)

print()
print()


inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

print(list(inventory.values()))
print(list(inventory.items()))

for k in inventory:
    print("Got",k,"that maps to",inventory[k])


print()
print()


inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print('apples' in inventory)
print('cherries' in inventory)

if 'bananas' in inventory:
    print(inventory['bananas'])
else:
    print("We have no bananas")

print()
print()


inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

print(inventory.get("apples"))
print(inventory.get("cherries"))

print(inventory.get("cherries",0))

print()
print()


mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
answer = mydict.get("cat")//mydict.get("dog")
print(answer)


print()
print()


total = 0
mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
for akey in mydict:
   if len(akey) > 3:
      total = total + mydict[akey]
print(total)

print()
print()


f = open('scarlet.txt', 'r')
txt = f.read()
# now txt is one long string containing all the characters
t_count = 0 #initialize the accumulator variable
for c in txt:
    if c == 't':
        t_count = t_count + 1   #increment the counter
print("t: " + str(t_count) + " occurrences")
f.close()
print()
print()

f = open('scarlet.txt', 'r')
txt = f.read()
# now txt is one long string containing all the characters
x = {} # start with an empty dictionary
x['t'] = 0  # initialize the t counter
x['s'] = 0  # initialize the s counter
for c in txt:
    if c == 't':
        x['t'] = x['t'] + 1  # increment the t counter
    elif c == 's':
        x['s'] = x['s'] + 1  # increment the s counter

print("t: " + str(x['t']) + " occurrences")
print("s: " + str(x['s']) + " occurrences")
f.close()
print()
print()

f = open('scarlet.txt', 'r')
txt = f.read()
# now txt is one long string containing all the characters
x = {} # start with an empty dictionary
x['t'] = 0  # intiialize the t counter
x['s'] = 0  # initialize the s counter
for c in txt:
    if c == 't':
        x[c] = x[c] + 1   # increment the t counter
    elif c == 's':
        x[c] = x[c] + 1   # increment the s counter

print("t: " + str(x['t']) + " occurrences")
print("s: " + str(x['s']) + " occurrences")
f.close()
print()
print()

f = open('scarlet.txt', 'r')
txt = f.read()
# now txt is one long string containing all the characters
x = {} # start with an empty dictionary
for c in txt:
    if c not in x:
        # we have not seen this character before, so initialize a counter for it
        x[c] = 0

    #whether we've seen it before or not, increment its counter
    x[c] = x[c] + 1

print("t: " + str(x['t']) + " occurrences")
print("s: " + str(x['s']) + " occurrences")
f.close()
print()
print()

f = open('scarlet.txt', 'r')
txt = f.read()
# now txt is one long string containing all the characters
letter_counts = {} # start with an empty dictionary
for c in txt:
    if c not in letter_counts:
        # we have not seen this character before, so initialize a counter for it
        letter_counts[c] = 0

    #whether we've seen it before or not, increment its counter
    letter_counts[c] = letter_counts[c] + 1

for c in letter_counts.keys():
    print(c + ": " + str(letter_counts[c]) + " occurrences")
f.close()



sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."

sent = sentence.split()
print(sent)

word_counts = {}

for i in sent:
  if i not in word_counts:
    word_counts[i] = 0

  word_counts[i] = word_counts[i] + 1

print(word_counts)



stri = "what can I do"

char_d = {}

for i in stri:
  if i not in char_d:
    char_d[i] = 0

  char_d[i] = char_d[i] + 1

print(char_d)
print()
print()

f = open('scarlet.txt', 'r')
txt = f.read()
# now txt is one long string containing all the characters
x = {} # start with an empty dictionary
for c in txt:
    if c not in x:
        # we have not seen this character before, so initialize a counter for it
        x[c] = 0

    #whether we've seen it before or not, increment its counter
    x[c] = x[c] + 1

letter_values = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f':4, 'g': 2, 'h':4, 'i':1, 'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1, 's':1, 't':1, 'u':1, 'v':4, 'w':4, 'x':8, 'y':4, 'z':10}

tot = 0
for y in x:
    if y in letter_values:
        tot = tot + letter_values[y] * x[y]

print(tot)
print()
print()


travel = {"North America": 2, "Europe": 8, "South America": 3, "Asia": 4, "Africa":1, "Antarctica": 0, "Australia": 1}
total = 0

trav = list(travel.values())
print(trav)

for i in trav:
  total = total + i

print(total)
print()
print()

schedule = {"UARTS 150": 3, "SPANISH 103": 4, "ENGLISH 125": 4, "SI 110": 4, "ENS 356": 2, "WOMENSTD 240": 4, "SI 106": 4, "BIO 118": 3, "SPANISH 231": 4, "PSYCH 111": 4, "LING 111": 3, "SPANISH 232": 4, "STATS 250": 4, "SI 206": 4, "COGSCI 200": 4, "AMCULT 202": 4, "ANTHRO 101": 4}


lst_schedule = list(schedule.values())
print(lst_schedule)

total_credits = 0

for credit in lst_schedule:
  total_credits += credit

print(total_credits)
print()
print()



placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."

d = {}

for char in placement:
  print(char)

  if char not in d:
    d[char] = 0

  d[char] += 1

print(d)  

d_keys = list(d.keys())
print(d_keys)

min_d_key = d_keys[0]
print(min_d_key)

for i in d_keys:
  if d[i] < d[min_d_key]:
    min_d_key = i

print(min_d_key)
print()
print()



product = "iphone and android phones"

lett_d = {}

for char_1 in product:
  print(char_1)
  if char_1 not in lett_d:
    lett_d[char_1] = 1
  else:
    lett_d[char_1] = lett_d[char_1] + 1

print(lett_d)

keys = list(lett_d.keys())
print(keys)

max_value = keys[0]

for i in keys:
  if lett_d[i] > lett_d[max_value]:
    max_value = i

print(max_value)
print()
print()


print(""" When to use a dictionary
Now that you have experience using lists and dictionaries, you will have to decide which one is best to use in each situation. The following guidelines will help you recognize when a dictionary will be beneficial:

When a piece of data consists of a set of properties of a single item, a dictionary is often better. You could try to keep track mentally that the zip code property is at index 2 in a list, but your code will be easier to read and you will make fewer mistakes if you can look up mydiction[‘zipcode’] than if you look up mylst[2].

When you have a collection of data pairs, and you will often have to look up one of the pairs based on its first value, it is better to use a dictionary than a list of (key, value) tuples. With a dictionary, you can find the value for any (key, value) tuple by looking up the key. With a list of tuples you would need to iterate through the list, examining each pair to see if it had the key that you want.

On the other hand, if you will have a collection of data pairs where multiple pairs share the same first data element, then you can’t use a dictionary, because a dictionary requires all the keys to be distinct from each other.
""")


print()
print()


medal_count = {'United States': 70, 'Great Britain':38, 'China':45, 'Russia':30, 'Germany':17, 'Italy':22, 'France': 22, 'Japan':26, 'Australia':22, 'South Korea':14, 'Hungary':12, 'Netherlands':10, 'Spain':5, 'New Zealand':8, 'Canada':13, 'Kazakhstan':8, 'Colombia':4, 'Switzerland':5, 'Belgium':4, 'Thailand':4, 'Croatia':3, 'Iran':3, 'Jamaica':3, 'South Africa':7, 'Sweden':6, 'Denmark':7, 'North Korea':6, 'Kenya':4, 'Brazil':7, 'Belarus':4, 'Cuba':5, 'Poland':4, 'Romania':4, 'Slovenia':3, 'Argentina':2, 'Bahrain':2, 'Slovakia':2, 'Vietnam':2, 'Czech Republic':6, 'Uzbekistan':5}


key = medal_count.keys()
print(key)
belarus = 0
for i in key:
  print(i)

  if i == "Belarus":
    belarus = medal_count.get(i)


print(belarus)
  

total_golds = {"Italy": 114, "Germany": 782, "Pakistan": 10, "Sweden": 627, "USA": 2681, "Zimbabwe": 8, "Greece": 111, "Mongolia": 24, "Brazil": 108, "Croatia": 34, "Algeria": 15, "Switzerland": 323, "Yugoslavia": 87, "China": 526, "Egypt": 26, "Norway": 477, "Spain": 133, "Australia": 480, "Slovakia": 29, "Canada": 22, "New Zealand": 100, "Denmark": 180, "Chile": 13, "Argentina": 70, "Thailand": 24, "Cuba": 209, "Uganda": 7,  "England": 806, "Denmark": 180, "Ukraine": 122, "Bahamas": 12}

key = total_golds.keys()

print(key)

chile_golds = 0

for i in key:
  if i == "Chile":
    print(total_golds[i])
    chile_golds = total_golds[i]


print(chile_golds)
print()
print()

str1 = "I wish I wish with all my heart to fly with dragons in a land apart"

str1_1 = str1.split()

freq_words = {}

for i in str1_1:
  if i not in freq_words:
    freq_words[i] = 1

  else:
    freq_words[i] = freq_words[i] + 1


print(freq_words)



L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1
for x in d.keys():
    print("{} appears {} times".format(x, d[x]))


L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1
y = sorted(d.keys())
for k in y:
    print("{} appears {} times".format(k, d[k]))



L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1

y = sorted(d.keys(), key=lambda k: d[k], reverse=True)
for k in y:
    print("{} appears {} times".format(k, d[k]))



L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1

def g(k):
    return d[k]

y =(sorted(d.keys(), key=g, reverse=True))

# now loop through the keys
for k in y:
    print("{} appears {} times".format(k, d[k]))



L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1

# now loop through the sorted keys
for k in sorted(d, key=lambda k: d[k], reverse=True):
      print("{} appears {} times".format(k, d[k]))



def test(t1,b = True , dict1 ={2:3, 4:5, 6:8}):
    if b == True:
        for i,v in dict1.items():
            if t1 in dict1.keys():
               p = dict1.get(t1)
        return p       
    elif b == False:
        return False    


 
p = test(2)
print(p)

p_1 = test(4, False)
print(p_1)

p_2 = test(5 , dict1 = {5:4, 2:1})
print(p_2)