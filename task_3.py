
class PointsForPlace:
    def get_points_for_place(self, place):
        self.points = 0
        if place > 100:
            print('Баллы начисляются только первым 100 участникам')
        elif place < 1:
            print('Спортсмен не может занять нулевое или отрицательное место')
        else:
            self.points = 101 - place
        return self.points

class PointsForMeters:
    def get_points_for_meters(self, meters):
        self.points = 0
        if meters < 0:
            print('Количество метров не может быть отрицательным')
        else:
            self.points = meters * 0.5
        return self.points

class TotalPoints(PointsForPlace, PointsForMeters):
    def get_total_points(self, meters, place):
        return self.get_points_for_place(place) + self.get_points_for_meters(meters)
        
my_points = 0

points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))
my_points += points_for_place.get_points_for_place(10)
print(my_points)


points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))
my_points += points_for_meters.get_points_for_meters(10)
print(my_points)

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))
my_points += total_points.get_total_points(100, 10)