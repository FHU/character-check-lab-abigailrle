#Remove pass and complete the code
def check_character(word, index):
   #letter, digit, white space, or unknown
   impt_bit = word[index].lower()
   if impt_bit.islower() == True:
      return 'letter'
   elif impt_bit.isspace() == True:
      return 'white space'
   elif impt_bit.isdigit() == True:
      return 'digit'
   else:
      return 'unknown'

if __name__ == '__main__': 
    print(check_character('happy birthday', 2))
    print(check_character('happy birthday', 5))
    print(check_character('happy birthday 2 you', 15))
    print(check_character('happy birthday!', 14))