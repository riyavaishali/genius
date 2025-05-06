import random as r

opt=["rock","paper","scissor"]
score_user=0
score_com=0

while True:
   user_input=input("enter choice rock/paper/scissor ")
   com_input=r.choice(opt)
   print("com_input",com_input)
   if user_input in opt:
       if user_input==com_input:
           print("Tie")
           print(" ")
       elif user_input=='rock' and com_input=='paper':
           print("user wins")
           score_user+=1
           print(" ")
       elif user_input=='rock' and com_input=='scissor':
           print("user wins")
           score_user+=1
           print(" ")
       elif user_input=='paper' and com_input=='rock':
           print("computer wins")
           score_com+=1
           print(" ")
       elif user_input=='scissor' and com_input=='rock':
           print("computer wins")
           score_com+=1
           print(" ")
       elif user_input=='scissor' and com_input=='paper':
           print("user wins")
           score_user+=1
           print(" ")
       else:
           print("computer wins")
           score_com+=1
           print(" ")
       next_opt=input("Do you want to enter another option ?  ")
       print(" ")
       if next_opt=='no':
           print("    Score   ")
           if score_com==score_user:
               print("User score = ",score_user)
               print("Computer score = ",score_com)
               print("Tie")
           elif score_user>score_com:
               print("User wins = ",score_user)
           else:
               print("Computer wins = ",score_com)
           break
   else:
      print("Invalid input")
