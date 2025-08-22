#!/usr/bin/env python3
"""
Test script to demonstrate separate browser targeting for different features
"""

import globalVariables
import windowsAPI
import time

def test_separate_browser_targeting():
    """Test that different features can target different browsers"""
    print("Testing Separate Browser Targeting")
    print("=" * 60)
    
    # Enable debug mode to see which windows are being targeted
    globalVariables.debug_mode = True
    
    # Set up different browser targets for each feature
    test_configs = [
        {
            "name": "Configuration 1: All Different Browsers",
            "settings": {
                "la_target_browser": "Opera GX",
                "gt_target_browser": "Chrome", 
                "alt_target_browser": "Firefox",
                "macro_target_browser": "Edge",
                "buffer_target_browser": "Focused Window"
            }
        },
        {
            "name": "Configuration 2: LA to Opera GX, Rest to Focused Window",
            "settings": {
                "la_target_browser": "Opera GX",
                "gt_target_browser": "Focused Window",
                "alt_target_browser": "Focused Window", 
                "macro_target_browser": "Focused Window",
                "buffer_target_browser": "Focused Window"
            }
        }
    ]
    
    for config in test_configs:
        print(f"\n{config['name']}")
        print("-" * len(config['name']))
        
        # Apply settings
        for setting, value in config['settings'].items():
            setattr(globalVariables, setting, value)
            print(f"  {setting}: {value}")
        
        print("\nTesting key sending for each feature:")
        
        # Test LA Buffer
        print("  LA Buffer -> ", end="")
        try:
            window = windowsAPI.get_target_window("la_buffer")
            if window:
                import win32gui
                title = win32gui.GetWindowText(window)
                print(f"✓ {title}")
            else:
                print("✗ No window found")
        except Exception as e:
            print(f"✗ Error: {e}")
        
        # Test GT Buffer
        print("  GT Buffer -> ", end="")
        try:
            window = windowsAPI.get_target_window("gt_buffer")
            if window:
                import win32gui
                title = win32gui.GetWindowText(window)
                print(f"✓ {title}")
            else:
                print("✗ No window found")
        except Exception as e:
            print(f"✗ Error: {e}")
        
        # Test Alt Controller
        print("  Alt Controller -> ", end="")
        try:
            window = windowsAPI.get_target_window("alt_controller")
            if window:
                import win32gui
                title = win32gui.GetWindowText(window)
                print(f"✓ {title}")
            else:
                print("✗ No window found")
        except Exception as e:
            print(f"✗ Error: {e}")
        
        # Test Macro Loop
        print("  Macro Loop -> ", end="")
        try:
            window = windowsAPI.get_target_window("macro_loop")
            if window:
                import win32gui
                title = win32gui.GetWindowText(window)
                print(f"✓ {title}")
            else:
                print("✗ No window found")
        except Exception as e:
            print(f"✗ Error: {e}")
        
        # Test Buffer
        print("  Buffer -> ", end="")
        try:
            window = windowsAPI.get_target_window("buffer")
            if window:
                import win32gui
                title = win32gui.GetWindowText(window)
                print(f"✓ {title}")
            else:
                print("✗ No window found")
        except Exception as e:
            print(f"✗ Error: {e}")

def demonstrate_usage():
    """Show how to use the separate browser targeting"""
    print("\n" + "=" * 60)
    print("HOW TO USE SEPARATE BROWSER TARGETING")
    print("=" * 60)
    
    print("""
1. OPEN MINI PYFLYFF
   - You'll see a 'Browser Targeting' section at the top

2. SET UP YOUR BROWSERS
   - Default: General fallback browser
   - LA: Browser for LA Buffer specifically  
   - GT: Browser for GT Buffer specifically

3. EXAMPLE SETUP FOR MULTI-BOXING:
   - LA: Opera GX (your main character)
   - GT: Chrome (your alt character)
   - Default: Focused Window (for other features)

4. CONFIGURE YOUR BUFFERS:
   - Set LA hotkey and delay
   - Set GT hotkey and delay
   - Enable the buffers you want

5. SAVE YOUR CONFIGURATION:
   - Menu → Save Config
   - All browser settings will be saved

6. USAGE:
   - LA Buffer will send keys to Opera GX
   - GT Buffer will send keys to Chrome
   - Other features use the Default setting
   
7. BENEFITS:
   - Control multiple characters simultaneously
   - Each buffer targets a different browser/character
   - Perfect for multi-boxing setups
   - No need to switch windows manually
    """)

if __name__ == "__main__":
    test_separate_browser_targeting()
    demonstrate_usage()
