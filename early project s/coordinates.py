from os import chdir, listdir, getcwd
import numpy as np
import pandas as pd


def cartesian_to_spherical(x, y, z):
    '''
    Transform from cartesian to spherical coordinates.
    x = r sin(phi) cos(theta)
    y = r sin(phi) sin(theta)
    z = r cos(phi)
    where theta measures on x-y plane
    and phi measures off z-axis
    '''
    r = np.sqrt(x**2 + y**2 + z**2)
    theta = np.arctan2(y, x)
    phi = np.arccos(z / r)
    return (r, theta, phi)


def spherical_to_cartesian(r, theta, phi):
    '''
    Transform from spherical to cartesian coordinates.
    x = r sin(phi) cos(theta)
    y = r sin(phi) sin(theta)
    z = r cos(phi)
    where theta measures on x-y plane
    and phi measures off z-axis
    '''
    x = r * np.sin(phi) * np.cos(theta)
    y = r * np.sin(phi) * np.sin(theta)
    z = r * np.cos(phi)
    return (x, y, z)


def equatorial_to_ecliptic(ra, dec, eps=0.418879):
    '''
    Transform from equatorial to ecliptic coordinates via rotation.
    ra: right ascension
    dec: declination
    eps: obliquity of ecliptic
    '''
    R = np.array([[1, 0, 0],
                [0, np.cos(eps), np.sin(eps)],
                [0, -np.sin(eps), np.cos(eps)]])
    v_equ = np.array(spherical_to_cartesian(1.0, ra, np.pi / 2 - dec))
    x_ecl, y_ecl, z_ecl = np.dot(R, v_equ)
    return cartesian_to_spherical(x_ecl, y_ecl, z_ecl)


def transform_csv(fname, ra_colname='R.A._(a-app)', dec_colname='DEC_(a-app)'):
    rad_change = lambda x: x * np.pi / 180.0
    deg_change = lambda x: x * 180.0 / np.pi

    df = pd.read_csv(fname)
    df = df.rename(columns=lambda h: h.strip())
    df = df.drop(['', '.1', 'Unnamed: 12'], axis=1)

    coords_equ = df[[ra_colname, dec_colname]]
    transform = lambda c: equatorial_to_ecliptic(rad_change(c[0]), rad_change(c[1]))
    _, df['RA_ECL_ANC'], df['DEC_ECL_ANC'] = zip(*coords_equ.apply(transform, axis=1))

    df['DEC_ECL_ANC'] = np.pi / 2 - df['DEC_ECL_ANC']

    df['RA_ECL_ANC'] = df['RA_ECL_ANC'].apply(deg_change)
    df['DEC_ECL_ANC'] = df['DEC_ECL_ANC'].apply(deg_change)

    df.to_csv(fname, index=False)


if __name__ == '__main__':
    chdir(getcwd())
    for file in listdir():
        if file.endswith('.csv'):
            transform_csv(file)
