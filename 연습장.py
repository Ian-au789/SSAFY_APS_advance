size = 10
car_in = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
parking_lot = [0] * size

idx = 0
for car in car_in:
    parking_lot[idx] = car
    temp = car_in.pop(0)
    print(temp)
