import threading
from time import sleep
from tkinter import Tk, Frame, StringVar, OptionMenu, Label, Entry, END
from ArkLib import conv_str_to_time, seconds_to_time, time_to_seconds, display_time, get_total_maturation_str, \
    all_dino_names


# one_tenth_decrease_time_for_food_in_seconds = 10
# get_food = float(input("How much food he got? "))
# food_left_in_seconds = get_food * one_tenth_decrease_time_for_food_in_seconds


# This is the main function for the entire system
def calc_dino_mat():
    try:
        # Sleep is how often the func is ran
        sleep(.2)

        # Get the active dino from the option box
        active_dino = var.get()

        # Get the servers maturation speed
        mat_multiplier = float(mat_speed_entry.get()) / 2

        # Get the current amount of maturation percentage
        current_mat = float(current_mat_ent.get())

        # Get the string of the dinos maturation time
        dino_mat_time_str = get_total_maturation_str(active_dino)

        # Convert the time string into a list of time [D, H, M]
        time_list = conv_str_to_time(dino_mat_time_str)

        # Convert the time list into total seconds
        time_in_sec = time_to_seconds(time_list)

        # Divide the time in seconds by the servers maturation multiplier
        time_in_sec_mult = int(time_in_sec / mat_multiplier)

        # Convert the dividend of seconds back into a time list
        time_after_mult = seconds_to_time(time_in_sec_mult)

        # Get the text of the TOTAL time until mature
        show_total_time_until_mature = display_time(active_dino, time_after_mult, "mature from 0%")

        # Show the text of the TOTAL time until mature
        display_txt_total.configure(text=show_total_time_until_mature)

        # Get the time it takes in seconds for 0.1% maturation
        one_tenth_mat_time_in_sec = time_in_sec_mult / 1000

        # Determine the time LEFT in seconds until maturation after the current maturation percentage
        maturation_left_in_seconds = int(((100 - current_mat) * 10) * (one_tenth_mat_time_in_sec))

        # Convert the time LEFT from seconds to a list
        time_left_after_mult = seconds_to_time(maturation_left_in_seconds)

        # Get the time LEFT until mature in a str
        show_mat_left_time = display_time(active_dino, time_left_after_mult, f"mature from {current_mat}%")

        # Display the time LEFT on the GUI
        display_txt_left.configure(text=show_mat_left_time)

        calc_dino_mat()

    except ZeroDivisionError:
        print("Zero Division Error")
        # If a 0 div error, set the mult to 1.0 to avoid freezing
        calc_dino_mat.mat_multiplier = 1.0
        calc_dino_mat()

    except ValueError:
        print("Value Error")
        # If a value error, set the mult to 1.0 to avoid freezing
        calc_dino_mat.mat_multiplier = 1.0
        calc_dino_mat()

    except RuntimeError:
        print("Run time error")
        quit()


def close_and_clean():
    # Closes the GUI and quits the application when called
    quit()


def only_num_input(input):
    try:
        input = float(input)
    except ValueError:
        pass
    if isinstance(input, float) or input.isdigit() or input == "":
        return True
    return False


# This is the padding for x and y around the grid squares
g_pad = 5

# GUI is the overall window holder
gui = Tk()
gui.title("Lil Tryke")
gui.geometry("500x250")
gui.iconbitmap('img/icon.ico')

# Register tk to python callback
callback = gui.register(only_num_input)

# Main frame is the holder of all other frames in the GUI
main_frame = Frame(gui,
                   padx=5,
                   pady=5)

main_frame.place(anchor="center",
                 relx=0.5,
                 rely=0.5)

# var is the active option chosen in the option menu
var = StringVar(gui)
var.set(all_dino_names[0])

# dino_choice is the holder of all the dino names
# all_dino_names is a separate list from the dino dictionary
dino_choice = OptionMenu(main_frame, var, *all_dino_names)

dino_choice.configure(font=("System", 12),
                      padx=17,
                      pady=9)

dino_choice.grid(row=5,
                 column=5,
                 padx=g_pad,
                 pady=g_pad)


# The maturation speed label and entry is the area to enter the servers rate of maturation
mat_speed_label = Label(main_frame,
                        text='Maturation Speed',
                        relief='groove',
                        padx=5,
                        pady=9,
                        font=("System", 12))

mat_speed_label.grid(row=5,
                     column=10,
                     padx=g_pad,
                     pady=g_pad)

mat_speed_entry = Entry(main_frame,
                        relief='groove',
                        width=4,
                        font=("System", 20))

mat_speed_entry.grid(row=5,
                     column=15,
                     padx=g_pad,
                     pady=g_pad)

mat_speed_entry.delete(0, END)
mat_speed_entry.insert(0, 2)
# Apply input checks to ensure float
mat_speed_entry.configure(validate="key", validatecommand=(callback, "%P"))


# Current maturation is the dino's active maturation %
current_mat_lbl = Label(main_frame,
                        text='Current Maturation',
                        relief='groove',
                        padx=5,
                        pady=9,
                        font=("System", 12))

current_mat_lbl.grid(row=10,
                     column=5,
                     padx=g_pad,
                     pady=g_pad)

current_mat_ent = Entry(main_frame,
                        relief='groove',
                        width=4,
                        font=("System", 20))

current_mat_ent.grid(row=10,
                     column=9,
                     padx=g_pad,
                     pady=g_pad)


current_mat_ent.delete(0, END)
current_mat_ent.insert(0, 0)
# Apply input checks to ensure float
current_mat_ent.configure(validate="key", validatecommand=(callback, "%P"))


# Current maturation is the dino's active maturation %
current_food_lbl = Label(main_frame,
                         text='Current Hunger',
                         relief='groove',
                         padx=14,
                         pady=9,
                         font=("System", 12))

current_food_lbl.grid(row=10,
                      column=10,
                      padx=g_pad,
                      pady=g_pad)

current_food_ent = Entry(main_frame,
                         relief='groove',
                         width=6,
                         font=("System", 20))

current_food_ent.grid(row=10,
                      column=15,
                      padx=g_pad,
                      pady=g_pad)


current_food_ent.delete(0, END)
current_food_ent.insert(0, 0)
# Apply input checks to ensure float
current_food_ent.configure(validate="key", validatecommand=(callback, "%P"))


# Display labels are the text shown to display the maturation times
display_txt_total = Label(main_frame,
                          text=f"NAME takes DHM to fully grow from 0%",
                          font=("System", 12))

display_txt_total.grid(row=15,
                       column=5,
                       columnspan=20,
                       padx=g_pad,
                       pady=g_pad)

display_txt_left = Label(main_frame,
                         text=f"NAME still has DHM to fully grow from NUM%",
                         font=("System", 12))

display_txt_left.grid(row=20,
                      column=5,
                      columnspan=20,
                      padx=g_pad,
                      pady=g_pad)


# Display labels are the text shown to display the food left until starvation times
display_starve_time = Label(main_frame,
                            text=f"NAME has DHM until they begin to starve.",
                            font=("System", 12))

display_starve_time.grid(row=25,
                         column=5,
                         columnspan=20,
                         padx=g_pad,
                         pady=g_pad)


if __name__ == '__main__':
    # Call close & clean if the x is clicked
    gui.protocol('WM_DELETE_WINDOW', close_and_clean)

    # Start the thread to check the input
    run_calc = threading.Thread(target=calc_dino_mat)
    run_calc.start()

    gui.mainloop()
