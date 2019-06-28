import time
import datetime as dt
import tkinter
from tkinter import messagebox
from tkinter import simpledialog
import winsound
# hide main window
root = tkinter.Tk()
root.withdraw()

total_pomodoros = 0

## Main script here:
# Collect time information
current_time = dt.datetime.now()                       # Current time for reference
pomodoro_time = 25*60                                   # Pomodoro time                 
t_delta = dt.timedelta(0,pomodoro_time)                 # Time delta in mins            
future_time = current_time + t_delta                         # Future time for reference     
delta_sec = 1#60                                  # Break time, after pomodoro  
t_fin = current_time + dt.timedelta(0,pomodoro_time+delta_sec) # Final time (w/ 5 mins break)  


print(f"Bug check 0: \nt_now: {current_time}\nt_fut: {future_time}")

# GUI set pomodoro in motion!
messagebox.showinfo("Pomodoro Started!", "\nIt is now "+current_time.strftime("%H:%M") +
" hrs. \nTimer set for 25 mins.")

# Main script
while True:
    # Pomodoro time! Code for adding and maintaining the websites to be blocked!
    if current_time < future_time:
        print('First Period')
    ## Commented out. Uncomment to add a break of 5 mins into the comodoro!
    ## it is now past working pomodoro, within the break. Delete the websites
    elif future_time <= current_time <= t_fin:
        # allow for browsing again. Remove websites from hosts file
        print('Break time!')
    #Pomodoro and break finished. Check if ready for another pomodoro!
    else:
        print('Third current_time > future_time - Finished')
        # Ring a bell (with print('\a') to alert of end of program.
        print('\a')
        # Annoy!
        for i in range(10):
            winsound.Beep((i+100), 500)
        usr_ans = messagebox.askyesno("Pomodoro Finished!","Would you like to start another pomodoro?")
        #usr_ans = input("Timer has finished. \nWould you like to start another pomodoro? \nY/N:  ")
        total_pomodoros += 1
        if usr_ans == True:
            # user wants another pomodoro! Update values to indicate new timeset.
            current_time = dt.datetime.now()
            future_time = current_time + dt.timedelta(0,pomodoro_time)
            t_fin = current_time + dt.timedelta(0,pomodoro_time+delta_sec)
            continue
        elif usr_ans == False:
            print(f'Pomodoro timer complete! \nYou have completed {total_pomodoros} pomodoros today.')
            # unlock the websites
            # Show a final message)
            messagebox.showinfo("Pomodoro Finished!",
            "\nYou completed "+str(total_pomodoros)+" pomodoros today!")
            break
    # check every 3 seconds and update current time
    time.sleep(20)
    current_time = dt.datetime.now()
    timenow = current_time.strftime("%H:%M")

print('\n\nMade it to the end!\n\n')
