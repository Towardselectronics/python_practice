def draw_hangman(life):
      
    if (life == 9):
        print ("_________")
        print ("|")
        print ("|")
        print ("|")
        print ("|")
        print ("|")
        print ("|________")
        
    elif (life == 8):
        print ("_________")
        print ("|      |")
        print ("|")
        print ("|")
        print ("|")
        print ("|")
        print ("|________")
    elif (life == 7):
        print ("_________")
        print ("|      |")
        print ("|      O")
        print ("|")
        print ("|")
        print ("|")
        print ("|________")
    elif (life == 6):
        print ("_________")
        print ("|      |")
        print ("|      O")
        print ("|      |")
        print ("|")
        print ("|")
        print ("|________")
    elif (life == 5):
        print ("_________")
        print ("|      |")
        print ("|      O")
        print ("|      |")
        print ("|      |")
        print ("|")
        print ("|________")
    elif (life == 4):
        print ("_________")
        print ("|      |")
        print ("|      O")
        print ("|     \|")
        print ("|      |")
        print ("|")
        print ("|________")
    elif (life == 3):
        print ("_________")
        print ("|      |")
        print ("|      O")
        print ("|     \|/")
        print ("|      |")
        print ("|")
        print ("|________")        
    elif (life == 2):
        print ("_________")
        print ("|      |")
        print ("|      O")
        print ("|     \|/")
        print ("|      |")
        print ("|     / ")
        print ("|________")
    elif (life == 1):
        print ("_________")
        print ("|      |")
        print ("|      O")
        print ("|     \|/")
        print ("|      |")
        print ("|     / \ ")
        print ("|________")
    elif (life == 0):
        print("💀💀Hanged💀💀")
        print ("_________")
        print ("|      |")
        print ("|      O")
        print ("|     \|/")
        print ("|      |")
        print ("|     / \ ")
        print ("|________")
        print('\n')
    
def random_word(fname):
    from random import choice
    lines = open(fname).read().splitlines()
    return choice(lines)

def get_user_character():
    character = input('🤔🤔 guess a character of the word : ')
    return character 

def check(char,dupli):
    res = False
    for i in word:
        if char == i:
            res = True
            mul_char = check_character_occurrence(word,char)
            
            if len(mul_char) == 1:
                dupli = replace_str_index(dupli,word.index(char),char)
            
            else:
                for k in range(len(mul_char)):
                    dupli = replace_str_index(dupli,mul_char[k],char)
    
    return res,dupli

def replace_str_index(text,index=0,replacement=''):
    return '%s%s%s'%(text[:index],replacement,text[index+1:])

def check_character_occurrence(strs,char):
    import re 
    occ = [x.start() for x in re.finditer(char, strs)]
    return occ

word = random_word('C:\\Users\\TowardsElectronics\\Desktop\\python\\python_practice\\word_list_hangman.txt')
life = 10
turn = 1
dupli = '-'*len(word)
print("Hangman Game")
while turn > 0:
    guess = get_user_character()
    if turn != 1:
        res,dup = check(guess,dup)
        draw_hangman(life)
        print('{}\tTurns : {}\tLife : {} ❤'.format(dup,turn,life))
    else:
        res,dup = check(guess,dupli)
        print('{}\tTurns : {}\tLife : {} ❤'.format(dup,turn,life))
    turn += 1
    if res != True:
        life -= 1
        if life == 0:
            draw_hangman(life=0)
            print('\n\n😢😔 life expired you lost 😢😔')
            print('\nThe word is : {}'.format(word))
            break
    if dup == word:
        print('\n\n♥♥♥ Congrats you guessed the word correctly | won the game ♥♥♥')
        break
