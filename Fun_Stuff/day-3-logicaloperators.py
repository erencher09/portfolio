print('''
                     <>______________________
       .-"""-.       ||-._`-._ :| |: _.-'_.-|
      /= ___  \      ||   `-._`:| |:`_.-'   |
     |- /~~~\  |     ||-------`-' '-'-------|
     |=( '.' ) |     ||------_.-. .-._------|
     \__\_=_/__/     ||  _.-'_.:| |:._`-._  |
      {_______}      ||-'_.-'  :| |:  `-._`-|
    /` *       `'--._||~~~~~~~~~~~~~~~~~~~~~~
   /= .     [] .     { >
  /  /|ooo     |`'--'|| 
 (   )\_______/      ||
  \``\/       \      ||
   `-| ==    \_|     ||
     /         |     ||
    |=   >\  __/     ||
    \   \ |- --|     ||
     \ __| \___/     ||
jgs  _{__} _{__}     ||
    (    )(    )     ||
^^~  `"""  `"""  ~^^^~^^~~~^^^~^^^~^^^~^^~^ ''')
print("Welcome to Space")
print("Your mission is to find the spaceship")


choice1 = input('You\'re on the moon at a crossroad, where do you want to go? Type "Left" or "Right"').lower()


if choice1 == "left":
  #continue
  choice2 = input('You\'ve come to a chasm, do you jump, or stay put? "Stay Put" or "Jump"').lower()
  if choice2 == "jump":
    #continue
    choice3 = input('You make it to the other side, but must fight a bear, do you "stab", "shoot", or "burn" the bear?').lower()
    if choice3 == "stab":
    #win game
      print("You stab the bear in the heart and it dies")
    #fail
    elif choice3 == "shoot":
      print("The bear dodges the bullet and mauls you to death, game over")
    #fail
    elif choice3 == "burn":
      print("You can't burn things in space, the bear kills you, game over")
    else:
      print("That was gibberish, game over")
  else:
    #game over
    print("An alien steals your brain and you die, game over")

    
#fail
else:
  input("You explode in a geyser and die, game over")

