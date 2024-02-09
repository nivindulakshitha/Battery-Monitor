import psutil, os
from plyer import notification
from time import sleep

current_dir = os.path.dirname(os.path.abspath(__file__))

def notify_fully_charged():
    notification.notify(
        title='Battery Fully Charged',
        message='Your battery is fully charged. Please unplug the charger.',
        app_name='Battery Monitor',
        timeout=10,
        toast=True
    )

def notify_plug_charger():
    notification.notify(
        title='Please Plug the Charger',
        message='Your battery is running low. Please plug in the charger.',
        app_name='Battery Monitor',
        timeout=10,
        toast=True
    )


def check_battery_status():
    battery = psutil.sensors_battery()
    if battery:
        plugged = battery.power_plugged
        percent = battery.percent
        
        if not plugged and percent == 52:
            notify_fully_charged()

        elif not plugged and percent <= 7:
            notify_plug_charger()


if __name__ == "__main__":
    while True:
        check_battery_status()
        sleep(60)
