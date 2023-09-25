
def computegrade():
    if score >=0.9:
        print('Grade A')
    elif score >=0.8 and score<0.9:
        print('Grade B')
    elif score >=0.7 and score<0.8:
        print('Grade C')
    elif score >=0.6 and score<0.7:
        print('Grade D')
    else:
        print('Grade F')

score = input('Go ahead and enter in your grades for me: ')
try:
    score = float(score)
    computegrade()
except:
    print('Sir, This is a number zone only! I will have to ask you to leave.')
