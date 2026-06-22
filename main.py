import random
import time
import pygame

pygame.mixer.init()

class Driver:
    def __init__(self, name, team, skill, audio_file):
        # 1. Passed-in arguments
        self.name = name
        self.team = team
        self._skill = skill # (internal) skill level from 0 to 10
        self.audio_file = audio_file
        # 2. Starting state (Not passed in, but initialized)
        self.total_time = 0.0

    
    def calc_lap_time(self):
        # It uses 'self._skill', so it MUST be a regular instance method!
        # let's assume base time as 80 seconds
        base_time = 90
        random_variation = random.uniform(-20,20)
        return (base_time - self._skill + random_variation)

class Race:
    def __init__(self, drivers, laps):
        self.drivers = drivers
        self.laps = laps

    def run(self):
        for lap in range(self.laps):
            for driver in self.drivers:
                lap_time = driver.calc_lap_time()
                driver.total_time += lap_time

    def leaderboard(self):
        sorted_drivers = sorted(self.drivers, key=lambda driver: driver.total_time)
        # lambda is an anonymous function that takes a driver 'd' and returns 'd.total_time' for sorting
        print("------------------------------")
        print("   🏆 FINAL LEADERBOARD 🏆   ")
        print("------------------------------")
        for position, driver in enumerate(sorted_drivers, start=1):
            print(f"{position}. {driver.name} - Total Time: {round(driver.total_time, 2)} seconds")
        print("------------------------------")
        winner = sorted_drivers[0]
        print(f"\n🏆 WINNER: {winner.name} from {winner.team}! 🏆")
        print("[System] Initializing audio subsystem...")
        print(f"[System] Playing winner's audio: {winner.audio_file}")
        pygame.mixer.music.load(winner.audio_file)
        pygame.mixer.music.play()
    
        while pygame.mixer.music.get_busy():
            time.sleep(0.5)



d1 = Driver("Carlos Sainz", "Williams Racing", 6, "carlos.mp3")
d2 = Driver("Max Verstappen", "Red Bull", 9, "DUDUDUDU MAXX VERSTA--_audio_file.mp3")
d3 = Driver("Charles Leclerc", "Ferrari", 7, "leclerc.mp3")
d4 = Driver("George Russell", "Mercedes", 7.5, "george.mp3")
all_drivers = [d1, d2, d3, d4]

#Sample Grand Prix Simulation
monaco_gp = Race(all_drivers, laps=65)
monaco_gp.run()
monaco_gp.leaderboard()