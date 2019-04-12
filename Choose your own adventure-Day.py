def main():
    
    #opening statemnet before questions start
    print("The year is 2078, America has fallen and been recreated into four different colonies each with its own set of rules and strict leaders. All of the colonies have constantly been at war for centuries with one colony, The Hollows, ruling over the others. Always stealing their land,this is where we meet you.")


    print("Your name is Day. Day has grown up in the impovershed militarized zone known as the Pit. Day was left orpahned when he was 9 years old, and is now approaching his 19th birthday. The Hollows force all 19 year old street kids into the military and join the Alliance to begin fighting for them. The members tasked with collecting these teens are ruthless and will stop at nothing ot either obtain these kids or kill themif they remain unwilling. Your birthday is in two days, goodluck Day.")


    print("It is time to see if you can survive, or sucum to the Hollows, evade capture and make it out, join the Alliance, or be hunted and killed. The choice is yours.")

    #where the user starts the game
    start= (input("To begin the game type 1 and press enter: "))
    if start is "1":
            print("You wake up shivering in the frosty February air, your stomach is growling and you ran out of water last night.Do you 1 want to start with water or 2 food?")
            q1= (input("Please enter the number of your choice (1 or 2): "))

    if q1 =="1":

        print("You get up and go to steal some water from a group of Alliance soldiers stupid enough to fall asleep on guard.")

        print("While you are there you see a half eaten sandwich in the sleeping guards hand. In the other is a 9mm pistol.")

        print("Do you 1 try and steal the sandwich or 2 the pistol?")

        q2= (input("Please enter the number of your choice (1 or 2): "))
    

    if q2 =="1":

        print("You snake the sandwich from the guards hand. Congrats on getting both food and water on the same day in the pit.")

        print("While walking back you run into your friend Hassan. He is talking to you about how he has not eaten in a week and hasn’t had water in days.")

        print("He is dying for food and water. Do you 1 share with Hassan or 2 keep everything for yourself?")

        q3= (input("Please enter the number of your choice (1 or 2): "))

    if q2 == "1":
        #ending

        print("You reach for the pistol and he wakes up and shoots you.")

        print("GAMEOVER")

    if q3 == "1":

        print("You share half of everything with Hassan and he gives you a spare knife he found.")

        print("He also invites you to come to a little rooftop poker game with him and some of your mutual friends.")

        print("Do you 1 accept or 2 decline and look for a safe place to sleep for the night?")

        q4= (input("Please enter the number of your choice (1 or 2): "))

    if q3 == "1":
        #ending

        print("You decide to keep everything for yourself and turn your back on him. Walking away you run into a rouge gang. They steal your food and water and beat you until you are unable to get up.")

        print("GAMEOVER")

    if q4 == "2":
        print("You decline and start your trek through the war then street. On your way you see a group of Alliance soldiers chasing this poor kid.")
        print("Do you 1 walk the other way or 2 offer them a way to escape?")
        q5= (input("Please enter the number of your choice (1 or 2): "))

    if q4 == "1":
        #ending

        print("You agree to go and end up having a great night. One of the guys managed to steal some alcohol form one of the bars and you spend the night drinking.")

        print("Sadly while stumbling back on your way home you run into  group of guys. They try to steal your stuff and as you try fighting them off you end up getting stabbed several times.")

        print("GAMEOVER")

    if q5 == "2":

        print("You snag her arm and pull her through an old sewage drain, telling her to keep going and don’t stop.")

        print("About 15 minutes later, exhausted and out of breath you too slow down and she turns to thank you.")

        print("She asks if you have a place to sleep for the night. Do you 1 lie and say yes or 2 tell her the truth?")

        q6= (input("Please enter the number of your choice (1 or 2): "))

    if q5 == "1":
        #ending

        print("You lie and say that you have a place. She smiles and says thank you for the help and walks off into the night. If start off in the opposite direction and end up running into the soldiers who have been looking for her.")

        print("Before you get a chance to run the are already on you placing you in handcuffs and taking you away.")

        print("GAMEOVER")

    if q6 == "2":

        print("You tell her the truth and she offers for the two of you to search for a place together. You happily agree.")

        print("You guys have two options 1 the old jail or 2 a dumpster?")

        q7= (input("Please enter the number of your choice (1 or 2): "))


    if q6 == "1":
        #ending

        print("You squat down next to the dumpster, but you two forget that she can’t be out in the open like that because the Alliance is relentlessly looking for her.")

        print("While drifting iff to sleep you are awoken with the butt of a rifle to your face. The Alliance had found you.")

        print("GAMEOVER")

    if q7 == "2":

        print("You slide up the side of by the old fire escape and enter through a broken window. For once you have a safe place to sleep for the night")

        print("In the morning you two part ways and she offers you a bag with something inside.")

        print("Do you 1 accept it or 2 politely decline?")

        q8= (input("Please enter the number of your choice (1 or 2): "))

    if q7 == "1":
        #ending

        print("")

        print("")

        print("GAMEOVER")

    if q8 == "2":

        print("You accept her off and she smiles and says I will see you again soon.")

        print("You open the bag to fid an invitation to join the resistance.")

        print("Do you 1 decide to join or 2 stay on your own, you are better as a lone wolf?")

        q9= (input("Please enter the number of your choice (1 or 2): "))

    if q8 == "1":
        #ending

        print("")

        print("")

        print("GAMEOVER")

    if q9 =="1":

        print("You decide to join and later head to the train tracks where the invitation told you to go.")

        print("There you see a group of what appears to be renegade soldiers not in any real set of uniforms standing around talking.")

        print("Do you 1 approach them or 2 hang back and watch for a while?")

        q10= (input("Please enter the number of your choice (1 or 2): "))

    if q9 == "2":
        #ending

        print("You decline her offer and leave the jail. While walking you see a group of alliance members kicking this poor boy.")

        print(" Deciding to step in and intervene you too get attacked and suffer major wounds leaving you unable to complete your journey.")

        print("GAMEOVER")

    if q10 == "2":

        print("You hang back for a moment and to your dismay Alliance soldiers come out for the woods and train cars killing everyone. ")
        
        print("You begin to back away and the mystery girl from earlier grabs your arm. Handing you a gun she asks if you will avenge her friends with her.")

        print("You accept the gun, but do you 1 help her avenge the fallen men or 2 give the gun back and walk away?")

        q11= (input("Please enter the number of your choice (1 or 2): "))

    if q10 == "1":
        #ending

        print("You approach when suddenly an ambush of Alliance soldiers emerge from the woods and train cars.")

        print("Failing to flee you get got in the crossfire and are fatally wounded.")

        print("GAMEOVER")

    if q11 == "2":

        print("You wish her the very best and go on your way. It is now less than 12 hours before you are 19 do you go back to the jail or do you head out into the woods?")

        q12= (input("Please enter the number of your choice (1 or 2): "))

    if q11 == "1":
        #ending

        print("You take the gun and in a last hurrah hail of bullets you both get shot, but you successfully killed most of the soldiers")

        print("GAMEOVER")
    

    if q12 == "2":

        print("You stumble through the dark woods and find a nice spot to sleep for the night.")

        print("You wake up right before sunrise freezing. Today is your 19th birthday Day, do you 1 make a fire or 2 get up and get moving for the day?")

        q13= (input("Please enter the number of your choice (1 or 2): "))

    if q12 == "1":
        #ending

        print("You walk back to the jail and fall asleep, but to your surprise yo wake up staring down the barrel of a gun.")

        print("It is the Alliance and the leader smiles and says happy birthday Day and welcome to the Alliance.")

        print("GAMEOVER")

    if q13 == "2":

        print("You get up and start moving. If you continue on your current path you will reach a different section of the pit.")

        print("Do you 1 continue forward or 2 turn back?")

        q14= (input("Please enter the number of your choice (1 or 2): "))

    if q13 == "1":
        #ending
        
        print("You start a fire and fall back asleep. You awake to the Alliance, with no other option you surrender and join them.")

        print("GAMEOVER")

    if q14 == "2":

        print("You reach the next section of the Pit. A place you have never ventured, but you are on the right track to reach the border.")

        print("Once you cross it you will be free from the long reach of the Alliance.")

        print("Do you 1 power through or 2 stop and gather supplies?")

        q15= (input("Please enter the number of your choice (1 or 2): "))

    if q14 == "1":
        #ending

        print("You turn back and run smack into an Alliance patrol unit squad. In an attempt to flea you are shot and killed.")

        print("GAMEOVER")

    if q15 == "2":

        print("You choose to stop and gather supplies. As you travel throughout the town you use a spare fire starter to get a large container of water. ")

        print("Then you stumble upon a fruit orchard owned by the Alliance.")

        print("Do you 1 steal some food or 2 move on?")

        q16= (input("Please enter the number of your choice (1 or 2): "))

    if q15 == "1":
        #ending

        print("Choosing to power through you enter a more destroyed area, quickly you discover that there is little to no food in the area and it is completely empty of water.")

        print("Determined to keep moving you eventual pass out from dehydration.")

        print("GAMEOVER")

    if q16 == "1":

        print("You hop over the fence and collect a bag full of apples and other fruits.")

        print("You now have enough supplies where you should be able to complete your journey.")

        print("Do you 1 rest and sleep or 2 push on to where you are going?")

        q17= (input("Please enter the number of your choice (1 or 2): "))

    if q16 == "2":
        #ending
        print("You decide to keep moving and use your knife to rob a trader, he turns and fires hitting you point blank and killing you instantly.")

        print("GAMEOVER")

    if q17 == "1":

        print("Choosing to rest you fall asleep leaning against an old log, sadly you didn’t get quite far enough away from the Alliance’s orchard and are discovered. ")

        print("You now are a member of the Alliance.")

        print("GAMEOVER")

    if q17 == "2":

        print("You push on and make your way out of the Hollows territory. You made it through to Watermark")

        print("CONGRATULATIONS Day you survived and made it out of the Pit.")


#this will be path 2

    if q1 == "2":

        print("")
   
    
    

    
            
    

main()
