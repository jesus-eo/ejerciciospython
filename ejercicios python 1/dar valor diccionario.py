

def relation_to_luke(name):
  dict = {
    'Darth Vader' : 'father',
    'Leia' : 'sister',
    'Han' : 'brother in law',
    'R2D2' : 'droid'
  }
  return 'Luke, I am your ' + dict[name] + '.'

print(relation_to_luke('Han'))
