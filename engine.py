import threading
import random

c = 0
m1 = 4
m2 = 98421
m3 = 100
m4 = 0


def out():
  threading.Timer(5.0, out).start()
  global c, m1, m2, m3, m4
  c += 1
  m1 = random.randint(0,m1)
  m2 = random.randint(1000,m2)
  m3 = random.randint(0,m3)

  if m4 >= 100: 
   m4 = 99
  else:
    m4 = random.randint(m4,m4+5)

 
  

  print (
    "Epoch: "+format(c)+
    ", Loss: "+format(m1)+"."+format(m2)+
    ", Train: "+ format(random.uniform(15.5, 80.5)) +"%" + 
    ", Valid: "+format(m3)+"."+format(m2)+
     ",Test: "+format(m4)+"."+format(m2))


out()
