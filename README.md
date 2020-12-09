# Comparison of Ancient Astronomical Models (Final Project)

To see a comparison of Greek and Indian astronomical models, check out `final.ipynb`. For basic data exploration, check out `project.ipynb`, which allows for interactive scatter plots and frequency analysis.

# Ancient Indian Ephemerides Data (Early Project)

This repository stores an ephemerides dataset relative to an observer on Earth of the planets, the Sun, and the Moon, calculated through [NASA Horizons JPL](https://ssd.jpl.nasa.gov/). By procedurally sending an email request to the Horizons system, `generate_csv.py` allows easy customizability with regards to observer location, time frame, and sample frequency. `coordinates.py` cleans the dataset as well as provides a new change of coordinates, what we have determined to be the historical measurements of Indian astronomers during the period 900CE-1300CE. This new coordinate data is in the columns `RA_ECL_ANC, DEC_ECL_ANC`.

## Contributors

Alan Zhou, Anish Nag, Jonathan Wang, Naveen Gopalan
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pandas.

```bash
pip install pandas
```

## Usage
```python
jpl_email = "horizons@ssd.jpl.nasa.gov" # NASA Horizons JPL Email
gmail = "<INSERT EMAIL>@gmail.com"   # Insert gmail of choice. Can also use the 'astro.cs189@gmail.com' in the code
password = "<INSERT PASSWORD HERE>"  # Insert email password here. Contact Repository Owners for the password of 'astro.cs189@gmail.com'

bodies = "'1'\n'2'\n'4'\n'5'\n'6'\n'7'\n'8'\n'10'\n'301'" # Major Bodies according to Horizons. Respectively: Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune, Sun, Moon.
site_coord = "'75.79,23.17,0.5'" # Ujjain, India. Latitude, Longitude, Elevation (km)

# Must include AD|BC for years < 1000
start_time = "'0900AD-01-01'"
stop_time = "'1300-12-31'"
step_size = "'2 d'"
```

These are the basic user parameters as noted in `generate_csv.py`. For a list of more solar system bodies and general formatting, please visit [Horizons JPL](https://ssd.jpl.nasa.gov/). To generate the csv files, simply execute `python3 generate_csv.py` in the terminal after filling out the relevant user parameters (gmail, password, bodies, etc. All of the variables listed in the code block above). Note that only the gmail and password need to be changed to create a valid ancient Indian ephemerides dataset; however, feel free to change site_coord (observer location), start time, stop time, and others. Make sure that the inbox of the email being used does not contain any emails for NASA Horizons JPL before running the script, so as to not process extra emails. Also, ensure that the email is a gmail with "Less secure app access" on.

<p align="center">
  <img src="https://github.com/NaveenGop/astro-data/blob/main/example_params.jpg" align="middle" width="350">
  <br>Figure 1. Example Parameters
</p>

The raw command to JPL is of this structure, stored in the `messages variable`. Visit [Horizons JPL](https://ssd.jpl.nasa.gov/?horizons_doc#customizing) in the Observer Table section for a list of more measurements as well as more information about the data in general, such as positional uncertainity, other solar system bodies, and more. By changing the `QUANTITIES` command, more columns can be requested (e.g. `QUANTITIES='18, 33'` for 18: Heliocentric ecliptic longitude & latitude; 33: Galactic latitude). Right now, the columns requested are `R.A._(ICRF), DEC_(ICRF), R.A._(a-app), DEC_(a-app), Azi_(a-app), Elev_(a-app), ObsEcLon, ObsEcLat, L_Ap_SOL_Time`. Other fields, such as Time Zone, Ang_Formats, etc., can be changed or removed to better reflect the user's needs.
```
!$$SOF
COMMAND = {bodies}
CENTER= 'coord@399'
COORD_TYPE= 'GEODETIC'
SITE_COORD= {site_coord}
MAKE_EPHEM= 'YES'
TABLE_TYPE= 'OBSERVER'
START_TIME= {start_time}
STOP_TIME= {stop_time}
STEP_SIZE= {step_size}
CAL_FORMAT= 'CAL'
TIME_DIGITS= 'MINUTES'
ANG_FORMAT= 'DEG'
OUT_UNITS= 'KM-S'
RANGE_UNITS= 'AU'
APPARENT= 'AIRLESS'
SUPPRESS_RANGE_RATE= 'NO'
SKIP_DAYLT= 'NO'
EXTRA_PREC= 'NO'
R_T_S_ONLY= 'NO'
REF_SYSTEM= 'J2000'
CSV_FORMAT= 'YES'
OBJ_DATA= 'NO'
TIME_ZONE = '+05:30'
QUANTITIES= '1,2,4,31,34'
!$$EOF
```

To process the data in terms of removing excess columns and adding the Indian astronomer measurements, execute `python3 coordinates.py` in the directory with all the .csv ephemerides files.

<p align="center">
  <img src="https://github.com/NaveenGop/astro-data/blob/main/example_dir.png" align="middle" >
  <br>Figure 2. Example Directory
</p>

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
