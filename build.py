#!/usr/bin/env python3
"""
Build script for Mini PyFlyff
Creates an executable with all dependencies included
"""

import os
import sys
import subprocess
import shutil
import time
from pathlib import Path

def check_dependencies():
    """Check if all required dependencies are installed"""
    print("Checking dependencies...")
    
    required_packages = ['keyboard', 'pywin32', 'pyinstaller']
    missing_packages = []
    
    for package in required_packages:
        try:
            if package == 'pywin32':
                import win32gui
                import win32api
                import win32con
            elif package == 'keyboard':
                import keyboard
            elif package == 'pyinstaller':
                import PyInstaller
            print(f"✓ {package} is installed")
        except ImportError:
            missing_packages.append(package)
            print(f"✗ {package} is missing")
    
    if missing_packages:
        print(f"\nMissing packages: {', '.join(missing_packages)}")
        print("Installing missing packages...")
        for package in missing_packages:
            subprocess.run([sys.executable, '-m', 'pip', 'install', package])
    
    return len(missing_packages) == 0

def clean_build_dirs():
    """Clean previous build directories"""
    print("Cleaning previous build directories...")
    
    dirs_to_clean = ['build', 'dist', '__pycache__']
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"✓ Removed {dir_name}")
    
    # Remove .spec files
    for spec_file in Path('.').glob('*.spec'):
        spec_file.unlink()
        print(f"✓ Removed {spec_file}")

def build_executable():
    """Build the executable using PyInstaller"""
    print("Building executable...")
    
    # PyInstaller command
    cmd = [
        'pyinstaller',
        '--onefile',                    # Single executable file
        '--windowed',                   # No console window
        '--name=MiniPyFlyff',          # Executable name
        '--add-data=icon;icon',        # Include icon directory
        '--icon=icon/PyFlyff.ico',     # Application icon
        '--clean',                     # Clean cache
        'MiniPyFlyff.py'              # Main script
    ]
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("✓ Build completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Build failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def verify_build():
    """Verify the build was successful"""
    print("Verifying build...")
    
    exe_path = Path('dist/MiniPyFlyff.exe')
    if exe_path.exists():
        size_mb = exe_path.stat().st_size / (1024 * 1024)
        print(f"✓ Executable created: {exe_path}")
        print(f"✓ File size: {size_mb:.1f} MB")
        return True
    else:
        print("✗ Executable not found!")
        return False

def create_release_package():
    """Create a release package with the executable and necessary files"""
    print("Creating release package...")

    release_dir = Path('release')
    if release_dir.exists():
        try:
            # Try to remove the directory
            shutil.rmtree(release_dir)
        except PermissionError:
            print("⚠️  Warning: Could not remove existing release directory.")
            print("   This might be because the executable is still running.")
            print("   Please close any running instances and try again.")

            # Try to kill any running processes
            try:
                import subprocess
                subprocess.run(['taskkill', '/F', '/IM', 'MiniPyFlyff.exe'],
                             capture_output=True, check=False)
                print("   Attempted to close running executable...")
                time.sleep(2)  # Wait a moment
                shutil.rmtree(release_dir)
                print("   ✓ Successfully removed release directory")
            except Exception as e:
                print(f"   Could not automatically fix the issue: {e}")
                print("   Please manually close MiniPyFlyff.exe and delete the 'release' folder")
                return False

    release_dir.mkdir()
    
    # Copy executable
    shutil.copy('dist/MiniPyFlyff.exe', release_dir)
    
    # Copy icon directory
    shutil.copytree('icon', release_dir / 'icon')
    
    # Copy documentation
    files_to_copy = ['README.md', 'LICENSE']
    for file_name in files_to_copy:
        if os.path.exists(file_name):
            shutil.copy(file_name, release_dir)
    
    # Create a simple batch file to run the executable
    batch_content = """@echo off
echo Starting Mini PyFlyff...
MiniPyFlyff.exe
pause
"""
    with open(release_dir / 'run.bat', 'w') as f:
        f.write(batch_content)

    print(f"✓ Release package created in: {release_dir}")
    return True

def main():
    """Main build process"""
    print("=" * 60)
    print("Mini PyFlyff Build Script")
    print("=" * 60)
    
    # Step 1: Check dependencies
    if not check_dependencies():
        print("Please install missing dependencies and try again.")
        return False
    
    print("\n" + "-" * 40)
    
    # Step 2: Clean previous builds
    clean_build_dirs()
    
    print("\n" + "-" * 40)
    
    # Step 3: Build executable
    if not build_executable():
        return False
    
    print("\n" + "-" * 40)
    
    # Step 4: Verify build
    if not verify_build():
        return False
    
    print("\n" + "-" * 40)
    
    # Step 5: Create release package
    if not create_release_package():
        print("\n⚠️  Release package creation failed, but executable is available in 'dist' folder.")
        return False

    print("\n" + "=" * 60)
    print("BUILD COMPLETED SUCCESSFULLY!")
    print("=" * 60)
    print("Your executable is ready in the 'release' directory.")
    print("You can distribute the entire 'release' folder.")

    return True

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1)
