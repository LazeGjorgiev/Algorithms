from matplotlib import pyplot as plt
import math
import numpy as np

def generate_random_points(x_max, y_max, number = 10):
    return list(zip(np.random.randint(0,x_max,number),np.random.randint(0,y_max,number)))

def plot(points,show_hull = False,planets=None,title=None,diagonal=None):
    xs,ys = zip(*points)

    plt.scatter(xs,ys,c='r')

    if(show_hull):
        for i in range(1,len(points)+1):
            if i ==len(points): i=0
            plt.plot((points[i-1][0],points[i][0]),(points[i-1][1],points[i][1]),c='red')
    if diagonal!=None:
        plt.plot([diagonal[0][0],diagonal[1][0]],[diagonal[0][1],diagonal[1][1]],c='blue')

    if(planets):
        xs, ys = zip(*planets)
        plt.scatter(xs, ys, c='green')

    if title!=None:
        plt.title(title)
    plt.show()

def plot_planets_and_army(planets,army,diagonal=None):
    xs,ys = zip(*planets)
    plt.scatter(xs,ys,c='green')
    xs, ys = zip(*army)
    plt.scatter(xs, ys, c='red')
    plt.title('Планети и вселенски бродови 2Д')

    plt.show()

def get_angle_between_points(point1, zero_degree_point):
    if point1[0] < zero_degree_point[0]:
        return 180 - math.asin((point1[1] - zero_degree_point[1])/distance_between_points(point1,zero_degree_point))
    return math.asin((point1[1] - zero_degree_point[1])/distance_between_points(point1,zero_degree_point))


