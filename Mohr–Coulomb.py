import numpy as np
import matplotlib.pyplot as plt


# Пример заданных значений
sigma_3 = 110
Rc = 400
Rp = 50
sigma_3_c = 0
sigma_3_p = 0


def data_processing(Rc, Rp):
    '''
    Фунция для нахождения координат огибающей, тау по заданной сигме и координат огибающей
    :param Rc: Радиус круга сжатия
    :param Rp: Радиус круга растяжения
    :return: sigma_array, tau_array, tau
    '''


    def methodical_data():
        '''
        функция для создания массивов q1_q2_array,q2_array, k1_q1_array из ГОСТ 21153.8-88
        :return: q1_q2_array,q2_array, k1_q1_array
        '''
        q1_q2_array = np.array([
            1.3, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.4, 4.8, 5.2, 5.6, 6.0, 6.4,
            6.8, 7.0, 7.2, 7.4, 7.6, 7.8, 8.0, 8.2, 8.4, 8.6, 8.8, 9.0, 9.2,
            9.4, 9.6, 9.8, 10.0, 10.2, 10.4, 10.6, 10.8, 11.0, 11.2, 11.4, 11.6,
            11.8, 12.0, 12.2, 12.4, 12.6, 12.8, 13.0, 13.5, 14.0, 14.5, 15.0,
            16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 30.0
        ])

        q2_array = np.array([
            0.6751, 0.6567, 0.6138, 0.5704, 0.5253, 0.4784, 0.4308, 0.3936,
            0.3584, 0.3262, 0.2972, 0.2717, 0.2493, 0.2297, 0.2208, 0.2123,
            0.2047, 0.1974, 0.1906, 0.1841, 0.1781, 0.1724, 0.1670, 0.1619,
            0.1573, 0.1526, 0.1483, 0.1442, 0.1403, 0.1366, 0.1331, 0.1298,
            0.1266, 0.1235, 0.1206, 0.1178, 0.1152, 0.1126, 0.1102, 0.1079,
            0.1056, 0.1035, 0.1014, 0.0994, 0.0975, 0.0930, 0.0889, 0.0851,
            0.0816, 0.0754, 0.0701, 0.0654, 0.0614, 0.0578, 0.0546, 0.0517,
            0.0491, 0.0467, 0.0446, 0.0363
        ])

        k1_q1_array = np.array([
            1.1418, 1.1118, 0.7317, 0.5252, 0.3933, 0.3011, 0.2335, 0.1918,
            0.1586, 0.1322, 0.1111, 0.0942, 0.0807, 0.0697, 0.0649, 0.0607,
            0.0568, 0.0533, 0.0500, 0.0471, 0.0443, 0.0419, 0.0396, 0.0375,
            0.0356, 0.0337, 0.0320, 0.0305, 0.0290, 0.0277, 0.0265, 0.0253,
            0.0242, 0.0231, 0.0222, 0.0213, 0.0204, 0.0196, 0.0189, 0.0181,
            0.0175, 0.0169, 0.0162, 0.0157, 0.0151, 0.0139, 0.0128, 0.0118,
            0.0109, 0.0095, 0.0083, 0.0073, 0.0065, 0.0058, 0.0052, 0.0047,
            0.0043, 0.0039, 0.0036, 0.0024
        ])

        return q1_q2_array, q2_array, k1_q1_array

    q1_q2_array, q2_array, k1_q1_array = methodical_data()


    def calculate_parameters(q1_q2_array, q2_array, k1_q1_array):
        '''
        Фунция для нахождения sigma0, a
        :param q1_q2_array: массив по ГОСТ 21153.8-88
        :param q2_array: массив по ГОСТ 21153.8-88
        :param k1_q1_array: массив по ГОСТ 21153.8-88
        :return: sigma0, a
        '''

        # Расчёт параметров для заданных радиусов кругов
        sigma_c = Rc * 2
        sigma_p = Rp * 2
        q1_q2 = sigma_c / sigma_p
        q2 = np.interp(q1_q2, q1_q2_array, q2_array)
        k1_q1 = np.interp(q1_q2, q1_q2_array, k1_q1_array)
        a = sigma_c / (2 * q2)
        sigma0 = a * k1_q1
        return sigma0, a

    sigma0, a = calculate_parameters(q1_q2_array, q2_array, k1_q1_array)
    return sigma0, a


def calculate_tau(sigma, sigma0, a):
    '''
    Функция для нахождения tau  огибающей
    :param sigma: Задаётся для нахождения tau
    :return: tau  огибающей
    '''
    # Нахождение tau по sigma для огибающей
    tau = 0.73 * ((((sigma + sigma0) / a) ** 2) / (((sigma + sigma0) / a) ** 2 + 1)) ** (3 / 8) * a
    return tau


if __name__ == '__main__':
    sigma0, a = data_processing(Rc, Rp)
    tau = calculate_tau(sigma_3, sigma0, a)
    print('sigma =', sigma_3, 'tau =', tau)
    tau_array = calculate_tau(np.arange(-sigma0, Rc*4, 0.01), sigma0, a)  # Нижний предел -sigma0, верхний любой
    plt.style.use('bmh')
    plt.ylabel('τ, МПа')
    plt.xlabel('σ, МПа')
    circle = plt.Circle((Rc, sigma_3_c), Rc, color='#4189C5', fill=False, linewidth=2)
    plt.gca().add_patch(circle)
    circle = plt.Circle((-Rp, sigma_3_p), Rp, color='#A01234', fill=False, linewidth=2)
    plt.gca().add_patch(circle)
    plt.xlim(-Rc, Rc * 3)
    plt.ylim(-Rc * 2, Rc * 2)
    plt.plot(np.arange(-sigma0, Rc*4, 0.01), tau_array, color='#8955AC')  # Нижний предел -sigma0, верхний любой
    plt.show()
