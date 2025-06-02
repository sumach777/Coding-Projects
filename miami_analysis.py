import fastf1 as f1
import fastf1.plotting
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

session23 = f1.get_session(2023, "Miami", "Q")
session23.load()
norris23 = session23.laps.pick_drivers("NOR").pick_fastest()
nor_data23 = norris23.get_car_data()
nort23 = nor_data23["Time"]
norv23 = nor_data23["Speed"]

session24 = f1.get_session(2024, "Miami", "Q")
session24.load()
norris24 = session24.laps.pick_drivers("NOR").pick_fastest()
nor_data24 = norris24.get_car_data()
nort24 = nor_data24["Time"]
norv24 = nor_data24["Speed"]

piastri23 = session23.laps.pick_drivers("PIA").pick_fastest()
pia_data23 = piastri23.get_car_data()
piat23 = pia_data23["Time"]
piav23 = pia_data23["Speed"]

piastri24 = session24.laps.pick_drivers("PIA").pick_fastest()
pia_data24 = piastri24.get_car_data()
piat24 = pia_data24["Time"]
piav24 = pia_data24["Speed"]

nor, ax = plt.subplots()
ax.plot(nort23, norv23, label='2023')
ax.plot(nort24, norv24, label="2024")
ax.set_xlabel('Time')
ax.set_ylabel('Speed [Km/h]')
ax.set_title("Norris Miami 2023 vs 2024")
ax.legend()


pia, ay = plt.subplots()
ay.plot(piat23, piav23, label='2023')
ay.plot(piat24, piav24, label="2024")
ay.set_xlabel('Time')
ay.set_ylabel('Speed [Km/h]')
ay.set_title("Piastri Miami 2023 vs 2024")
ay.legend()
plt.show()

