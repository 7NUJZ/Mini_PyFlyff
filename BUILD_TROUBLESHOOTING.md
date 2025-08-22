# Build Troubleshooting Guide

## 🚨 Common Build Issues and Solutions

### Issue 1: Permission Error (Access Denied)
```
PermissionError: [WinError 5] Access is denied: 'release\MiniPyFlyff.exe'
```

**Cause**: The executable is still running or being used by another process.

**Solutions**:
1. **Close all instances** of MiniPyFlyff.exe
2. **Check Task Manager** for any running MiniPyFlyff processes
3. **Delete the 'release' folder** manually
4. **Use the simple build script**: `python simple_build.py`

### Issue 2: PyInstaller Not Found
```
ModuleNotFoundError: No module named 'PyInstaller'
```

**Solution**:
```bash
pip install pyinstaller
```

### Issue 3: Build Fails with Import Errors
**Solution**: Install missing dependencies
```bash
pip install keyboard pywin32
```

## 🛠️ Build Methods

### Method 1: Simple Build (Recommended)
```bash
python simple_build.py
```
- Handles permission issues automatically
- Creates files in 'dist' folder
- Most reliable method

### Method 2: Original Build Script
```bash
python build.py
```
- More features but can have permission issues
- Creates 'release' folder

### Method 3: Manual PyInstaller
```bash
# Basic build
pyinstaller --onefile --windowed MiniPyFlyff.py

# With icon (if available)
pyinstaller --onefile --windowed --icon=icon/PyFlyff.ico MiniPyFlyff.py
```

## 🔧 Step-by-Step Troubleshooting

### Step 1: Clean Environment
```bash
# Close all MiniPyFlyff instances
# Delete these folders if they exist:
# - build/
# - dist/
# - release/
# - __pycache__/
```

### Step 2: Check Dependencies
```bash
python -c "import keyboard; import win32gui; import tkinter; print('All dependencies OK')"
```

### Step 3: Test Application
```bash
python MiniPyFlyff.py
```
Make sure the application runs before building.

### Step 4: Build with Simple Script
```bash
python simple_build.py
```

## 📁 Output Locations

### Simple Build Script:
- **Location**: `dist/` folder
- **Files**: 
  - `MiniPyFlyff.exe` - Main executable
  - `run.bat` - Launcher script
  - Documentation files

### Original Build Script:
- **Location**: `release/` folder  
- **Files**:
  - `MiniPyFlyff.exe` - Main executable
  - `run.bat` - Launcher script
  - `icon/` folder
  - Documentation files

## 🚀 Quick Fix Commands

### Kill Running Processes:
```cmd
taskkill /F /IM MiniPyFlyff.exe
```

### Clean Build Directories:
```cmd
rmdir /s /q build
rmdir /s /q dist
rmdir /s /q release
rmdir /s /q __pycache__
```

### Install All Dependencies:
```bash
pip install keyboard pywin32 pyinstaller
```

## ⚠️ Known Issues

### Windows Defender/Antivirus
- May flag the executable as suspicious
- **Solution**: Add exception for the build folder
- This is normal for PyInstaller executables

### Large File Size
- Executable may be 20-50 MB
- **Cause**: PyInstaller bundles Python interpreter
- **Normal behavior**: This is expected

### Slow Startup
- First run may be slower
- **Cause**: Windows scanning the new executable
- **Normal behavior**: Subsequent runs will be faster

## 💡 Pro Tips

### For Development:
1. **Use simple_build.py** for regular builds
2. **Test before building** - run `python MiniPyFlyff.py` first
3. **Close applications** before building
4. **Keep backups** of working builds

### For Distribution:
1. **Test the executable** on a clean system
2. **Include documentation** files
3. **Provide the run.bat** for easier launching
4. **Zip the entire folder** for distribution

### For Troubleshooting:
1. **Check the console output** for specific errors
2. **Try building in a new folder** if issues persist
3. **Use virtual environment** to isolate dependencies
4. **Update PyInstaller** if builds fail: `pip install --upgrade pyinstaller`

## 🆘 If All Else Fails

1. **Create a new folder**
2. **Copy only the Python files** (not build folders)
3. **Install fresh dependencies**:
   ```bash
   pip install keyboard pywin32 pyinstaller
   ```
4. **Run simple build**:
   ```bash
   python simple_build.py
   ```

## 📞 Getting Help

If you're still having issues:
1. **Check the error message** carefully
2. **Try the simple build script** first
3. **Ensure all dependencies** are installed
4. **Test the Python script** runs correctly before building

Remember: The executable in the `dist` folder is all you need to run the application!
