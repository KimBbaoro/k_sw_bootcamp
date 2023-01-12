example ={'korean' : 'Kimchi', 'japan' : "sushi", 'china' : "duck"}


country = 'japan'
print(f'{country}의 맛있는 음식은 {example[country]}')

#old style
print('%s의 맛있는 음식은 %s _ v'%(country, example[country]))
print("{0}의 맛있는 음식은 {1} oldest v".format(country, example[country]))


import webbrowser
import json
from urllib.request import urlopen

# print("Let's find an old website.")
# site = input("Type a website URL : ")
# era = input("Type a")