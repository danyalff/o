import threading

def out():
  threading.Timer(5.0, out).start()
  print ("Epoch: 01, Loss: 4.2716, Train: 17.29%, Valid: 25.17% Test: 22.93%")

out()
