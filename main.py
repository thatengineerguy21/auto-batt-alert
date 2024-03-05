import psutil
from ctypes import Structure, windll, c_uint, sizeof, byref
from time import sleep

class LASTINPUTINFO(Structure):
    _fields_ = [("cbSize", c_uint), ("dwTime", c_uint)]

def get_idle_duration():
    lii = LASTINPUTINFO()
    lii.cbSize = sizeof(LASTINPUTINFO)
    windll.user32.GetLastInputInfo(byref(lii))
    millis = windll.kernel32.GetTickCount() - lii.dwTime
    return millis / 1000.0

def show_notification(title, message):
    windll.user32.MessageBoxW(0, message, title, 1)

def check_battery_level():
    battery = psutil.sensors_battery()
    percent = battery.percent

    if percent <= 20 or percent >= 80:
        show_notification("Battery Alert", f"Battery level is {percent}%.")

if __name__ == "__main__":
    while True:
        check_battery_level()
        # Check every 2 minutes
        sleep(120)