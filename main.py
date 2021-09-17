f = open("555SAMPLE.GED", 'r')

person = {}
people = {}

id = ''
zerolevel = ''

for line in f:
  #print(line)

  tokens = line.split()

  #print(tokens)

  if tokens[0] == '0':
    if len(tokens) >= 3:
      if tokens[2] == 'INDI':
        #print("I found an INDI!  They are called " + tokens[1])

        #print(person)

        zerolevel = 'INDI'

        # store the prior person, if this isn't the first one
        if 'name' in person: # if not (id == ''): ... if len(id) > 0
          people[id] = person

        id = tokens[1]
        person = {}
      else:
        zerolevel = ''
  elif tokens[0] == '1':
    if(len(tokens) >= 2):
      if tokens[1] == 'NAME':
        #print("I found a name!")
        #print(line)

        if zerolevel == 'INDI':
          name = line

          spacelocation = name.index(' ')
          secondspacelocation = name.index(' ', spacelocation)

          person['name'] = name[secondspacelocation:]

# get the last person
people[id] = person

print(people)

print("digraph G {")
for key in people.keys():
  print("\t" + key.replace('@', '').strip() + " [label= \"" +  people[key]['name'].strip().replace('/', '') + "\"]")
print("}")