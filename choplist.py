# have scraped prod catigory titles and number prods in each catigory. 
# to to get it in a csv file for bioregonal 

from wilkoOutput import output
from DecoratingAndDIY import * 
from GuardenOutdoorLiving import * 
from Halloween import * 
from HealthandBeauty import * 
from Home_Living import * 
from HouseholdCleaning import * 
from KitchenDining import * 
from offers import * 
from pets import * 
from stationaryCraft import * 
from storage import * 
from studentliving import * 
from Toysandbikes import * 

count1 = 0
count2 = 0

list_of_lists = [
        'ToysAndBikes',
        'studentliving',
        'Storage', 
        'StationaryCraft',
        'pets', 
        'offers', 
        'KitchenDining',
        'HouseholdCleaning',
        'HomeLiving',
        'HealthandBeauty',
        'Halloween',
        'GuardenOutdoorLving',
        'DecoratingAndDIY',
]


dict_of_lists = {
        'ToysAndBikes':ToysAndBikes,
        'studentliving': studentliving,
        'Storage': Storage, 
        'StationaryCraft': StationaryCraft,
        'pets': pets, 
        'offers': offers, 
        'KitchenDining': KitchenDining,
        'HouseholdCleaning': HouseholdCleaning,
        'HomeLiving': HomeLiving,
        'HealthandBeauty':HealthandBeauty,
        'Halloween':Halloween,
        'GuardenOutdoorLving': GuardenOutdoorLving,
        'DecoratingAndDIY': DecoratingAndDIY,
        }
# tern this into a dictionary of titles and values with is the number. 

Big_dict = {}

for i in output:
    try: 
        items = i.split('|')
        numb = items[1].split(':')
        quant = int(numb[1])
        #print(quant)
        #print(items[0],quant)
        Big_dict[items[0].strip('Title: ')]= quant

    except: 
        pass

#print('>>>>>>>>>>>>>>>>>>>> Big_dict <<<<<<<<<<<<<<<<<<<<<<<<')
'''
for i in Big_dict:
    print(i)
'''
#print('>>>>>>>>>>>>>>>>>>>> Big_dict END  <<<<<<<<<<<<<<<<<<<<<<<<')

print(Big_dict['Chopping Boards'])


Grand_Total_products = 0

for i in list_of_lists:
    Catigory_Total = 0

    for a in dict_of_lists[i]:
        try: 
            key = str(a)
            #print(key,Big_dict[str(key)])
            Catigory_Total += Big_dict[str(key)]
        except: 
            pass 
            #print('Dict error:', a )

    print('\n')
    print('Catigory Heading:', i, 'estimate: Products in Catigory:', Catigory_Total)
    print('AWOOGA: this is an estimate, possible dupplication')

    Grand_Total_products += Catigory_Total

print('\n' * 2)
print('Wilko estimate Total number of products Sold:' ,Grand_Total_products)
