# Separate Browser Targeting Guide

## 🎯 Overview

Mini PyFlyff now supports **separate browser targeting** for different features! This means you can:

- **LA Buffer** → Send keys to Opera GX
- **GT Buffer** → Send keys to Chrome  
- **Alt Controller** → Send keys to Firefox
- **Macro Loop** → Send keys to Edge
- **Buffer** → Send keys to any browser

Perfect for **multi-boxing** setups where you want to control multiple characters in different browsers simultaneously!

## 🚀 Quick Setup Example

### Scenario: Control Two Characters
- **Main Character** in Opera GX (LA Buffer)
- **Alt Character** in Chrome (GT Buffer)

### Setup Steps:
1. Open Mini PyFlyff
2. In the "Browser Targeting" section:
   - **LA**: Select "Opera GX"
   - **GT**: Select "Chrome"
   - **Default**: Select "Focused Window"
3. Configure your buffers:
   - **LA Buffer**: Set hotkey (e.g., "f") and delay (e.g., "45")
   - **GT Buffer**: Set hotkey (e.g., "g") and delay (e.g., "30")
4. Save configuration: Menu → Save Config

### Result:
- LA Buffer will automatically send "f" key to Opera GX every 45 seconds
- GT Buffer will automatically send "g" key to Chrome every 30 seconds
- Both run independently and simultaneously!

## 🎮 Browser Targeting Options

### Available Browsers:
- **Focused Window** - Sends to currently active window
- **Firefox** - Targets Mozilla Firefox
- **Chrome** - Targets Google Chrome
- **Opera** - Targets Opera browser
- **Opera GX** - Targets Opera GX
- **Edge** - Targets Microsoft Edge

### Feature-Specific Targeting:

| Feature | Description | Use Case |
|---------|-------------|----------|
| **LA** | LA Buffer targeting | Main character buffs |
| **GT** | GT Buffer targeting | Alt character buffs |
| **Default** | Fallback for other features | General purpose |

## 📋 Complete Setup Guide

### Step 1: Open Multiple Browsers
```
1. Open Opera GX with your main character
2. Open Chrome with your alt character
3. (Optional) Open Firefox for other purposes
```

### Step 2: Configure Browser Targeting
```
1. Launch Mini PyFlyff
2. In "Browser Targeting" section:
   - Default: Focused Window
   - LA: Opera GX
   - GT: Chrome
```

### Step 3: Configure Buffers
```
LA Buffer:
- Check "Activate LA"
- LA Key: f (or your preferred hotkey)
- LA Delay: 45 (seconds between casts)

GT Buffer:
- Check "Activate GT"  
- GT Key: g (or your preferred hotkey)
- GT Delay: 30 (seconds between casts)
```

### Step 4: Save and Test
```
1. Menu → Save Config
2. Test by enabling one buffer at a time
3. Verify keys are sent to correct browsers
```

## 🔧 Advanced Configurations

### Configuration 1: Full Multi-Boxing
```
- LA: Opera GX (Main character)
- GT: Chrome (Alt character 1)
- Default: Firefox (Alt character 2)
- Alt Controller: Edge (Alt character 3)
```

### Configuration 2: Single Browser with Focused Window
```
- LA: Focused Window
- GT: Focused Window
- Default: Focused Window
(Switch focus between characters manually)
```

### Configuration 3: Mixed Setup
```
- LA: Opera GX (Dedicated main)
- GT: Focused Window (Manual control)
- Default: Chrome (Other features)
```

## 🛠️ Troubleshooting

### Keys not going to the right browser?
1. **Check browser selection** - Verify correct browser is selected
2. **Verify browser is open** - Target browser must be running
3. **Test with debug mode** - Enable debug in test scripts
4. **Use "Focused Window"** - Most reliable fallback option

### Multiple windows of same browser?
- Tool targets the first window found
- Use "Focused Window" for precise control
- Close extra browser windows if needed

### Browser not in the list?
- Use "Focused Window" option
- Works with any application, not just browsers
- Most flexible option available

## 💡 Pro Tips

### For Multi-Boxing:
1. **Use different browsers** for each character
2. **Set different delays** to avoid conflicts
3. **Test one buffer at a time** initially
4. **Save configurations** for different setups

### For Single Character:
1. **Use "Focused Window"** for maximum flexibility
2. **Keep game window active** when buffers run
3. **Use specific browser targeting** for automation

### For Stability:
1. **Start with "Focused Window"** to test
2. **Enable debug mode** for troubleshooting
3. **Use panic button** if something goes wrong
4. **Save working configurations** as backups

## 🎯 Example Use Cases

### Case 1: Dual Boxing
- **Main**: Opera GX with LA Buffer (healing)
- **Alt**: Chrome with GT Buffer (support buffs)

### Case 2: Triple Boxing  
- **Main**: Opera GX with LA Buffer
- **Alt 1**: Chrome with GT Buffer
- **Alt 2**: Firefox with Alt Controller

### Case 3: Flexible Setup
- **All features**: "Focused Window"
- **Manual switching** between characters
- **Maximum compatibility**

## 🔄 Migration from Single Browser

If you were using the old single-browser system:
1. **Existing configs will work** - Default targeting preserved
2. **New features available** - Can now set specific targeting
3. **Gradual migration** - Change one feature at a time
4. **Fallback support** - "Focused Window" always works

---

**Remember**: Save your configuration after setting up browser targeting. All settings are preserved between sessions!
