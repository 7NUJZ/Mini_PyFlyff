#!/usr/bin/env python3
"""
Simple build script for Mini PyFlyff
Handles permission issues and provides clear instructions
"""

import os
import sys
import subprocess
import shutil
import time
from pathlib import Path

def check_and_install_pyinstaller():
    """Check if PyInstaller is installed, install if needed"""
    try:
        import PyInstaller
        print("✓ PyInstaller is available")
        return True
    except ImportError:
        print("Installing PyInstaller...")
        try:
            subprocess.run([sys.executable, '-m', 'pip', 'install', 'pyinstaller'], check=True)
            print("✓ PyInstaller installed successfully")
            return True
        except subprocess.CalledProcessError:
            print("✗ Failed to install PyInstaller")
            return False

def kill_existing_processes():
    """Try to kill any existing MiniPyFlyff processes"""
    try:
        # Try to kill any running instances
        result = subprocess.run(['taskkill', '/F', '/IM', 'MiniPyFlyff.exe'], 
                               capture_output=True, text=True)
        if result.returncode == 0:
            print("✓ Closed existing MiniPyFlyff processes")
            time.sleep(2)  # Wait for processes to fully close
        return True
    except Exception:
        return False

def clean_directories():
    """Clean build directories with better error handling"""
    print("Cleaning build directories...")
    
    dirs_to_clean = ['build', 'dist', '__pycache__']
    
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            try:
                shutil.rmtree(dir_name)
                print(f"✓ Removed {dir_name}")
            except PermissionError:
                print(f"⚠️  Could not remove {dir_name} (permission denied)")
                print(f"   Please manually delete the '{dir_name}' folder and try again")
                return False
            except Exception as e:
                print(f"⚠️  Error removing {dir_name}: {e}")
    
    # Remove .spec files
    for spec_file in Path('.').glob('*.spec'):
        try:
            spec_file.unlink()
            print(f"✓ Removed {spec_file}")
        except Exception as e:
            print(f"⚠️  Could not remove {spec_file}: {e}")
    
    return True

def build_executable():
    """Build the executable"""
    print("Building executable...")
    
    cmd = [
        'pyinstaller',
        '--onefile',
        '--windowed',
        '--name=MiniPyFlyff',
        '--clean',
        'MiniPyFlyff.py'
    ]
    
    # Add icon if it exists
    if os.path.exists('icon/PyFlyff.ico'):
        cmd.extend(['--icon=icon/PyFlyff.ico'])
        cmd.extend(['--add-data=icon;icon'])
    
    try:
        print("Running PyInstaller...")
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("✓ Build completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Build failed!")
        print(f"Error: {e.stderr}")
        return False

def verify_executable():
    """Verify the executable was created"""
    exe_path = Path('dist/MiniPyFlyff.exe')
    if exe_path.exists():
        size_mb = exe_path.stat().st_size / (1024 * 1024)
        print(f"✓ Executable created: {exe_path}")
        print(f"✓ File size: {size_mb:.1f} MB")
        return True
    else:
        print("✗ Executable not found!")
        return False

def create_simple_release():
    """Create a simple release without complex directory operations"""
    print("Creating release files...")
    
    exe_path = Path('dist/MiniPyFlyff.exe')
    if not exe_path.exists():
        print("✗ Executable not found in dist folder")
        return False
    
    # Create a simple batch file next to the executable
    batch_content = """@echo off
echo Starting Mini PyFlyff...
echo.
echo If you see this window, the application is running.
echo You can minimize this window.
echo.
MiniPyFlyff.exe
echo.
echo Mini PyFlyff has closed.
pause
"""
    
    try:
        with open('dist/run.bat', 'w') as f:
            f.write(batch_content)
        print("✓ Created run.bat in dist folder")
        
        # Copy important files to dist
        files_to_copy = ['README.md', 'SEPARATE_BROWSER_GUIDE.md', 'BROWSER_SETUP_GUIDE.md']
        for file_name in files_to_copy:
            if os.path.exists(file_name):
                try:
                    shutil.copy(file_name, 'dist/')
                    print(f"✓ Copied {file_name} to dist")
                except Exception as e:
                    print(f"⚠️  Could not copy {file_name}: {e}")
        
        print("\n" + "=" * 50)
        print("BUILD COMPLETED!")
        print("=" * 50)
        print("Your files are ready in the 'dist' folder:")
        print("  • MiniPyFlyff.exe - The main application")
        print("  • run.bat - Double-click to run the application")
        print("  • Documentation files")
        print("\nYou can distribute the entire 'dist' folder.")
        
        return True
        
    except Exception as e:
        print(f"✗ Error creating release files: {e}")
        return False

def main():
    """Main build process"""
    print("=" * 60)
    print("Mini PyFlyff Simple Build Script")
    print("=" * 60)
    
    # Step 1: Check PyInstaller
    if not check_and_install_pyinstaller():
        return False
    
    print("\n" + "-" * 40)
    
    # Step 2: Kill existing processes
    kill_existing_processes()
    
    # Step 3: Clean directories
    if not clean_directories():
        print("\nPlease close any running applications and delete build folders manually.")
        print("Then run this script again.")
        return False
    
    print("\n" + "-" * 40)
    
    # Step 4: Build executable
    if not build_executable():
        return False
    
    print("\n" + "-" * 40)
    
    # Step 5: Verify build
    if not verify_executable():
        return False
    
    print("\n" + "-" * 40)
    
    # Step 6: Create release
    if not create_simple_release():
        print("Build succeeded but release creation failed.")
        print("You can find your executable in the 'dist' folder.")
        return False
    
    return True

if __name__ == "__main__":
    try:
        success = main()
        if not success:
            print("\n❌ Build failed!")
            sys.exit(1)
        else:
            print("\n✅ Build completed successfully!")
    except KeyboardInterrupt:
        print("\n\n⚠️  Build cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)
