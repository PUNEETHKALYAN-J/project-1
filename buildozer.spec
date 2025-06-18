[app]

# App name and package info
title = MyKivyApp
package.name = mykivyapp
package.domain = org.example

# Entry point
source.dir = .
source.main = main.py

# KV file (optional, auto-detected if named main.kv)
# kv.filename = main.kv

# Android permissions
android.permissions = INTERNET

# Orientation and fullscreen
orientation = portrait
fullscreen = 1
android.hide_statusbar = 1

# Android platform settings
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.private_storage = True
android.archs = armeabi-v7a, arm64-v8a

# Application dependencies
requirements = python3==3.10.13, kivy==2.3.0, cython==0.29.36

# Blacklist problematic Python 2 files that cause syntax errors during build
android.exclude_patterns = **/lib2to3/tests/*

# Versioning
version = 0.1
python.version = 3

# APK output
copy_to_current = 1

# Log settings
log_level = 2

# Exclude unnecessary test files
android.exclude_patterns = **/lib2to3/tests/**

# Optional icon and presplash (uncomment if needed)
# icon.filename = %(source.dir)s/icon.png
# presplash.filename = %(source.dir)s/data/presplash.png

[buildozer]

# Output build directory
build_dir = ./.buildozer

# Verbose logging
verbose = 1
warn_on_root = 1
