import os

for i in range(700):
    d = str(i) + ' days ago'
    with open('bot.txt','a') as file:
        file.write(d+'\n')
    os.system('git add bot.txt')
    os.system('git commit --date="'+d+'" -m "first-hack"')
        
os.system('git push -u origin master')       