def distance_between_points(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def compute_orientation(x, y, p):
    return np.cross([p[0]-x[0],p[1]-x[1]],[y[0]-x[0],y[1]-x[1]])

def graham_scan(points):
    point_min_y = points[0]
    idx = 0

    # plot(points)

    for i in range(1,len(points)):
        if point_min_y[1] > points[i][1]:
            point_min_y = points[i]
            idx = i
        elif point_min_y[1] == points[i][1] and point_min_y[0] > points[i][0]:
            point_min_y = points[i]
            idx = i

    del points[idx]

    sorted_by_angle = sorted(points,key=lambda p: get_angle_between_points(p,point_min_y))

    hull = [point_min_y,sorted_by_angle[0]]


    for i in range(1,len(sorted_by_angle)):
        # plot(hull, True)

        while compute_orientation(hull[-2],hull[-1], sorted_by_angle[i]) >= 0:

            del hull[-1]
            if len(hull)<2:
                break

        hull.append(sorted_by_angle[i])

    # plot(hull, True)

    return hull


def doIntersect(p1, q1, p2, q2):
    # Find the 4 orientations required for
    # the general and special cases
    o1 = cross_product_orientation(p1, q1, p2)
    o2 = cross_product_orientation(p1, q1, q2)
    o3 = cross_product_orientation(p2, q2, p1)
    o4 = cross_product_orientation(p2, q2, q1)

    # General case
    if ((o1 != o2) and (o3 != o4)):
        return True

    # Special Cases

    # p1 , q1 and p2 are colinear and p2 lies on segment p1q1
    if ((o1 == 0) and sameSegment(p1, p2, q1)):
        return True

    # p1 , q1 and q2 are colinear and q2 lies on segment p1q1
    if ((o2 == 0) and sameSegment(p1, q2, q1)):
        return True

    # p2 , q2 and p1 are colinear and p1 lies on segment p2q2
    if ((o3 == 0) and sameSegment(p2, p1, q2)):
        return True

    # p2 , q2 and q1 are colinear and q1 lies on segment p2q2
    if ((o4 == 0) and sameSegment(p2, q1, q2)):
        return True

    # If none of the cases
    return False

def sameSegment(p, q, r):
    if ( (q[0] <= max(p[0], r[0])) and (q[0] >= min(p[0], r[0])) and
           (q[1] <= max(p[1], r[1])) and (q[1] >= min(p[1], r[1]))):
        return True
    return False


def cross_product_orientation(a, b, c):
    val = compute_orientation(a,b,c)
    if val < 0:
        return 1
    elif val>0:
        return 2
    return 0

def check_for_intersection(vector1,vector2):
    return doIntersect(vector1[0],vector1[1],vector2[0],vector2[1])


def point_in_polygon_binary_search(point : tuple, polygon : list) -> bool:
    '''
    Function that uses binary search for determinating if the given point is inside the given polygon

     Parameters
    ----------
    point : tuple
         Tuple in format (x,y) representing point's coordinates in 2d.
    polygon : list
        List of points that form convex polygon ordered in counter-clockwise or clockwise order.

     Returns
    -------
    value : bool
        True if the point is inside the polygon, otherwise returns False.
    '''
    current_polygon = polygon
    while True:
        l = len(current_polygon)

        #if the current polygon is a triangle then stop searching

        if l == 3:
            break
        #get the representation of the diagonal between the first point in the list (the point that is first
        # added to the polygon at it's creation) and the middle point in the list of points in the polygon
        #with this diagonal we defide the polygon into left and right sub-polygon

        diagonal = (current_polygon[0], current_polygon[l//2])

        #we compute the cross product between the the vectors diagonal and (point - diagonal).
        #Based on the sign of the cross product we will determinate of the point is left or right from the diagonal vector

        cross_product = compute_orientation(diagonal[0], diagonal[1], point)

        #check if the point is left or right from the diagonal_vector
        #if it is left then we are certain that the point is not in the right part, so we can discard it and continue
        # with the same procedure with the left sub-polygon
        if cross_product > 0:
            if l == 4:
                current_polygon = current_polygon[:-1]
            else:
                current_polygon = current_polygon[:l // 2 + 1]

        # if it is right from the vector then discard the left sub-polygon and continue searching in the right sub-polygon

        elif cross_product < 0:
            if l == 4:
                current_polygon = [current_polygon[0]] + current_polygon[2:]
            else:
                current_polygon=[current_polygon[0]] + current_polygon[l // 2:]

        #if the point lies on the diagonal then we just need to form triangle with the points from the diagonal vector and
        #the next point to the middle point left or right

        else:
            current_polygon = [diagonal[0], current_polygon[l//2-1], diagonal[1]]

    #when we reduce the search space to a triangle then we just check if the point is inside the triangle
    #if the poing is located left from every side in the triangle then we can infer that the point is inside the triangle
    #thus it is inside the given polygon, otherwise the point is not in the polygon

    for i in range(1,len(current_polygon) + 1):
        if i == len(current_polygon) : i=0
        if compute_orientation(current_polygon[i-1], current_polygon[i], point) > 0:
            return False
    return True

def check_destroyed_planets_optimized(planets,tanos_army_polygon):
    destroyed_planets = []
    for planet in planets:
        if point_in_polygon_binary_search(planet, tanos_army_polygon):
            destroyed_planets.append(planet)

    return destroyed_planets


def check_destroyed_panets(planets,tanos_army_polygon):
    right_most_point = max(tanos_army_polygon,key=lambda p:p[0])
    new_right_most_point = (right_most_point[0]+1,right_most_point[1])
    destroyed_planets=[]
    for planet in planets:
        count = 0
        for i in range(1,len(tanos_army_polygon)+1):
            if i==len(tanos_army_polygon): i=0

            if check_for_intersection((planet,new_right_most_point),(tanos_army_polygon[i-1],tanos_army_polygon[i])):
                count+=1
        if count % 2!=0:
            destroyed_planets.append(planet)

    return destroyed_planets

def find_extreme_points(polygon):
    sorted_x = sorted(polygon, key=lambda p: p[0])
    sorted_y = sorted(polygon, key=lambda p: p[1])

    #left top and left bottom
    left_most_1 = sorted_x[0]
    left_most_2 = sorted_x[1]
    left_top = None
    left_bottom = None
    if left_most_1[1] > left_most_2[1]:
        left_top = left_most_1
        left_bottom = left_most_2
    else:
        left_top = left_most_2
        left_bottom = left_most_1

    # top right and bottom right
    right_most_1 = sorted_x[-1]
    right_most_2 = sorted_x[-2]
    right_top = None
    right_bottom = None
    if right_most_1[1] > right_most_2[1]:
        right_top = right_most_1
        right_bottom = right_most_2
    else:
        right_top = right_most_2
        right_bottom = right_most_1

    #bottom left and bottom right

    bottom_most_1 = sorted_y[0]
    bottom_most_2 = sorted_y[1]
    bottom_left = None
    bottom_right = None
    if bottom_most_1[0] > bottom_most_2[0]:
        bottom_right = bottom_most_1
        bottom_left = bottom_most_2
    else:
        bottom_right = bottom_most_2
        bottom_left = bottom_most_1

    # top left and top right

    top_most_1 = sorted_y[-1]
    top_most_2 = sorted_y[-2]
    top_left = None
    top_right = None
    if top_most_1[0] > top_most_2[0]:
        top_right = top_most_1
        top_left = top_most_2
    else:
        top_right = top_most_2
        top_left = top_most_1

    return [left_top,left_bottom,right_top,right_bottom,bottom_left,bottom_right,top_left,top_right]


class Avengers:
    def maximize_destroyed_planets(self,planets,tanos_army_polygon,R):
        destroyed_planets = check_destroyed_planets_optimized(planets, tanos_army_polygon)
        max_planets = destroyed_planets
        current_max = len(destroyed_planets)
        current_changed_point = None
        current_changed_op = None

        max_tanos_army = tanos_army_polygon
        for i in range(0, len(tanos_army_polygon)):
            p = tanos_army_polygon[i]
            p_x_new_plus = (p[0] + R, p[1])
            p_x_new_minus = (p[0] - R, p[1])
            p_y_new_plus = (p[0], p[1] + R)
            p_y_new_minus = (p[0], p[1] - R)

            # move the current point left for R units
            tanos_army_polygon_current = graham_scan(tanos_army_polygon[:i] + [p_x_new_minus] +
                                                     tanos_army_polygon[i + 1:])

            destroyed_planets = check_destroyed_planets_optimized(planets, tanos_army_polygon_current)
            if len(destroyed_planets) > current_max:
                current_max = len(destroyed_planets)
                current_changed_point = p
                current_changed_op = 'L'
                max_planets = destroyed_planets
                max_tanos_army = tanos_army_polygon[:i] + [p_x_new_minus] + tanos_army_polygon[i + 1:]

            # move the current point right for R units
            tanos_army_polygon_current = graham_scan(tanos_army_polygon[:i] + [p_x_new_plus] +
                                                     tanos_army_polygon[i + 1:])
            destroyed_planets = check_destroyed_planets_optimized(planets, tanos_army_polygon_current)
            if len(destroyed_planets) > current_max:
                current_max = len(destroyed_planets)
                current_changed_point = p
                max_planets = destroyed_planets
                current_changed_op = 'R'

                max_tanos_army = tanos_army_polygon[:i] + [p_x_new_plus] + tanos_army_polygon[i + 1:]

            # move the current point up for R units
            tanos_army_polygon_current = graham_scan(tanos_army_polygon[:i] + [p_y_new_plus] +
                                                     tanos_army_polygon[i + 1:])
            destroyed_planets = check_destroyed_planets_optimized(planets, tanos_army_polygon_current)
            if len(destroyed_planets) > current_max:
                current_max = len(destroyed_planets)
                current_changed_point = p
                max_planets = destroyed_planets
                current_changed_op = 'U'
                max_tanos_army = tanos_army_polygon[:i] + [p_y_new_plus] + tanos_army_polygon[i + 1:]

                # move the current point down for R units
            tanos_army_polygon_current = graham_scan(tanos_army_polygon[:i] + [p_y_new_minus] +
                                                     tanos_army_polygon[i + 1:])
            destroyed_planets = check_destroyed_planets_optimized(planets, tanos_army_polygon_current)
            if len(destroyed_planets) > current_max:
                current_max = len(destroyed_planets)
                current_changed_point = p
                max_planets = destroyed_planets
                current_changed_op = 'D'
                max_tanos_army = tanos_army_polygon[:i] + [p_y_new_minus] + tanos_army_polygon[i + 1:]

        # plot(max_tanos_army, True, planets, "Максимизиран број на планети во полигонот")

        return current_changed_point, current_changed_op, max_planets

    def maximize_destroyed_planets_optimized(self,planets,tanos_army_polygon,R):
        destroyed_planets = check_destroyed_planets_optimized(planets, tanos_army_polygon)
        max_planets = destroyed_planets
        current_max = len(destroyed_planets)
        current_changed_point = None
        current_changed_op = None
        max_tanos_army = tanos_army_polygon

        extreme_points = \
            find_extreme_points(tanos_army_polygon)


        for i in range(0, len(extreme_points)):
            p = extreme_points[i]
            p_x_new_plus = (p[0] + R, p[1])
            p_x_new_minus = (p[0] - R, p[1])
            p_y_new_plus = (p[0], p[1] + R)
            p_y_new_minus = (p[0], p[1] - R)

            # move the current point left for R units
            index_of_current_point = tanos_army_polygon.index(p)
            tanos_army_polygon_current = graham_scan(tanos_army_polygon[:index_of_current_point] + [p_x_new_minus] +
                                                     tanos_army_polygon[index_of_current_point + 1:])

            destroyed_planets = check_destroyed_planets_optimized(planets, tanos_army_polygon_current)
            if len(destroyed_planets) > current_max:
                current_max = len(destroyed_planets)
                current_changed_point = p
                current_changed_op = 'L'
                max_planets = destroyed_planets
                max_tanos_army = tanos_army_polygon[:index_of_current_point] + [p_x_new_minus] + tanos_army_polygon[index_of_current_point + 1:]

            # move the current point right for R units
            tanos_army_polygon_current = graham_scan(tanos_army_polygon[:index_of_current_point] + [p_x_new_plus] +
                                                     tanos_army_polygon[index_of_current_point + 1:])
            destroyed_planets = check_destroyed_planets_optimized(planets, tanos_army_polygon_current)
            if len(destroyed_planets) > current_max:
                current_max = len(destroyed_planets)
                current_changed_point = p
                max_planets = destroyed_planets
                current_changed_op = 'R'

                max_tanos_army = tanos_army_polygon[:index_of_current_point] + [p_x_new_plus] + tanos_army_polygon[index_of_current_point + 1:]

            # move the current point up for R units
            tanos_army_polygon_current = graham_scan(tanos_army_polygon[:index_of_current_point] + [p_y_new_plus] +
                                                     tanos_army_polygon[index_of_current_point + 1:])
            destroyed_planets = check_destroyed_planets_optimized(planets, tanos_army_polygon_current)
            if len(destroyed_planets) > current_max:
                current_max = len(destroyed_planets)
                current_changed_point = p
                max_planets = destroyed_planets
                current_changed_op = 'U'
                max_tanos_army = tanos_army_polygon[:index_of_current_point] + [p_y_new_plus] + tanos_army_polygon[index_of_current_point + 1:]

                # move the current point down for R units
            tanos_army_polygon_current = graham_scan(tanos_army_polygon[:index_of_current_point] + [p_y_new_minus] +
                                                     tanos_army_polygon[index_of_current_point + 1:])
            destroyed_planets = check_destroyed_planets_optimized(planets, tanos_army_polygon_current)
            if len(destroyed_planets) > current_max:
                current_max = len(destroyed_planets)
                current_changed_point = p
                max_planets = destroyed_planets
                current_changed_op = 'D'
                max_tanos_army = tanos_army_polygon[:index_of_current_point] + [p_y_new_minus] + tanos_army_polygon[index_of_current_point + 1:]

        # plot(max_tanos_army, True, planets,title= "Максимизиран број на планети во полигонот")

        return current_changed_point, current_changed_op, max_planets


    def destroyed_planets(self, planets, tanos_army,R):
        # plot_planets_and_army(planets,tanos_army)
        tanos_army_polygon = graham_scan(tanos_army)
        # plot(tanos_army_polygon,True,planets,title="Почетен полигон")
        destroyed_planets_without_adjustment = check_destroyed_planets_optimized(planets, tanos_army_polygon)
        # return self.maximize_destroyed_planets(planets,tanos_army_polygon,R) if len(tanos_army_polygon)<9 \
        #        else self.maximize_destroyed_planets_optimized(planets,tanos_army_polygon,R)
        moved_space_ship,direction, planets_to_be_destroyed = self.maximize_destroyed_planets(planets, tanos_army_polygon, R)
        if len(destroyed_planets_without_adjustment) >= len(planets_to_be_destroyed):
            return str(len(planets_to_be_destroyed))+" "+" ".join([str(p[0])+"-"+str(p[1]) for p in planets_to_be_destroyed])

        return str(len(planets_to_be_destroyed)) +" "+ str(moved_space_ship[0])+"-"+str(moved_space_ship[1])+ \
               " "+direction +" "+" ".join([str(p[0])+"-"+str(p[1]) for p in planets_to_be_destroyed])


if __name__=='__main__':
    #broj na koordinati za niva1
    N = int(input())
    planeti = []
    for i in range(N):
        planeta = input()
        planeti.append((int(planeta.split(" ")[0]),int(planeta.split(" ")[1])))

    # broj na koordinati za niva2
    K = int(input())
    vselenski_brodovi_tanos = []
    for i in range(K):
        vselenski_brod = input()
        vselenski_brodovi_tanos.append((int(vselenski_brod.split(" ")[0]),int(vselenski_brod.split(" ")[1])))

    R = int(input())

    print(Avengers().destroyed_planets(planeti,vselenski_brodovi_tanos,R))

# print(Avengers().destroyed_planets(
#         [(13, 6), (16, 6), (1, 9), (7, 18), (12, 22), (10, 20), (29, 5), (24, 21), (4,21),(3, 20), (11, 14), (25, 16), (23, 23), (7, 8), (1, 16), (10, 21)],
#       [(1,1),(5,6),(29,0),(28,5),(30,20),(23,25),(16,23),(10,15),(3,10),(-1,13),(0,5),(5,20),(4,19),(10,0),(15,24),(31,5)], 3))
#

# s = check_destroyed_planets_optimized([(13, 6), (16, 6), (1, 9), (7, 18), (12, 22), (10, 20), (29, 5), (24, 21), (4,21),(3, 20), (11, 14), (25, 16), (23, 23), (7, 8), (1, 17), (10, 21)],
# [(10, 0), (29, 0), (31, 5), (30, 20), (23, 25), (15, 24), (5, 20), (4, 22), (-1, 13), (0, 5), (1, 1)])
# print(s)
