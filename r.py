import threading

f=open('/content/o/o/data.txt')
lines=f.readlines()
c = -1


def out():
  threading.Timer(5.0, out).start()
  global lines, c
  c+=1
  print (lines[c])




out()
