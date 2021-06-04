def bubble(a):
      for c in range(1,len(a)):
            b=0
            for i in range(len(a)-c):
                  a1 = a[b]
                  a2 = a[b+1]
                  if a1>a2:
                        a[b] = a2
                        a[b+1] = a1
                  b=b+1
      print(a)
list1= [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]
bubble(list1)