# Mini PyFlyff Download and Information

## 📥 Direct Download Link:

[**Download the Newest Version!**](https://github.com/ils94/Mini_PyFlyff/releases/download/release_v2/MiniPyFlyff.zip)  
_Last binary update: Mar 06, 2025_

---

## 🌟 About Mini PyFlyff

**Mini PyFlyff** is a streamlined version of PyFlyff, built specifically for Mozilla Firefox. It combines classic features with exciting new functionalities to enhance your experience.

---

## 🛠️ Requirements

- **Python 3.7+**: Download from [python.org](https://www.python.org/)
- **Any Modern Browser**: Works with Firefox, Chrome, Opera GX, Edge, and more!
- **Flexible Targeting**: Can send keys to a specific browser or the currently focused window

### Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install keyboard pywin32
```

## 🚀 How to Run

### Option 1: Run from Source

```bash
# Clone or download the project
cd Mini_PyFlyff

# Install dependencies
pip install -r requirements.txt

# Run the application
python MiniPyFlyff.py
```

### Option 2: Build Executable

```bash
# Install build dependencies
pip install pyinstaller

# Run the build script
python build.py

# The executable will be in the 'release' folder
```

---

## 💡 Features (New and Improved!)

### **🎯 Browser Targeting** (NEW!)

Choose your target browser or window:

- **Focused Window**: Sends keys to whatever window is currently active (recommended)
- **Specific Browser**: Target Firefox, Chrome, Opera GX, Edge, or other browsers
- **Flexible Setup**: Perfect for multi-browser setups or different game clients

### **Alt Controller**

The original **"Alt Control"** has evolved into **Alt Controller**!

- Set up hotkeys in Alt Controller to control your alt character with ease. Actions taken on your main character will automatically reflect on your alt, perfect for combining your alt's Heal with your main's AoE!

### **Macro Loop**

The feature formerly known as **"Mini Ftool"** is now **Macro Loop**!

- Set up hotkey sequences to spam with customized delays.
- Toggle "Random Delays" to add an unique touch between each key press for a more natural feel.

### **Buffer**

The beloved **Buffer** feature is now here!

- Set your buff hotkeys and press the hotkey whenever you want to buy your main (the buffer key needs to be pressed manually).
- **Activate the GT Buffer** to have it periodically cast automatically!
- **Activate the LA Buffer** to have it periodically cast automatically! (New Feature)
- Easily toggle the Macro Loop and Buffer via shortcuts, no need to open the tool each time!

✨ **Hover over text fields, buttons, and labels for quick tooltips that explain each feature.**

### Example Configuration

Here’s a valid example setup for Mini PyFlyff:

![Mini PyFlyff Configuration Example](https://github.com/ils94/Mini_PyFlyff/blob/master/example.png?raw=true)

### ❗ **Panic button** ❗

If something goes wrong with the tool (crazy loops, zombie threads, bananas!), go to Menu → Panic! This should set all loops to false, slowly terminate any zombie threads, and everything should return to normal!

---

## ⚠️ Disclaimer

**Note**: Macros and bots are typically prohibited by game developers. Mini PyFlyff enables multi-action key bindings and includes automated features. Please use responsibly:

- Avoid fully AFK gameplay.
- Stay alert to avoid getting caught by a GM and risking a ban. **Use at your own discretion!**

---

## ❗ Not for Sale!

**Mini PyFlyff is entirely free and open-source**, and it always will be! I enjoy creating these Python projects as learning experiences. **If anyone tries to sell this tool, they are scamming you!**
