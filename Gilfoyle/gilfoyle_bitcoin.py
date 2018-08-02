import requests
import winsound

#Programado por Guillermo Sánchez García
#winsound.PlaySound("why", winsound.SND_FILENAME)
print("To know if is rentable for you to mine or not we will need you to enter your core (If you have INTEL I7-7700K 4.70 GHZ put q, AMD RYZEN 7 1700X 4.00 GHZ put w)")
r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
rentable = 0;
bucle = 1;
song = 1;
print("Bitcoin price: $" + r.json()['bpi']['USD']['rate'])
core = input("Your core?")
print(core)
if (core == "w"):
    rentable = 124000000000000;
    print(rentable)

if (core == "q"):
    rentable = 32400000000000;
    print(rentable) 

while bucle > 0:
   r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
   price = r.json()['bpi']['USD']['rate_float']
   
   if (price >= rentable):
       print ("rentable")
       print (price - rentable)
       if (song != 1):
           winsound.PlaySound("why", winsound.SND_FILENAME)
           song = 1
   else:
       print ("no rentable")
       if (song != 0):
           winsound.PlaySound("why", winsound.SND_FILENAME)
           song = 0
