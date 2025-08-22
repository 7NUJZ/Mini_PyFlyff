#!/usr/bin/env python3
"""
Test script to verify browser targeting functionality
"""

import time
import globalVariables
import windowsAPI

def test_browser_targeting():
    """Test browser targeting with different browsers"""
    print("Testing Browser Targeting Functionality")
    print("=" * 50)
    
    # Test different browser targets
    browsers_to_test = [
        "Focused Window",
        "Chrome", 
        "Firefox",
        "Opera GX",
        "Edge"
    ]
    
    for browser in browsers_to_test:
        print(f"\nTesting: {browser}")
        globalVariables.target_browser = browser
        
        try:
            # Get target window
            window = windowsAPI.get_target_window()
            if window:
                import win32gui
                try:
                    window_title = win32gui.GetWindowText(window)
                    print(f"✓ Found window: {window_title}")
                except:
                    print(f"✓ Found window (handle: {window})")
            else:
                print("✗ No window found")
        except Exception as e:
            print(f"✗ Error: {e}")
    
    print("\n" + "=" * 50)
    print("Browser targeting test completed!")
    print("\nInstructions:")
    print("1. Open your preferred browser (Chrome, Opera GX, etc.)")
    print("2. Set 'Target Browser' to 'Focused Window' in Mini PyFlyff")
    print("3. Make sure your browser window is focused when using the tool")
    print("4. Or select your specific browser from the dropdown")

def test_key_sending():
    """Test sending a key to the focused window"""
    print("\n" + "=" * 50)
    print("Key Sending Test")
    print("=" * 50)
    
    print("This will send the 'a' key to the focused window in 5 seconds...")
    print("Make sure to focus on a text editor or browser to see the result.")
    
    for i in range(5, 0, -1):
        print(f"Sending key in {i} seconds...")
        time.sleep(1)
    
    try:
        globalVariables.target_browser = "Focused Window"
        windowsAPI.windows_api('a')
        print("✓ Key 'a' sent successfully!")
    except Exception as e:
        print(f"✗ Error sending key: {e}")

if __name__ == "__main__":
    # Enable debug mode for testing
    globalVariables.debug_mode = True
    
    test_browser_targeting()
    
    # Uncomment the line below to test key sending
    # test_key_sending()
