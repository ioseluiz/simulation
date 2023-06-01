

def calc_speed(distance, start_time, end_time):
    return (distance/(end_time - start_time))

def calc_delta_x(point_1, point_2):
    coor_x_1 = point_1[0]
    coor_x_2 = point_2[0]
    return (coor_x_2 - coor_x_1)

def calc_delta_y(point_1, point_2):
    coor_y_1 = point_1[1]
    coor_y_2 = point_2[1]
    return (coor_y_2 - coor_y_1)

def calc_total_distance(points):
    total = 0
    for i in range(1,len(points)):
        previous_point = points[i-1]
        actual_point = points[i]
        total += calc_distance_points(previous_point, actual_point)
    return total

def calc_distance_points(point_1, point_2):
    # Coordinates of point 1
    coor_x_1 = point_1[0]
    coor_y_1 = point_1[1]
    # Coordinates of point 2
    coor_x_2 = point_2[0]
    coor_y_2 = point_2[1]

    distance = ((coor_x_2 - coor_x_1)**2 + (coor_y_2 - coor_y_1)**2)**0.5
    print(distance)
    return distance


if __name__ == '__main__':
    list_points = [(0,0),(2,2),(3,5)]
    print(calc_total_distance(list_points))
    



    