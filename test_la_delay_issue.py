#!/usr/bin/env python3
"""
Test script to check LA Delay entry field issue
"""

import tkinter as tk
from tkinter import ttk
import saveConfigs

def test_la_delay_field():
    """Test what's being loaded into the LA Delay field"""
    print("Testing LA Delay Field Issue")
    print("=" * 40)
    
    # Test config loading
    try:
        config_data = saveConfigs.open_json_config()
        print(f"Config data length: {len(config_data)}")
        print(f"Config data: {config_data}")
        
        if len(config_data) > 13:
            la_delay_value = config_data[13]
            print(f"LA Delay value from config: '{la_delay_value}' (type: {type(la_delay_value)})")
        else:
            print("LA Delay value not found in config")
            
    except Exception as e:
        print(f"Error loading config: {e}")

def create_test_window():
    """Create a test window to check the LA Delay field"""
    root = tk.Tk()
    root.title("LA Delay Test")
    root.geometry("400x200")
    
    # Create LA Delay field similar to main app
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)
    
    label = tk.Label(frame, text="LA Delay:")
    label.pack(side=tk.LEFT, padx=5)
    
    entry = tk.Entry(frame, width=5)
    entry.pack(side=tk.LEFT, padx=5)
    
    # Load config data
    try:
        config_data = saveConfigs.open_json_config()
        if len(config_data) > 13:
            entry.insert(tk.END, config_data[13])
            print(f"Inserted into entry: '{config_data[13]}'")
    except Exception as e:
        print(f"Error: {e}")
    
    # Check what's in the entry
    def check_entry():
        content = entry.get()
        print(f"Entry content: '{content}'")
        
    check_button = tk.Button(root, text="Check Entry Content", command=check_entry)
    check_button.pack(pady=10)
    
    # Clear entry
    def clear_entry():
        entry.delete(0, tk.END)
        print("Entry cleared")
        
    clear_button = tk.Button(root, text="Clear Entry", command=clear_entry)
    clear_button.pack(pady=5)
    
    root.mainloop()

if __name__ == "__main__":
    test_la_delay_field()
    print("\nCreating test window...")
    create_test_window()
