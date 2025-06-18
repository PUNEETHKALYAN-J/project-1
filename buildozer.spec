[app]

# (str) Title of your application
title = MyKivyApp

# (str) Package name
package.name = mykivyapp

# (str) Package domain (unique identifier)
package.domain = org.example

# (str) Source code where your main.py is located
source.dir = .

# (str) Application entry point
source.main = main.py

# (str) The main .kv file to use (optional if it's named my.kv automatically)
# kv.filename = my.kv

# (list) Permissions your app needs
android.permissions = INTERNET

# (str) Supported orientation (portrait, landscape or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (bool) Hide the statusbar
android.hide_statusbar = 0

# (str) Supported Android API
android.api = 33

# (str) Minimum Android API your app will support
android.minapi = 21

# (str) Android NDK version
android.ndk = 25b

# (str) Android SDK version to use
android.sdk = 33

# (bool) Use --private data storage (deprecated)
android.private_storage = True

# (str) Application icon
# icon.filename = %(source.dir)s/icon.png

# (str) Supported platforms
android.archs = armeabi-v7a, arm64-v8a

# (list) Application requirements
requirements = python3,kivy==2.3.0,cython==0.29.36



# (str) Presplash image
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Version number
version = 0.1

# (str) Python version to use (3, 3.7, 3.8, etc.)
python.version = 3

# (bool) Copy the .apk to the current directory
copy_to_current = 1

# (bool) Enable logcat debugging
log_level = 2

[buildozer]

# (str) Path to build output
build_dir = ./.buildozer

# (bool) Enable verbose output
verbose = 1
