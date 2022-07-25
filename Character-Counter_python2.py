# -*- coding: cp1254 -*-

print "Character Counter Tool"

a = raw_input("Input : ")
def uniq(input):
  output = []
  for x in input:
    if x not in output:
      output.append(x)
  return output
c = uniq(a)
for b in c:
    print b , "=====>" , a.count(b) , "found."


