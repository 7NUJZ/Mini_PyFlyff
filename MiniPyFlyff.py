from tkinter import Button, Label, Entry, X, LEFT, RIGHT, LabelFrame, Frame, Checkbutton, IntVar, Menu, END, Tk, Toplevel

import globalVariables
import keyboardListener
import os
import saveConfigs
import toolControl
import miscs
import panicButton


def panic():
    try:
        button_buffer_disable_enable["text"] = "Enable"
        button_alt_controller_enable_disable["text"] = "Enable"
        button_macro_loop_enable_disable["text"] = "Enable"
        gt_checkbox_var.set(False)
        la_checkbox_var.set(False)
        panicButton.set_all_to_false()
        print("Panic button activated - all processes stopped")
    except Exception as e:
        print(f"Error in panic function: {e}")


def load_config():
    try:
        config_data = saveConfigs.open_json_config()

        # Clear existing entries first
        for entry in [entry_alt_controller_hotkeys, entry_macro_loop_hotkey, entry_macro_loop_delays,
                     entry_macro_loop_shortcut, entry_buffer_hotkeys, entry_buffs_hotbar,
                     entry_previous_hotbar, entry_buffer_delay, entry_buffer_shortcut,
                     entry_GT_hotkey, entry_GT_delay, entry_LA_hotkey, entry_LA_delay]:
            entry.delete(0, END)

        # Load configuration data
        entry_alt_controller_hotkeys.insert(END, config_data[0])
        entry_macro_loop_hotkey.insert(END, config_data[1])
        entry_macro_loop_delays.insert(END, config_data[2])
        entry_macro_loop_shortcut.insert(END, config_data[3])
        entry_buffer_hotkeys.insert(END, config_data[5])
        entry_buffs_hotbar.insert(END, config_data[6])
        entry_previous_hotbar.insert(END, config_data[7])
        entry_buffer_delay.insert(END, config_data[8])
        entry_buffer_shortcut.insert(END, config_data[9])
        entry_GT_hotkey.insert(END, config_data[10])
        entry_GT_delay.insert(END, config_data[11])
        entry_LA_hotkey.insert(END, config_data[12])
        entry_LA_delay.insert(END, config_data[13])
    except Exception as e:
        print(f"Error loading config: {e}")
        # Continue with empty fields if config loading fails

    random_delay_checkbox_var.set(int(saveConfigs.open_json_config()[4]))

    globalVariables.macro_loop_random_delay = int(saveConfigs.open_json_config()[4])

    miscs.multithreading(keyboardListener.listener)

    entry_alt_controller_hotkeys.config(validate="key")
    entry_alt_controller_hotkeys.config(validatecommand=(validation_keys, "%S"))

    entry_macro_loop_hotkey.config(validate="key")
    entry_macro_loop_hotkey.config(validatecommand=(validation_keys, "%S"))

    entry_macro_loop_delays.config(validate="key")
    entry_macro_loop_delays.config(validatecommand=(validation_delays, "%S"))

    entry_buffer_hotkeys.config(validate="key")
    entry_buffer_hotkeys.config(validatecommand=(validation_keys, "%S"))

    entry_buffs_hotbar.config(validate="key")
    entry_buffs_hotbar.config(validatecommand=(validation_buffer_key, "%S"))

    entry_previous_hotbar.config(validate="key")
    entry_previous_hotbar.config(validatecommand=(validation_buffer_key, "%S"))

    entry_buffer_delay.config(validate="key")
    entry_buffer_delay.config(validatecommand=(validation_buffer_delays, "%S"))

    entry_GT_hotkey.config(validate="key")
    entry_GT_hotkey.config(validatecommand=(validation_buffer_key, "%S"))

    entry_GT_delay.config(validate="key")
    entry_GT_delay.config(validatecommand=(validation_buffer_delays, "%S"))

    entry_LA_hotkey.config(validate="key")
    entry_LA_hotkey.config(validatecommand=(validation_buffer_key, "%S"))

    entry_LA_delay.config(validate="key")
    entry_LA_delay.config(validatecommand=(validation_buffer_delays, "%S"))


def save_data():
    data = (entry_alt_controller_hotkeys.get(),
            entry_macro_loop_hotkey.get(),
            entry_macro_loop_delays.get(),
            entry_macro_loop_shortcut.get(),
            random_delay_checkbox_var.get(),
            toolControl.start_stop_macro_loop,
            entry_buffer_hotkeys.get(),
            entry_buffs_hotbar.get(),
            entry_previous_hotbar.get(),
            entry_buffer_delay.get(),
            entry_buffer_shortcut.get(),
            toolControl.start_stop_buffer,
            entry_GT_hotkey.get(),
            entry_GT_delay.get(),
            entry_LA_hotkey.get(),
            entry_LA_delay.get())

    return data


