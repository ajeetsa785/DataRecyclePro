[app]

# (str) Title of your application
title = Data Recycle

# (str) Package name
package.name = datarecycle

# (str) Package domain (needed for android packaging)
package.domain = rtv.network

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 1.0.0

# (list) Application requirements
# MUST include requests and its helpers for the Telegram bot to work
requirements = python3, kivy==2.3.0, requests, urllib3, charset-normalizer, idna

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) Permissions
# WAKE_LOCK keeps the "Selling" status active in the background
android.permissions = INTERNET, FOREGROUND_SERVICE, WAKE_LOCK, RECEIVE_BOOT_COMPLETED

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (list) The Android architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) indicates if the application should be fullscreen or not
fullscreen = 0

# (str) Android entry point, default is ok
android.entrypoint = org.kivy.android.PythonActivity

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
