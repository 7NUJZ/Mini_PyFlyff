#!/usr/bin/env python3
"""
Test script to verify GUI components are properly created
"""

import tkinter as tk
from tkinter import ttk
import sys
import os

def test_gui_components():
    """Test that all GUI components can be created"""
    try:
        # Import the main module
        import MiniPyFlyff
        
        print("✓ MiniPyFlyff module imported successfully")
        
        # Check if LA components exist
        if hasattr(MiniPyFlyff, 'entry_LA_hotkey'):
            print("✓ LA hotkey entry exists")
        else:
            print("✗ LA hotkey entry missing")
            
        if hasattr(MiniPyFlyff, 'entry_LA_delay'):
            print("✓ LA delay entry exists")
        else:
            print("✗ LA delay entry missing")
            
        if hasattr(MiniPyFlyff, 'checkbutton_la'):
            print("✓ LA checkbox exists")
        else:
            print("✗ LA checkbox missing")
            
        if hasattr(MiniPyFlyff, 'la_checkbox_var'):
            print("✓ LA checkbox variable exists")
        else:
            print("✗ LA checkbox variable missing")
            
        print("\nGUI component test completed!")
        
    except ImportError as e:
        print(f"✗ Import error: {e}")
    except Exception as e:
        print(f"✗ Error: {e}")

def create_minimal_test_window():
    """Create a minimal test window to verify layout"""
    root = tk.Tk()
    root.title("Mini PyFlyff Layout Test")
    root.geometry("300x600")
    
    # GT Section
    gt_frame = tk.LabelFrame(root, text="GT Buffer")
    gt_frame.pack(fill=tk.X, padx=5, pady=5)
    
    gt_controls = tk.Frame(gt_frame)
    gt_controls.pack(fill=tk.X, padx=5, pady=5)
    
    tk.Checkbutton(gt_controls, text="Activate GT").pack(side=tk.LEFT)
    tk.Label(gt_controls, text="GT Key:").pack(side=tk.LEFT)
    tk.Entry(gt_controls, width=4).pack(side=tk.LEFT)
    tk.Label(gt_controls, text="GT Delay:").pack(side=tk.LEFT)
    tk.Entry(gt_controls, width=5).pack(side=tk.LEFT)
    
    # LA Section
    la_frame = tk.LabelFrame(root, text="LA Buffer")
    la_frame.pack(fill=tk.X, padx=5, pady=5)
    
    la_controls = tk.Frame(la_frame)
    la_controls.pack(fill=tk.X, padx=5, pady=5)
    
    tk.Checkbutton(la_controls, text="Activate LA").pack(side=tk.LEFT)
    tk.Label(la_controls, text="LA Key:").pack(side=tk.LEFT)
    tk.Entry(la_controls, width=4).pack(side=tk.LEFT)
    tk.Label(la_controls, text="LA Delay:").pack(side=tk.LEFT)
    tk.Entry(la_controls, width=5).pack(side=tk.LEFT)
    
    tk.Label(root, text="Layout Test - Both GT and LA should be visible", 
             fg="blue", font=("Arial", 10, "bold")).pack(pady=10)
    
    tk.Button(root, text="Close", command=root.destroy).pack(pady=10)
    
    print("Test window created. Both GT and LA sections should be visible.")
    root.mainloop()

if __name__ == "__main__":
    print("Testing Mini PyFlyff GUI Components...")
    print("=" * 50)
    
    # Test 1: Component existence
    test_gui_components()
    
    print("\n" + "=" * 50)
    print("Creating layout test window...")
    
    # Test 2: Layout test
    create_minimal_test_window()
