a=[[100,100,100],[100,100,100],[100,100,100]]
lst1=[1,3,5,7,9]
lst2=[0,2,4,6,8]
pos=int
pos2=int
for s in range (0,3) :
    for m in range (0,1) :
            
            
          print (a[s][m],a[s][m+1],a[s][m+2])


while True:
    
   
    b=int(input("player 1 please enter number : "))
    while b%2==0 :
        print("player 1 please enter odd number")
        b=int(input("player 1 please enter number : "))
    while b<0 or b>9:
        print ("enter number in the limit")
        b=int(input("player 1 please enter number : "))
    try   :
     if b == 1  :
             lst1.remove(1)
    
     elif b == 3  :
             lst1.remove(3)
  
     elif b == 5  :
               lst1.remove(5)
    
     elif b == 7  :
             lst1.remove(7)
    
     elif b == 9  :
             lst1.remove(9)
     else :
         print ("please enter a number didn't use before")
         b=int(input("player 1 please enter number : "))
    except :
         print ("please enter a number didn't use before")
         b=int(input("player 1 please enter number : "))

        
        
    
    
    pos=int(input("please enter position :"))
    while pos==pos2:
        print("this position is busy")
        pos=int(input("please enter another position"))
    
        break
    
    
    try :
     if pos==1:
            a[0][0]=b
     if pos==2:
        a[0][1]=b
     if pos==3:
        a[0][2]=b
     if pos==4:
        a[1][0]=b
     if pos==5:
        a[1][1]=b    
     if pos==6:
        a[1][2]=b  
     if pos==7:
        a[2][0]=b
     if pos==8:
        a[2][1]=b
     if pos==9:
        a[2][2]=b
    except :
        print("this position is busy")
        pos=int(input("please enter another position"))
    
    for s in range (0,3) :
        for m in range (0,1) :
              print (a[s][m],a[s][m+1],a[s][m+2])
   
                     
    if (a[0][0]+a[0][1]+a[0][2]==15) \
       or (a[1][0]+a[1][1]+a[1][2]==15) \
       or (a[2][0]+a[2][1]+a[2][2]==15)  \
       or (a[0][0]+a[1][0]+a[2][0]==15)  \
       or (a[0][1]+a[1][1]+a[2][1]==15)  \
       or (a[0][2]+a[1][2]+a[2][2]==15)  \
       or (a[0][0]+a[1][1]+a[2][2]==15)  \
       or (a[0][2]+a[1][1]+a[2][0]==15)  :
            print ("player one win")
            break
    
            
        
         
    player2=int(input("player2 please enter number : "))
    while player2%2!=0  :
        print("player2 please enter even number")
        player2=int(input("player2 please enter number : "))

    while player2<0 or player2>9:
        print (" player2 please enter number in the limit")
        player2=int(input("player 2 please enter number : "))
    try :

         if player2 == 0  :
             lst2.remove(0)
    

         elif player2 == 2  :   
             lst2.remove(2)
    
         elif player2 == 4  :
             lst2.remove(4)
    
         elif player2 == 6  :
             lst2.remove(6)
        
         elif player2 == 8  :
             lst2.remove(8)
         else :
            print ("player2 please enter a number didn't use before")
            player2=int(input("player 2 please enter number : "))
    except :
             print ("player2 please enter a number didn't use before")
             player2=int(input("player 2 please enter number : "))

    pos2=int(input("player2 please enter position : "))
    while pos==pos2:
        print("this position is busy")
        pos2=int(input("please enter another position"))
    
    try :
     if pos2==1 :
            a[0][0]=player2
     if pos2==2:
        a[0][1]=player2
     if pos2==3:
        a[0][2]=player2
     if pos2==4:
        a[1][0]=player2
     if pos2==5:
        a[1][1]=player2   
     if pos2==6:
        a[1][2]=player2  
     if pos2==7:
        a[2][0]=player2
     if pos2==8:
        a[2][1]=player2
     if pos2==9:
        a[2][2]=player2
    except :
        print("this position is busy")
        pos2=int(input("please enter another position"))
    
    
    for s in range (0,3) :
        for m in range (0,1) :
              print (a[s][m],a[s][m+1],a[s][m+2])
    
                
        if (a[0][0]+a[0][1]+a[0][2]==15) \
       or (a[1][0]+a[1][1]+a[1][2]==15) \
       or (a[2][0]+a[2][1]+a[2][2]==15)  \
       or (a[0][0]+a[1][0]+a[2][0]==15) \
       or (a[0][1]+a[1][1]+a[2][1]==15) \
       or (a[0][2]+a[1][2]+a[2][2]==15) \
       or (a[0][0]+a[1][1]+a[2][2]==15) \
       or (a[0][2]+a[1][1]+a[2][0]==15) :
            print ("player two win")
            break

