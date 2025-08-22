# Browser Setup Guide for Mini PyFlyff

## 🎯 Browser Targeting Options

Mini PyFlyff now supports multiple browsers and targeting methods. Choose the option that works best for your setup.

### Option 1: Focused Window (Recommended)
**Best for**: Most users, especially those who switch between different applications

- Set "Target Browser" to **"Focused Window"**
- The tool will send keys to whatever window is currently active/focused
- Works with ANY browser or application
- Most flexible and reliable option

**How to use:**
1. Open your game in any browser (Chrome, Opera GX, Firefox, Edge, etc.)
2. Set Mini PyFlyff to "Focused Window"
3. Make sure your game window is focused when the buffers activate
4. Keys will be sent to the active window

### Option 2: Specific Browser Targeting
**Best for**: Users who always use the same browser and want automatic targeting

Supported browsers:
- **Firefox** - Targets Mozilla Firefox windows
- **Chrome** - Targets Google Chrome windows  
- **Opera** / **Opera GX** - Targets Opera browser windows
- **Edge** - Targets Microsoft Edge windows

**How to use:**
1. Select your browser from the "Target Browser" dropdown
2. The tool will automatically find and target that browser
3. No need to keep the window focused

## 🔧 Setup Instructions

### For Opera GX Users:
1. Open Opera GX with your game
2. In Mini PyFlyff, set "Target Browser" to either:
   - **"Focused Window"** (recommended) - Just keep Opera GX focused
   - **"Opera GX"** - Automatic targeting

### For Chrome Users:
1. Open Chrome with your game
2. In Mini PyFlyff, set "Target Browser" to either:
   - **"Focused Window"** (recommended) - Just keep Chrome focused
   - **"Chrome"** - Automatic targeting

### For Firefox Users:
1. Open Firefox with your game
2. In Mini PyFlyff, set "Target Browser" to either:
   - **"Focused Window"** (recommended) - Just keep Firefox focused
   - **"Firefox"** - Automatic targeting

## 🚀 Quick Start

1. **Launch Mini PyFlyff**
2. **Select Target Browser** at the top of the window
3. **Configure your buffers** (GT and/or LA)
4. **Test the setup** by activating a buffer briefly

## 🛠️ Troubleshooting

### Keys not being sent?
1. **Check browser selection** - Make sure the right option is selected
2. **Verify window focus** - If using "Focused Window", ensure your game is active
3. **Test with notepad** - Try "Focused Window" with a text editor to verify key sending works
4. **Check browser windows** - Make sure your target browser is actually open

### Multiple browser windows?
- The tool targets the first window it finds for specific browser targeting
- Use "Focused Window" for more precise control

### Browser not in the list?
- Use "Focused Window" - it works with any application
- The tool will send keys to whatever window is currently active

## 💡 Pro Tips

1. **Use "Focused Window"** for maximum compatibility
2. **Keep your game window active** when buffers are running
3. **Test your setup** before long gaming sessions
4. **Save your configuration** after setting up browser targeting
5. **Use the panic button** (Menu → Panic!) if something goes wrong

## 🔄 Migration from Old Version

If you were using the old Firefox-only version:
1. Your existing configurations will still work
2. Browser targeting defaults to "Focused Window" for better compatibility
3. You can now use any browser instead of just Firefox
4. No need to change your existing hotkey setups

## ⚠️ Important Notes

- **Browser targeting setting is saved** with your configuration
- **"Focused Window" is the most reliable** option for most users
- **Specific browser targeting** requires that browser to be open
- **Keys are sent using Windows API** - works with any Windows application
