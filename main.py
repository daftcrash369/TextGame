print("Hello,\n Welcome to Whatever Land!")
print("==============================")

choice1 = [ 'HAPPY', 'ANGRY', 'CONFLICTED', 'GRACEFUL', 'CONTENT' ]

choices = ""
for choice in choice1:
    choices += choice + ", "
choices = choices[:-2] # remove the last ', '
ans = str(input("'How are you today?' \n" + choices + "? "))
ans1 = ans.upper()


if ans1 == choice1[0]:
    print('Yay, I\'m so very happy that you\'re happy!! That makes me happy!')
elif ans1 == choice1[1]:
    print('Yay, wait....no... that\'s not good.')
elif ans1 == choice1[2]:
    print('Excuse me...  Who are you?? Where am I? What\'s even going on?')
elif ans1 == choice1[3]:
    print('You are among the very best. Not many people reach a state such as you\'re in.')

print(ans)