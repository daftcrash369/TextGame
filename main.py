print("Hello,\n Welcome to Whatever Land!")
print("=================================")

ans1 = str(input("'How are you today?' \n HAPPY, ANGRY, CONFLICTED, GRACEFUL? "))

choice1 = [ 'HAPPY', 'ANGRY','CONFLICTED', 'GRACEFUL' ]

if ans1 == 'HAPPY':
    print('Yay, I\'m so very happy that you\'re happy!! That makes me happy!')
elif ans1 == 'ANGRY':
    print('Yay, wait....no... that\'s not good.')
elif ans1 == 'CONFLICTED':
    print('Excuse me...  Who are you?? Where am I? What\'s even going on?')
elif ans1 == 'GRACEFUL':
    print('You are among the very best. Not many people reach a state such as you\'re in.')

print(ans1)