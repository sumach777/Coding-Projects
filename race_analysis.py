import fastf1 as f1
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

schedule_24 = f1.get_event_schedule(2024)

norris_avg = []
piastri_avg = []

for i in schedule_24["EventName"]:
    session = f1.get_session(2024, i, "Q")
    session.load(telemetry=False, laps=True, weather=False, messages=False)
    norris = session.laps.pick_drivers("NOR")
    norris_times = norris["LapTime"].dt.total_seconds()
    norris_avg.append(norris_times.mean())

    piastri = session.laps.pick_drivers("PIA")
    piastri_times = piastri["LapTime"].dt.total_seconds()
    piastri_avg.append(piastri_times.mean())

results = pd.DataFrame({"Event" : schedule_24["EventName"], "Norris" : norris_avg, "Piastri" : piastri_avg})



delta = results["Norris"] - results["Piastri"]
plt.figure(figsize=(12, 6))
plt.plot(results["Event"], delta)
plt.title("Lando Norris vs Oscar Piastri - 2024 Qualifying Fastlaps")
plt.ylabel("Time Difference (seconds)")
plt.xlabel("Grand Prix")
plt.show()