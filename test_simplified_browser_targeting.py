#!/usr/bin/env python3
"""
Test script to verify simplified browser targeting (2 browser selections)
"""

import globalVariables
import windowsAPI

def test_simplified_browser_targeting():
    """Test the simplified 2-browser targeting system"""
    print("Testing Simplified Browser Targeting (2 Selections)")
    print("=" * 60)
    
    # Enable debug mode
    globalVariables.debug_mode = True
    
    # Test Configuration 1: LA to Opera GX, Others to Firefox
    print("\nConfiguration 1: LA → Opera GX, Others → Firefox")
    print("-" * 50)
    
    globalVariables.la_target_browser = "Opera GX"
    globalVariables.main_target_browser = "Firefox"
    
    print(f"LA Target: {globalVariables.la_target_browser}")
    print(f"Main Target: {globalVariables.main_target_browser}")
    
    # Test each feature
    features_to_test = [
        ("la_buffer", "LA Buffer"),
        ("gt_buffer", "GT Buffer"), 
        ("alt_controller", "Alt Controller"),
        ("macro_loop", "Macro Loop"),
        ("buffer", "Buffer")
    ]
    
    for feature_type, feature_name in features_to_test:
        print(f"\n{feature_name} -> ", end="")
        try:
            window = windowsAPI.get_target_window(feature_type)
            if window:
                import win32gui
                title = win32gui.GetWindowText(window)
                print(f"✓ {title}")
            else:
                print("✗ No window found")
        except Exception as e:
            print(f"✗ Error: {e}")
    
    # Test Configuration 2: LA to Focused Window, Others to Chrome
    print("\n" + "=" * 60)
    print("\nConfiguration 2: LA → Focused Window, Others → Chrome")
    print("-" * 50)
    
    globalVariables.la_target_browser = "Focused Window"
    globalVariables.main_target_browser = "Chrome"
    
    print(f"LA Target: {globalVariables.la_target_browser}")
    print(f"Main Target: {globalVariables.main_target_browser}")
    
    for feature_type, feature_name in features_to_test:
        print(f"\n{feature_name} -> ", end="")
        try:
            window = windowsAPI.get_target_window(feature_type)
            if window:
                import win32gui
                title = win32gui.GetWindowText(window)
                print(f"✓ {title}")
            else:
                print("✗ No window found")
        except Exception as e:
            print(f"✗ Error: {e}")

def demonstrate_usage():
    """Show how to use the simplified browser targeting"""
    print("\n" + "=" * 60)
    print("HOW TO USE SIMPLIFIED BROWSER TARGETING")
    print("=" * 60)
    
    print("""
🎯 SIMPLIFIED SETUP - ONLY 2 BROWSER SELECTIONS:

┌─────────────────────────────────────────────────┐
│ Browser Targeting                               │
├─────────────────────────────────────────────────┤
│ LA Buffer: [Opera GX     ▼]                     │ ← Only for LA Buffer
│ Other Features: [Firefox ▼]                     │ ← GT, Alt Controller, Macro, Buffer
└─────────────────────────────────────────────────┘

✅ WHAT THIS MEANS:
• LA Buffer → Sends keys to Opera GX
• GT Buffer → Sends keys to Firefox  
• Alt Controller → Sends keys to Firefox
• Macro Loop → Sends keys to Firefox
• Buffer → Sends keys to Firefox

🎮 PERFECT FOR YOUR SETUP:
1. Set "LA Buffer" to "Focused Window" (for flexibility)
2. Set "Other Features" to "Firefox" (for GT and Alt Controller)
3. Both GT Buffer and Alt Controller will work in Firefox
4. LA Buffer can target any focused window

🔧 EXAMPLE CONFIGURATIONS:

Configuration A - Multi-Boxing:
• LA Buffer: Opera GX (main character)
• Other Features: Chrome (alt character)

Configuration B - Single Browser:
• LA Buffer: Focused Window
• Other Features: Firefox

Configuration C - Your Current Setup:
• LA Buffer: Focused Window  
• Other Features: Firefox (fixes Alt Controller issue!)

💡 WHY THIS FIXES YOUR ALT CONTROLLER:
Before: Alt Controller used "default" browser (confusing)
Now: Alt Controller uses "Other Features" browser (clear!)

🚀 SETUP STEPS:
1. Open Mini PyFlyff
2. Set "Other Features" to "Firefox"
3. Set "LA Buffer" to "Focused Window" or "Opera GX"
4. Configure your hotkeys
5. Save configuration
6. Test Alt Controller - it should work now!
    """)

if __name__ == "__main__":
    test_simplified_browser_targeting()
    demonstrate_usage()