def gt_checkbutton_state():
    toolControl.gt_checkbutton_state(gt_checkbox_var)


def la_checkbutton_state():
    toolControl.la_checkbutton_state(la_checkbox_var)


def random_delay_checkbutton_state():
    if random_delay_checkbox_var.get() == 1:
        globalVariables.macro_loop_random_delay = 1
    else:
        globalVariables.macro_loop_random_delay = 0


def create_tooltip(widget, text):
    def on_enter(event):
        try:
            # Destroy any existing tooltip
            if hasattr(widget, 'tooltip') and widget.tooltip:
                widget.tooltip.destroy()

            tooltip = Toplevel()
            tooltip.wm_overrideredirect(True)
            tooltip.wm_attributes('-topmost', True)

            # Calculate position to keep tooltip on screen
            x = event.x_root + 10
            y = event.y_root + 10

            # Get screen dimensions
            screen_width = tooltip.winfo_screenwidth()
            screen_height = tooltip.winfo_screenheight()

            # Adjust position if tooltip would go off screen
            if x + 200 > screen_width:
                x = event.x_root - 210
            if y + 50 > screen_height:
                y = event.y_root - 60

            tooltip.wm_geometry(f"+{x}+{y}")

            label = Label(tooltip, text=text, background="lightyellow",
                         relief="solid", borderwidth=1, font=("Arial", 8),
                         wraplength=200, justify="left")
            label.pack()
            widget.tooltip = tooltip
        except Exception:
            # Silently handle any tooltip creation errors
            pass

    def on_leave(event):
        try:
            if hasattr(widget, 'tooltip') and widget.tooltip:
                widget.tooltip.destroy()
                widget.tooltip = None
        except Exception:
            # Silently handle any tooltip destruction errors
            pass

    widget.bind("<Enter>", on_enter)
    widget.bind("<Leave>", on_leave)


root = Tk()

menu_bar = Menu(root)

menu = Menu(menu_bar, tearoff=0)

menu.add_command(label="Save Config", command=lambda: saveConfigs.save_key_configs(save_data()))
menu.add_command(label="Panic!", command=panic)

menu_bar.add_cascade(label="Menu", menu=menu)

root.config(menu=menu_bar)

window_width = 262
window_height = 520

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)

root.geometry(str(window_width) + "x" + str(window_height) + "+" + str(int(x)) + "+" + str(int(y)))
root.title("Mini PyFlyff")
if os.path.isfile("icon/PyFlyff.ico"):
    root.iconbitmap("icon/PyFlyff.ico")
root.resizable(False, False)

validation_delays = root.register(miscs.validate_input_timers)
validation_keys = root.register(miscs.validate_input_keys)

validation_buffer_delays = root.register(miscs.validate_input_buffer_timer)
validation_buffer_key = root.register(miscs.validate_input_buffer_key)

random_delay_checkbox_var = IntVar()
gt_checkbox_var = IntVar()
la_checkbox_var = IntVar()

label_frame_1 = LabelFrame(root)
label_frame_1.pack(fill=X, padx=2, pady=2)

label_alt_controller = Label(label_frame_1, text="Alt Controller Hotkey(s):")
label_alt_controller.pack(fill=X, padx=1, pady=1)
create_tooltip(label_alt_controller, "Hotkey(s) to control your Alt Client (separate each hotkey(s) with commas).")

entry_alt_controller_hotkeys = Entry(label_frame_1, validate="none")
entry_alt_controller_hotkeys.pack(fill=X, padx=1, pady=1)
create_tooltip(entry_alt_controller_hotkeys,
               "Hotkey(s) to control your Alt Client (separate each hotkey(s) with commas).")

frame_alt_controller_button = Frame(label_frame_1)
frame_alt_controller_button.pack(fill=X, padx=1, pady=1)

button_alt_controller_enable_disable = Button(frame_alt_controller_button, text="Enable", width=10)
button_alt_controller_enable_disable.pack(side=RIGHT, padx=1, pady=1)
button_alt_controller_enable_disable.config(
    command=lambda: toolControl.enable_disable_alt_control(button_alt_controller_enable_disable))
create_tooltip(button_alt_controller_enable_disable, "Button to Disable/Enable Alt Controller.")

label_frame_2 = LabelFrame(root)
label_frame_2.pack(fill=X, padx=2, pady=2)

label_macro_loop = Label(label_frame_2, text="Macro Loop Key(s):")
label_macro_loop.pack(fill=X, padx=1, pady=1)
create_tooltip(label_macro_loop, "Hotkey(s) for the Macro Loop (separate each hotkey(s) with commas).")

