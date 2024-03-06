
import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import Union
from scipy import interpolate
from scipy.interpolate import CubicSpline
import pandas as pd
from shapely.geometry import LineString

sigma_3 = 40

Rc = 8
Rp = 1
sigma_3_c = 0
sigma_3_p = 0


def circlepoints(points, radius, center):
    x = []
    y = []
    slice = 2 * np.pi / (points-1)
    for i in range(points):
        angle = slice * i
        x.append(center[0] + radius*np.cos(angle))
        y.append(center[1] + radius*np.sin(angle))

    return x, y
xc, yc = np.asarray(circlepoints(10000, Rc, [Rc, 0]))
xp, yp = np.asarray(circlepoints(10000, Rp, [-Rp, 0]))

plt.style.use('bmh')
plt.xlim(-Rc*3, Rc*3)
plt.ylim(-Rc*3, Rc*3)
plt.plot(xc, yc)
plt.plot(xp, yp)







# circle = plt.Circle((Rc, 0), Rc, color='r', fill=False, linewidth=2, alpha= .3)
# plt.gca().add_patch(circle)
# circle = plt.Circle((-Rp, 0), Rp, color='b', fill=False, linewidth=2)
# plt.gca().add_patch(circle)
plt.grid(which='major', linewidth=1.2)


# plt.plot(sigma_3, tao)
#
# plt.xlim(-Rc*4, Rc*4)
# plt.ylim(-Rc*4, Rc*4)

# plt.show()

K = np.array([
2.00, 1.80, 1.60, 1.40, 1.20, 1.00, 0.90, 0.80, 0.70, 0.60, 0.50,
0.40, 0.30, 0.20, 0.10, 0.08, 0.06,0.05, 0.04, 0.0300, 0.0200, 0.0100,
0.0080, 0.0060, 0.0050, 0.0040, 0.0030, 0.0020, 0.0010, 0.0009,
0.0008, 0.0007, 0.0006, 0.0005, 0.0004, 0.0003, 0.0002, 0.0001])

L = np.array([
0.6720, 0.6600, 0.6450, 0.6310, 0.6010, 0.5630, 0.5400, 0.5110,
0.4820, 0.4440, 0.3990, 0.3410, 0.2865, 0.2151, 0.1294, 0.1101,
0.0882, 0.0771, 0.0653, 0.0526, 0.0388, 0.0231, 0.0196, 0.0157,
0.0137, 0.0115, 0.0094, 0.0069, 0.0041, 0.0038, 0.0035, 0.0031,
0.0028, 0.0024, 0.0020, 0.0016, 0.0012, 0.0007])

temp = interpolate.interp1d(K, L)
K = np.arange(min(K), max(K), 0.0001)
L = np.around(np.asarray(temp(K)), 4)

K_L_array = np.array([[K], [L]])
K_L_dict = dict(zip(K, L))



q1_q2_array = np.array([
1.3, 1.5, 2.0, 2.5, 3.0,  3.5, 4.0, 4.4, 4.8, 5.2, 5.6, 6.0, 6.4, 6.8,  7.0, 7.2,
7.4, 7.6, 7.8, 8.0, 8.2, 8.4, 8.6, 8.8, 9.0, 9.2, 9.4, 9.6, 9.8, 10.0, 10.2, 10.4,
10.6, 10.8, 11.0, 11.2, 11.4, 11.6, 11.8, 12.0, 12.2, 12.4, 12.6, 12.8, 13.0, 13.5,
14.0, 14.5, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 30.0
])

q2_array = np.array([
0.6751, 0.6567, 0.6138, 0.5704, 0.5253, 0.4784, 0.4308, 0.3936,
0.3584, 0.3262, 0.2972, 0.2717, 0.2493, 0.2297, 0.2208, 0.2123,
0.2047, 0.1974, 0.1906, 0.1841, 0.1781, 0.1724, 0.1670, 0.1619,
0.1573, 0.1526, 0.1483, 0.1442, 0.1403, 0.1366, 0.1331, 0.1298,
0.1266, 0.1235,  0.1206, 0.1178, 0.1152, 0.1126, 0.1102, 0.1079,
0.1056, 0.1035, 0.1014, 0.0994, 0.0975, 0.0930, 0.0889, 0.0851,
0.0816,  0.0754, 0.0701, 0.0654, 0.0614, 0.0578, 0.0546, 0.0517,
0.0491, 0.0467, 0.0446, 0.0363
])

K1_q1_array = np.array([
1.1418, 1.1118, 0.7317, 0.5252, 0.3933, 0.3011, 0.2335, 0.1918,
0.1586, 0.1322, 0.1111, 0.0942, 0.0807, 0.0697, 0.0649, 0.0607,
0.0568, 0.0533, 0.0500, 0.0471, 0.0443, 0.0419, 0.0396, 0.0375,
0.0356, 0.0337, 0.0320, 0.0305, 0.0290, 0.0277, 0.0265, 0.0253,
0.0242, 0.0231, 0.0222, 0.0213, 0.0204, 0.0196, 0.0189, 0.0181,
0.0175, 0.0169, 0.0162, 0.0157, 0.0151, 0.0139, 0.0128, 0.0118,
0.0109, 0.0095, 0.0083, 0.0073, 0.0065, 0.0058, 0.0052, 0.0047,
0.0043, 0.0039, 0.0036, 0.0024
])


temp = interpolate.interp1d(q1_q2_array, q2_array)
temp2 = interpolate.interp1d(q2_array, K1_q1_array)
q1_q2_array = np.around(np.linspace(min(q1_q2_array), max(q1_q2_array), 20000),3)
q2_array = np.around(temp(q1_q2_array), 4)
K1_q1_array = np.around(temp2(q2_array), 4)
q1_q2_dict = dict(zip(q1_q2_array, q2_array))
q2_K1_q1_dict = dict(zip(q2_array, K1_q1_array))

print('q1_q2_dict', q1_q2_dict)
print('q1_q2_K1_dict', q2_K1_q1_dict)

sigma_c = Rc*2
sigma_p = Rp*2
q1_q2 = round(sigma_c/sigma_p, 3)
print('q1_q2', q1_q2)
q2 = q1_q2_dict[q1_q2]
print('q2', q2)
k1_q1 = q2_K1_q1_dict[q2]
a = sigma_c / (2 * q2)
sigma0 = round(a*k1_q1, 4)

q1 = q2*sigma_p/sigma_c
sigma_z = 111
# k=[]
sigma_array = []
tau_array = []
# k.append(round((sigma_z+sigma0)/a, 4))
for i in K:
    sigma_array.append(i*a-sigma0)
    l = K_L_dict[i]
    tau_array.append(l * a)


plt.plot(sigma_array, tau_array)

sigma_array = np.around(np.asarray(sigma_array), 1)
tau_array = np.around(np.asarray(tau_array), 1)

sigma_array_tau_array = dict(zip(sigma_array, tau_array))
print(sigma_array_tau_array)
print(sigma_array_tau_array[sigma_3])
plt.show()
