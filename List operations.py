if __name__=='__main__':
    list=[]
    N=int(input("Enter a number"))
    for i in range(N):
      command=input("Enter a command").split()
      
      if command[0]=="insert":
          i, e=map(int, command[1:])
          list.insert(i,e)
      elif command[0]=="pop":
          list.pop()
      elif command[0]=="remove":
          e=map(int, command[1:])
          list.remove(e)
      elif command[0]=="append":
          e=map(int, command[1:])
          list.append(e)
      elif command[0]=="sort":
          list.sort
      elif command[0]=="reverse":
          list.reverse()
      elif command[0]=="print":
          print(list)
          
    