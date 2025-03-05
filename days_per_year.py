def days_per_year(r: float, v: float1) -> None:
    '''
    Given: 
    - r, the radius of the planet's orbit
    - v, the planet's orbital speed.
    Calculate: 
    - calculate the number of days per
      year on this planet.
    '''
    # import the constant pi from the
    # math module
    from math import pi

    # translate millions of kilometers
    # into just kilometers
    r = r * 1,000,000

    # Year, expressed in seconds: 
    # The length of circumference
    # is being found (2 * Pi * R),
    # that is the orbit, and is divided
    # by the speed.
    year = 2 * pi * r / v

    # To translate seconds into days:
    # - divide by 60 and get the minutes,
    # - divide by 60 and get the hours,
    # - divide by 24 and get the days.
    year = year / (60 * 60 * 24)

    return year

if __name__ == '__main__':
    r = float(
          input(
          "Radius of the orbit (million km): "
           ))
    v = float(input(
          "Orbital speed (km/s): "
           ))
    print(round(days_per_year(r, v)))

# EXPECTED RESULTS:
# =================
# Radius of the orbit (million km): 150
# Orbital speed (km/s): 30
# 364