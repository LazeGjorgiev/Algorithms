from matplotlib import pyplot as plt
import math
import numpy as np

def generate_random_points(x_max, y_max, number = 10):
    return list(zip(np.random.randint(0,x_max,number),np.random.randint(0,y_max,number)))

def plot(points1, show_hull = False, points2=None,title = None):
    xs,ys = zip(*points1)

    plt.scatter(xs,ys,c='r')

    if(show_hull):
        for i in range(1, len(points1) + 1):
            if i ==len(points1): i=0
            plt.plot((points1[i - 1][0], points1[i][0]), (points1[i - 1][1], points1[i][1]), c='red')

    if(points2):
        xs, ys = zip(*points2)

        plt.scatter(xs, ys, c='r')

        if (show_hull):
            for i in range(1, len(points2) + 1):
                if i == len(points2): i = 0
                plt.plot((points2[i - 1][0], points2[i][0]), (points2[i - 1][1], points2[i][1]), c='blue')


    if title!=None:
        plt.title(title)
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

def compute_area_convex_hull(polygon):
    x_vector = [p[0] for p in polygon]
    y_vector = [p[1] for p in polygon]

    part1= 0
    for i in range(len(x_vector)):
        if i == len(x_vector)-1 :
            part1+= x_vector[i]*y_vector[0]
            part1-=x_vector[0]*y_vector[i]
            break
        part1 += x_vector[i] * y_vector[i+1]
        part1 -= x_vector[i+1] * y_vector[i]
    return part1*0.5


class Zemjodelec:
    def povrsina_na_sosednata_niva(self,N,X1Y1,K,X2Y2):
        koordinati_povrsina1 = []
        for i in range(0,N):
            koord = X1Y1[i].split(" ")
            koordinati_povrsina1.append((int(koord[0]),int(koord[1])))

        krajni_koordinati_povrsina_2 = []
        for i in range(0, K):
            koord = X2Y2[i].split(" ")
            krajni_koordinati_povrsina_2.append((int(koord[0]), int(koord[1])))

        povrsina1_polygon = graham_scan(koordinati_povrsina1)
        spoeni_polygon = graham_scan(povrsina1_polygon+krajni_koordinati_povrsina_2)

        # plot(povrsina1_polygon,True,title="Земјоделска површина 1")
        # plot(spoeni_polygon,True,title="Вкупна земјоделска површина")
        # plot(spoeni_polygon,True,povrsina1_polygon,title="Вкупна земјоделска површина - делови")

        povrsina_1 = compute_area_convex_hull(povrsina1_polygon)
        povrsina_spoeni = compute_area_convex_hull(spoeni_polygon)

        return povrsina_spoeni - povrsina_1

if __name__=='__main__':

    #broj na koordinati za niva1
    N = int(input())
    koordinati_niva1 = []
    for i in range(N):
        koordinati_niva1.append(input())

    # broj na koordinati za niva2
    K = int(input())
    koordinati_niva2 = []
    for i in range(K):
        koordinati_niva2.append(input())

    print(Zemjodelec().povrsina_na_sosednata_niva(N,koordinati_niva1,K,koordinati_niva2))
