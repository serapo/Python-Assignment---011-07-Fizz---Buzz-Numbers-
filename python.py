
for i in range(1,101):
  if i%3==0 and i%5 !=0:
    print("Fiz")
  elif i%5==0 and i%3 !=0:
    print("Buzz")
  elif i%5==0 and i%3==0:
    print("FizBuzz")
  else:
    print(i)  
