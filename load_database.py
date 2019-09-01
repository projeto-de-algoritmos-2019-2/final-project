from cars.models import Car

cars = []

with open('carros.txt') as file:
    for line in file:
        lst = line.split(',') #['(1926', " 'Chrysler'", " 'Imperial')"]
        # year, model, manufacturer

        lst = [elem.replace('(', '') for elem in lst]
        lst = [elem.replace(')', '') for elem in lst]
        lst = [elem.replace(';', '') for elem in lst]
        lst = [elem.replace(',', '') for elem in lst]
        lst = [elem.replace("'", '') for elem in lst]
        lst = [elem for elem in lst if elem != '\n']
        lst = [elem.strip() for elem in lst]

        year, manufacturer, model = lst

        car = Car(year=year, model=model, manufacturer=manufacturer)
        cars.append(car)
    

for i, car in enumerate(cars):
    
    print('Progress {:.2f}'.format(i/len(cars)))
    car.save()