#FILE USED FOR TESTING AND PLAYING AROUND. NOTHING SERIOUS
def testing(x) :
  if x>0 :
    return print("{x} is bigger than 0")
  else:
    return print('you suck')


#testing(5)

def findNeedle(junk) :

  return print(f"Found the needle in position {junk.index('needle')}")

example = ['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]
#findNeedle(example)

def stray(arr) :
  y = 0
  x = arr[y]
  while arr.count(x) >= 2:
    y= y+1
    x=arr[y]
  return print(x)

stray([13, 13, 13, 5, 13])