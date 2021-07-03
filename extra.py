import os
shiba_inu = os.path.join(os.getcwd(), 'doge-coin.mp3')
os.system("{0} {1}".format('mpg123', shiba_inu))