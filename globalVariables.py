# Application state variables
macro_loop_on = False
macro_loop_enable_disabled = False
buffer_enable_disabled = False
alt_controller_on = False

# Keyboard shortcuts
macro_loop_shortcut = None
buffer_shortcut = None

# Hotkey lists and configurations
alt_controller_hotkey_list = []
macro_loop_hotkeys = []
macro_loop_hotkey_delay = []
macro_loop_random_delay = 0

# Buffer configuration
buffer_hotkeys = []
buffs_hotbar = None
previous_hotbar = None
buffer_delay = None

# Buffer state
buffer_is_on = False
buffer_is_going = False

# GT Buffer configuration and state
gt_buffer = False
gt_buffer_hotkey = None
gt_buffer_delay = None

# LA Buffer configuration and state
la_buffer = False
la_buffer_hotkey = None
la_buffer_delay = None

# Browser targeting configuration
debug_mode = False

# Simplified browser targeting - only 2 settings needed
la_target_browser = "Focused Window"      # LA Buffer target
main_target_browser = "Focused Window"    # All other features (GT, Alt Controller, Macro Loop, Buffer)
