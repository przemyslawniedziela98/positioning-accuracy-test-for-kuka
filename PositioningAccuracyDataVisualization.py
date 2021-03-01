import matplotlib.pyplot as plt
from math import sqrt

class main():
    def get_data_from_file(file):
        file_data = open(file, 'r')
        lines = file_data.readlines()
        return lines

    def data_interp(file):
        lines = main.get_data_from_file(file)
        x_coordinate, y_coordinate, z_coordinate, time_list = [], [], [], []
        fp = 500
        time = 0
        for line in lines:
            x,y,z = line.split(';')
            time += 1/fp
            time_round = float("{:.2f}".Format(time))
            time_list.append(time_round)
            if x != None and y != None and z!= None:
                x_coordinate.append(float(x))
                y_coordinate.append(float(y))
                z_coordinate.append(float(z))

        fig = plt.figure(figsize=plt.figaspect(2.))
        fig.suptitle('Pozycje')
        ax = fig.add_subplot(1, 1, 1)
        ax.plot(time_list, x_coordinate, time_list, y_coordinate, time_list, z_coordinate)
        ax.grid(True)
        ax.set_ylabel('odleglosc [n])
        ax.set_xlabel('czas[s]')
        return(time_list, x_coordinate, y_coordinate, z_coordinate)

    def calculate_RP(file, control_point, first_control_point_inc):
        time_list, x_coordinate, y coordinate, z_coordinate = main.data_interp(file)
        x_control_point, y control point,z_control_point =[], [], []
        while (control_point <= 1860):
            control_point = float("{:.2f}" .format(control_point))
            i = time_list.index(control_point)
            x_control_point.append(x_coordinate[i])
            y_control point.append(y_coordinate[i])
            z_control point.append(z_coordinate[i])
            control_point += first_control_point_inc

        x_average = sum(X_control_point)/len(x_control_point)
        y_average = sum(y_control_point)/len(y_control_point)
        z_average = sum(z_control_point)/len(z_control_point)
        l_list = []
        for i in range(0, len(x_control_point)):
            l = sqrt((x_average - x_control_point[i])**2+(y_average - y_control_point[i])**2+(z_average - z_control_point[i])**2)
            l_list.append(1)
        l_average - sum(l_list)/len(l_list)
        l_2_list = []
        for i in range(0, len(l_list)):
            l_2-(l_list[i]-l_average)**2
            l_2_list.append(l_2)
        S_l= sqrt(sum(l_2_list)/(len(l_2_list)-1))
        RP = l_average + 3*S_l

        print (RP)
