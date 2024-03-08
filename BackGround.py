import time
import os
import ctypes
def chng_backgorund(new_background_path):
    if os.name == 'posix':
        os.system("gsettings set org.gnome.desktop.background picture-uri file://" + new_background_path)
    elif os.name == 'nt':
        ctypes.windll.user32.SytsemParametersInfoW(20,0,new_background_path,0)
    else:
        print("Error")

def main():
    target_hour_chng = 16
    target_hour_rst = 6
    new_backgorund_path = "/path/to/your/new/wallpaper.jpg"
    old_background_path = "/path/to/your/old/wallpaper.jpg"
    while True:
        currentTime = time.localtime
        if currentTime.tm_hour >= target_hour_chng:
            chng_backgorund(new_background_path)
            while currentTime.tm_hour < target_hour_rst:
                time.sleep(120)
                currentTime = time.localtime()
            chng_backgorund(old_background_path)
            break
        else:
            time.sleep(120)
if __name__ == "__main__":
    main()    