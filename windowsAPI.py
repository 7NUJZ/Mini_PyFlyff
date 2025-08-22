import win32gui
import win32api
import win32con
import time
import virtualKeys
import globalVariables

# Browser window class mappings
BROWSER_CLASSES = {
    "Firefox": "MozillaWindowClass",
    "Chrome": "Chrome_WidgetWin_1",
    "Opera": "Chrome_WidgetWin_1",  # Opera GX uses Chrome engine
    "Opera GX": "Chrome_WidgetWin_1",
    "Edge": "Chrome_WidgetWin_1",  # New Edge uses Chrome engine
    "Focused Window": None  # Special case for focused window
}


def get_target_window(feature_type="default"):
    """Get the target window handle based on browser selection for specific feature"""
    try:
        # Get browser choice based on feature type
        if feature_type == "la_buffer":
            browser_choice = getattr(globalVariables, 'la_target_browser', 'Focused Window')
        elif feature_type == "gt_buffer":
            browser_choice = getattr(globalVariables, 'gt_target_browser', 'Focused Window')
        elif feature_type == "alt_controller":
            browser_choice = getattr(globalVariables, 'alt_target_browser', 'Focused Window')
        elif feature_type == "macro_loop":
            browser_choice = getattr(globalVariables, 'macro_target_browser', 'Focused Window')
        elif feature_type == "buffer":
            browser_choice = getattr(globalVariables, 'buffer_target_browser', 'Focused Window')
        else:
            # Default/fallback to main browser setting
            browser_choice = getattr(globalVariables, 'target_browser', 'Focused Window')

        if browser_choice == "Focused Window":
            # Get the currently focused window
            window = win32gui.GetForegroundWindow()
            if window and win32gui.IsWindow(window):
                return window
        else:
            # Find specific browser window
            window_class = BROWSER_CLASSES.get(browser_choice)
            if window_class:
                window = win32gui.FindWindow(window_class, None)
                if window:
                    return window

        # Fallback: try to find any browser window
        for browser, class_name in BROWSER_CLASSES.items():
            if class_name:  # Skip "Focused Window"
                window = win32gui.FindWindow(class_name, None)
                if window:
                    if hasattr(globalVariables, 'debug_mode') and globalVariables.debug_mode:
                        print(f"Found {browser} window as fallback for {feature_type}")
                    return window

        # Last resort: use focused window
        return win32gui.GetForegroundWindow()

    except Exception as e:
        print(f"Error getting target window for {feature_type}: {e}")
        # Return focused window as ultimate fallback
        return win32gui.GetForegroundWindow()


def windows_api(key, feature_type="default"):
    """Send key to target window for specific feature"""
    try:
        window = get_target_window(feature_type)

        if not window or not win32gui.IsWindow(window):
            print(f"No valid target window found for {feature_type}")
            return

        # Get window title for debugging
        try:
            window_title = win32gui.GetWindowText(window)
            if hasattr(globalVariables, 'debug_mode') and globalVariables.debug_mode:
                print(f"Sending key '{key}' to window: {window_title} (feature: {feature_type})")
        except:
            pass

        # Get virtual key code
        vk_code = virtualKeys.vk_code.get(key)
        if not vk_code:
            print(f"Unknown key: {key}")
            return

        # Send key down
        win32api.SendMessage(window, win32con.WM_KEYDOWN, vk_code, 0)
        time.sleep(0.1)

        # Send key up
        win32api.SendMessage(window, win32con.WM_KEYUP, vk_code, 0)

    except Exception as e:
        print(f"Error sending key '{key}' for {feature_type}: {e}")