entry_macro_loop_hotkey = Entry(label_frame_2, validate="none")
entry_macro_loop_hotkey.pack(fill=X, padx=1, pady=1)
create_tooltip(entry_macro_loop_hotkey, "Hotkey(s) for the Macro Loop (separate each hotkey(s) with commas).")

label_macro_loop_delays = Label(label_frame_2, text="Macro Loop Delay(s):")
label_macro_loop_delays.pack(fill=X, padx=1, pady=1)
create_tooltip(label_macro_loop_delays,
               "Delay(s) for each hotkey for the Macro Loop (separate each delay(s) with commas).")

entry_macro_loop_delays = Entry(label_frame_2, validate="none")
entry_macro_loop_delays.pack(fill=X, padx=1, pady=1)
create_tooltip(entry_macro_loop_delays,
               "Delay(s) for each hotkey for the Macro Loop (separate each delay(s) with commas).")

label_macro_loop_shortcut = Label(label_frame_2, text="Macro Loop Shortcut:")
label_macro_loop_shortcut.pack(fill=X, padx=1, pady=1)
create_tooltip(label_macro_loop_shortcut, "Shortcut to Start/Stop the Macro Loop.")

entry_macro_loop_shortcut = Entry(label_frame_2, validate="none")
entry_macro_loop_shortcut.pack(fill=X, padx=1, pady=1)
create_tooltip(entry_macro_loop_shortcut, "Shortcut to Start/Stop the Macro Loop.")

frame_macro_loop_checkbutton = Frame(label_frame_2)
frame_macro_loop_checkbutton.pack(fill=X, padx=1, pady=1)

checkbutton_macro_loop = Checkbutton(frame_macro_loop_checkbutton, text="Random Delays",
                                     variable=random_delay_checkbox_var, command=random_delay_checkbutton_state)
checkbutton_macro_loop.pack(side=LEFT, padx=1, pady=1)
create_tooltip(checkbutton_macro_loop, "Create random delay(s) for each Macro Loop hotkey(s) interaction.")

frame_macro_loop_buttons = Frame(label_frame_2)
frame_macro_loop_buttons.pack(fill=X, padx=1, pady=1)

button_macro_loop_enable_disable = Button(frame_macro_loop_buttons, text="Enable", width=10)
button_macro_loop_enable_disable.pack(side=RIGHT, padx=1, pady=1)
button_macro_loop_enable_disable.config(
    command=lambda: toolControl.enable_disable_macro_loop(button_macro_loop_enable_disable))
create_tooltip(button_macro_loop_enable_disable, "Enable/Disable the Macro Loop.")

label_frame_3 = LabelFrame(root)
label_frame_3.pack(fill=X, padx=2, pady=2)

label_buffer_hotkeys = Label(label_frame_3, text="Buffer Hotkey(s):")
label_buffer_hotkeys.pack(fill=X, padx=1, pady=1)
create_tooltip(label_buffer_hotkeys, "Hotkey(s) for each buff used (separate each hotkey(s) with commas).")

entry_buffer_hotkeys = Entry(label_frame_3, validate="none")
entry_buffer_hotkeys.pack(fill=X, padx=1, pady=1)
create_tooltip(entry_buffer_hotkeys, "Hotkey(s) for each buff used (separate each hotkey(s) with commas).")

frame_buffer_1 = Frame(label_frame_3)
frame_buffer_1.pack(fill=X, padx=1, pady=1)

label_buffs_hotbar = Label(frame_buffer_1, text="Hotbar:")
label_buffs_hotbar.pack(side=LEFT, padx=1, pady=1)
create_tooltip(label_buffs_hotbar, "The hotkey to change to the buff's hotbar.")

entry_buffs_hotbar = Entry(frame_buffer_1, width=5, validate="none")
entry_buffs_hotbar.pack(side=LEFT, padx=1, pady=1)
create_tooltip(entry_buffs_hotbar, "The hotkey to change to the buff's hotbar.")

label_preview_hotbar = Label(frame_buffer_1, text="Previous:")
label_preview_hotbar.pack(side=LEFT, padx=1, pady=1)
create_tooltip(label_preview_hotbar, "The hotkey to go back to the previous hotbar.")

entry_previous_hotbar = Entry(frame_buffer_1, width=5, validate="none")
entry_previous_hotbar.pack(side=LEFT, padx=1, pady=1)
create_tooltip(entry_previous_hotbar, "The hotkey to go back to the previous hotbar.")

