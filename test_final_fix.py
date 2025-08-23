#!/usr/bin/env python3
"""
Test script to verify the final fixes for LA hotkey and delay fields
"""

import tkinter as tk
import saveConfigs
import miscs

def test_config_data():
    """Test the config data structure"""
    print("Testing Config Data Structure")
    print("=" * 40)
    
    config_data = saveConfigs.open_json_config()
    print(f"Config length: {len(config_data)}")
    print(f"Full config: {config_data}")
    print()
    
    # Test specific indices
    indices_to_test = [
        (10, "GT Hotkey"),
        (11, "GT Delay"), 
        (12, "LA Hotkey"),
        (13, "LA Delay"),
        (14, "LA Browser"),
        (15, "Main Browser")
    ]
    
    for index, name in indices_to_test:
        if index < len(config_data):
            value = config_data[index]
            print(f"Index {index:2d} ({name:12s}): '{value}' (type: {type(value).__name__})")
        else:
            print(f"Index {index:2d} ({name:12s}): NOT FOUND")

def test_validation():
    """Test the validation functions"""
    print("\n" + "=" * 40)
    print("Testing Validation Functions")
    print("=" * 40)
    
    # Test buffer key validation
    test_chars = ['a', 'A', '1', '', ' ', ',', '.']
    print("Buffer Key Validation:")
    for char in test_chars:
        result = miscs.validate_input_buffer_key(char)
        print(f"  '{char}' -> {result}")
    
    print("\nBuffer Timer Validation:")
    for char in test_chars:
        result = miscs.validate_input_buffer_timer(char)
        print(f"  '{char}' -> {result}")

def create_test_window():
    """Create a test window to verify the fields work correctly"""
    root = tk.Tk()
    root.title("LA Fields Test")
    root.geometry("400x300")
    
    # Create validation functions
    validation_buffer_key = root.register(miscs.validate_input_buffer_key)
    validation_buffer_delays = root.register(miscs.validate_input_buffer_timer)
    
    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)
    
    # LA Hotkey field
    tk.Label(frame, text="LA Hotkey:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
    la_hotkey_entry = tk.Entry(frame, width=10, validate="key", validatecommand=(validation_buffer_key, "%S"))
    la_hotkey_entry.grid(row=0, column=1, padx=5, pady=5)
    
    # LA Delay field  
    tk.Label(frame, text="LA Delay:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
    la_delay_entry = tk.Entry(frame, width=10, validate="key", validatecommand=(validation_buffer_delays, "%S"))
    la_delay_entry.grid(row=1, column=1, padx=5, pady=5)
    
    # Load config data
    config_data = saveConfigs.open_json_config()
    if len(config_data) > 12:
        la_hotkey_entry.insert(tk.END, config_data[12])  # LA_hotkey
    if len(config_data) > 13:
        la_delay_entry.insert(tk.END, config_data[13])   # LA_delay
    
    # Test buttons
    def check_values():
        hotkey = la_hotkey_entry.get()
        delay = la_delay_entry.get()
        print(f"LA Hotkey: '{hotkey}'")
        print(f"LA Delay: '{delay}'")
    
    def clear_fields():
        la_hotkey_entry.delete(0, tk.END)
        la_delay_entry.delete(0, tk.END)
        print("Fields cleared")
    
    tk.Button(frame, text="Check Values", command=check_values).grid(row=2, column=0, pady=10)
    tk.Button(frame, text="Clear Fields", command=clear_fields).grid(row=2, column=1, pady=10)
    
    # Instructions
    instructions = tk.Label(root, text="Test Instructions:\n1. Try typing in both fields\n2. Try deleting text (backspace/delete)\n3. Check if validation works correctly", 
                           justify="left", bg="lightyellow")
    instructions.pack(pady=10, padx=10, fill="x")
    
    root.mainloop()

if __name__ == "__main__":
    test_config_data()
    test_validation()
    print("\n" + "=" * 40)
    print("Creating test window...")
    print("Test typing and deletion in both fields")
    create_test_window()
