store_car = {'cars' :  [{'mersedes' : 10000000},
                        {'ferrary' : 46524372},
                        {'bmw' : 965243720000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000}], 
             'info' : {'director' : 'Виниамин'}}

# print(store_car['info'] ['director'])
# prise_mers = store_car['cars'][2]['bmw']
# print(prise_mers)
def get_mark_car():
    cars = store_car['cars']
    for car in cars:
        for i in car:
            return i
        
print(get_mark_car())