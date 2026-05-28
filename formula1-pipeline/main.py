import fastf1
import fastf1.plotting
import os
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs('cache', exist_ok=True)

fastf1.Cache.enable_cache('cache')

class drivers:
    def __init__(self, year: int, race: str, sessionn: str):
        self.fastf1 = fastf1.get_session(year, race, sessionn)
        self.fastf1_plotting = fastf1.plotting.setup_mpl(mpl_timedelta_support=True, color_scheme='fastf1')
        
    def all_drivers(self):
        race = self.fastf1
        race.load()
        for i in race.drivers:
            print(i)
    
    def fastest_q_lap(self, driver: str):
        race = self.fastf1
        race.load()
        fastest = race.laps.pick_driver(driver).pick_fastest()
        return fastest   
    
    def laps_comparison(self, drivers: tuple):
        race = self.fastf1
        fig, ax = plt.subplots(figsize=(10, 6))
        for driver in drivers:
            driver_laps = race.laps.pick_drivers(driver).pick_quicklaps()
            driver_laps = driver_laps.reset_index()
            
        ax.plot(driver_laps['LapNumber'], driver_laps['LapTime'], 
            label=driver)
        ax.set_xlabel('Lap Number')
        ax.set_ylabel('Lap Time')
        ax.legend()
        plt.show()



def main():
    season_2026 = drivers(2026, 'Canada', 'Q')
    rus_qualy_fastest = season_2026.fastest_q_lap('RUS')
    qualy_comparison = season_2026.laps_comparison(('RUS', 'VER', 'HAM'))
    df = pd.DataFrame(rus_qualy_fastest)
    df_comparison = pd.DataFrame(qualy_comparison)
    print(season_2026.all_drivers())
    print(rus_qualy_fastest)
    print(df)
    print(df_comparison)
    # session = fastf1.get_session(2026, 'Canada', 'Q')
    # session.load()
    # laps = session.laps
    # verstappen_laps = laps.pick_driver('VER')
    # fastest_lap = verstappen_laps.pick_fastest()
    # df = pd.DataFrame(fastest_lap)
    # print(f"Total laps: {len(laps)}")
    # print(f"Verstappen fastest lap: {df}")
    # print(f"type: {type(fastest_lap)}")
    # df.to_excel('ver_fastes_lap(Monaco-2024).xlsx', index=False)
    

if __name__ == "__main__":
    main()