label_buffer_delay = Label(frame_buffer_1, text="Delay:")
label_buffer_delay.pack(side=LEFT, padx=1, pady=1)
create_tooltip(label_buffer_delay, "Delay to cast each buff.")

entry_buffer_delay = Entry(frame_buffer_1, width=6, validate="none")
entry_buffer_delay.pack(side=LEFT, padx=1, pady=1)
create_tooltip(entry_buffer_delay, "Delay to cast each buff.")

label_buffer_shortcut = Label(label_frame_3, text="Buffer Shortcut:")
label_buffer_shortcut.pack(padx=1, pady=1)
create_tooltip(label_buffer_shortcut, "Shortcut to activate the Buffer.")

entry_buffer_shortcut = Entry(label_frame_3, validate="none")
entry_buffer_shortcut.pack(fill=X, padx=1, pady=1)
create_tooltip(entry_buffer_shortcut, "Shortcut to activate the Buffer.")

frame_buffer_4 = Frame(label_frame_3)
frame_buffer_4.pack(fill=X, padx=1, pady=1)

button_buffer_disable_enable = Button(frame_buffer_4, text="Enable", width=10)
button_buffer_disable_enable.pack(side=RIGHT, padx=1, pady=1)
button_buffer_disable_enable.config(command=lambda: toolControl.enable_disable_buffer(button_buffer_disable_enable))
create_tooltip(button_buffer_disable_enable, "Enable/Disable the Buffer")

label_frame_4 = LabelFrame(root)
label_frame_4.pack(fill=X, padx=2, pady=2)

frame_buffer_2 = Frame(label_frame_4)
frame_buffer_2.pack(fill=X, padx=1, pady=1)

checkbutton_gt = Checkbutton(frame_buffer_2, text="Activate GT", variable=gt_checkbox_var, command=gt_checkbutton_state)
checkbutton_gt.pack(side=LEFT, padx=1, pady=1)
create_tooltip(checkbutton_gt, "Mark this box to initiate the GT Buffer.")

label_GT_hotkey = Label(frame_buffer_2, text="GT Key:")
label_GT_hotkey.pack(side=LEFT, padx=1, pady=1)
create_tooltip(label_GT_hotkey, "Hotkey to use GT")

entry_GT_hotkey = Entry(frame_buffer_2, width=4, validate="none")
entry_GT_hotkey.pack(side=LEFT, padx=1, pady=1)
create_tooltip(entry_GT_hotkey, "Hotkey to use GT")

label_GT_delay = Label(frame_buffer_2, text="GT Delay:")
label_GT_delay.pack(side=LEFT, padx=1, pady=1)
create_tooltip(label_GT_delay, "Delay to use GT")

entry_GT_delay = Entry(frame_buffer_2, width=5, validate="none")
entry_GT_delay.pack(side=LEFT, padx=1, pady=1)
create_tooltip(entry_GT_delay, "Delay to use GT")

# LA Buffer section - in the same frame as GT
frame_buffer_5 = Frame(label_frame_4)
frame_buffer_5.pack(fill=X, padx=1, pady=1)

checkbutton_la = Checkbutton(frame_buffer_5, text="Activate LA", variable=la_checkbox_var, command=la_checkbutton_state)
checkbutton_la.pack(side=LEFT, padx=1, pady=1)
create_tooltip(checkbutton_la, "Mark this box to initiate the LA Buffer.")

label_LA_hotkey = Label(frame_buffer_5, text="LA Key:")
label_LA_hotkey.pack(side=LEFT, padx=1, pady=1)
create_tooltip(label_LA_hotkey, "Hotkey to use LA")

entry_LA_hotkey = Entry(frame_buffer_5, width=4, validate="none")
entry_LA_hotkey.pack(side=LEFT, padx=1, pady=1)
create_tooltip(entry_LA_hotkey, "Hotkey to use LA")

label_LA_delay = Label(frame_buffer_5, text="LA Delay:")
label_LA_delay.pack(side=LEFT, padx=1, pady=1)
create_tooltip(label_LA_delay, "Delay to use LA")

entry_LA_delay = Entry(frame_buffer_5, width=5, validate="none")
entry_LA_delay.pack(side=LEFT, padx=1, pady=1)
create_tooltip(entry_LA_delay, "Delay to use LA")

def main():
    """Main application entry point with error handling"""
    try:
        load_config()
        print("Mini PyFlyff started successfully")
        root.mainloop()
    except Exception as e:
        print(f"Critical error in main application: {e}")
        import traceback
        traceback.print_exc()
    finally:
        # Cleanup on exit
        try:
            panicButton.set_all_to_false()
        except:
            pass

if __name__ == "__main__":
    main()
