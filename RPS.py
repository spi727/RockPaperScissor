# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
count=0
sample=["R","P","S","S","R"]
pattern=[]
myhist=sample
play_order=[{
              "RR": 0,
              "RP": 0,
              "RS": 0,
              "PR": 0,
              "PP": 0,
              "PS": 0,
              "SR": 0,
              "SP": 0,
              "SS": 0,
          }]
def player(prev_play, opponent_history=[]):
    global sample,count,pattern,play_order,myhist
    guess="R"
    if count==0:prev_play=""
    if prev_play != "":
        opponent_history.append(prev_play)
        
    if count<5:
        guess=sample[count]
        count+=1
        pattern.append(prev_play)
        return guess
    #quincy
    if pattern[-4:]==["R","P","P","S"]:
        count+=1
        choices = ["R", "R", "P", "P", "S"]
        counter=["P","P","S","S","R"]
        guess=counter[count % len(choices)]
    
    #abbey
    if pattern[-4:]==["P","P","P","P"]:
        count+=1
        last_two = "".join(myhist[-2:])
        if len(last_two) == 2:
            play_order[0][last_two] += 1
        a=myhist[-1]
        potential_plays = [
         a + "R",
         a + "P",
         a + "S",
        ]

        sub_order = {
           k: play_order[0][k]
          for k in potential_plays if k in play_order[0]
        }

        prediction = max(sub_order, key=sub_order.get)[-1:]
        ideal_response = {"P": "R", "R": "S", "S": "P"}
        myhist.append(ideal_response[prediction])
        guess=ideal_response[prediction]
    
    #kris
    if pattern[-4:]==["P","P","S","R"]:
        count+=1
        c=myhist[-1]
        ideal_response = {"P": "R", "R": "S", "S": "P"}
        myhist.append(ideal_response[c])
        guess=ideal_response[c]
    
    #mrugesh
    if pattern[-4:]==["R","R","R","R"]:
        count+=1
        last_ten = myhist[-10:]
        most= max(set(last_ten), key=last_ten.count)

        if most == '':
            most = "S"

        ideal_response = {"P": "R", "R": "S", "S": "P"}
        myhist.append(ideal_response[most])
        guess=ideal_response[most]


    if count==1000:
        count=0
        sample=["R","P","S","S","R"]
        myhist=sample
        pattern=[]
        play_order=[{
              "RR": 0,
              "RP": 0,
              "RS": 0,
              "PR": 0,
              "PP": 0,
              "PS": 0,
              "SR": 0,
              "SP": 0,
              "SS": 0,
          }]
    
    
        
    return guess