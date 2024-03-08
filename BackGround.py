import time
import os
import ctypes
def chng_backgorund(new_background_path):
    # Change wallpaper according to commands used in the system
    if os.name == 'posix':
        # For Linux
        os.system("gsettings set org.gnome.desktop.background picture-uri file://" + new_background_path)
    elif os.name == 'nt':
        # For Windows
        ctypes.windll.user32.SytsemParametersInfoW(20,0,new_background_path,0)
    else:
        print("Error: Not supported to change the background.")

def main():
    target_hour_chng = 16  # The time to change Background
    target_hour_rst = 6    # The time you go back to the old Background
    new_backgorund_path = "/path/to/your/new/wallpaper.jpg"
    old_background_path = "/path/to/your/old/wallpaper.jpg"
    while True:
        currentTime = time.localtime
        # Time control
        if currentTime.tm_hour >= target_hour_chng:
            chng_backgorund(new_background_path)
            # Wait to revert back to the old Background at a certain time
            while currentTime.tm_hour < target_hour_rst:
                time.sleep(120)
                currentTime = time.localtime()
                # Back to the old Background
            chng_backgorund(old_background_path)
            break
        else:
            # Wait 60 seconds to check it every 2 minutes
            time.sleep(120)
if __name__ == "__main__":
    main()    
