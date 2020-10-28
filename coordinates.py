import numpy as np
import matplotlib.pyplot as plt

'''
Transform from cartesian to spherical coordinates.
x = r sin(phi) cos(theta)
y = r sin(phi) sin(theta)
z = r cos(phi)
where theta measures on x-y plane
and phi measures off z-axis
'''
def cartesian_to_spherical(x, y, z):
  r = np.sqrt(x**2 + y**2 + z**2)
  theta = np.arctan2(y, x)
  phi = np.arccos(z/r)
  return (r, theta, phi)

'''
Transform from spherical to cartesian coordinates.
x = r sin(phi) cos(theta)
y = r sin(phi) sin(theta)
z = r cos(phi)
where theta measures on x-y plane
and phi measures off z-axis
'''
def spherical_to_cartesian(r, theta, phi):
  x = r * np.sin(phi) * np.cos(theta)
  y = r * np.sin(phi) * np.sin(theta)
  z = r * np.cos(phi)
  return (x, y, z)

'''
Transform from equatorial to ecliptic coordinates via rotation.
ra: right ascension
dec: declination
eps: obliquity of ecliptic
'''
def equatorial_to_ecliptic(ra, dec, eps=0.418879):
  R = np.array([[1, 0, 0],
                [0, np.cos(eps), np.sin(eps)],
                [0, -np.sin(eps), np.cos(eps)]])
  v_equ = np.array(spherical_to_cartesian(1.0, ra, np.pi/2-dec))
  x_ecl, y_ecl, z_ecl = np.dot(R, v_equ)
  return cartesian_to_spherical(x_ecl, y_ecl, z_ecl)

def plot(n=100):
  plt.style.use('dark_background')
  plt.figure(figsize=(12,8))
  plt.subplot(projection="aitoff")

  ras = np.linspace(-np.pi, np.pi, n)
  decs = np.zeros(n)
  # ras = np.linspace(-np.pi, np.pi, n)
  # decs = np.linspace(-np.pi/2, np.pi/2, n)
  for ra, dec in zip(ras, decs):
    r, theta, phi = equatorial_to_ecliptic(ra, dec)
    plt.plot(ra, dec, color='tab:red', marker='o', linestyle='None', markersize=5)
    plt.plot(theta, np.pi/2-phi, color='tab:orange', marker='o', linestyle='None', markersize=5)

  plt.grid(True)
  plt.xlabel("longitude (deg)")  
  plt.ylabel("latitude (deg)")
  # plt.legend()
  plt.show()
