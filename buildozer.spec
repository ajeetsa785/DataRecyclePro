[app]
title = Data Recycle
package.name = datarecycle
package.domain = rtv.network
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0

# These requirements allow the App to talk to Telegram and Infatica
requirements = python3, kivy==2.3.0, requests, urllib3, charset-normalizer, idna

orientation = portrait

# Critical permissions for data selling to stay active in background
android.permissions = INTERNET, FOREGROUND_SERVICE, WAKE_LOCK, RECEIVE_BOOT_COMPLETED

android.api = 31
android.minapi = 21
android.ndk = 25b
android.sdk = 31
android.archs = arm64-v8a, armeabi-v7a
fullscreen = 0
android.entrypoint = org.kivy.android.PythonActivity

[buildozer]
log_level = 2
warn_on_root = 1
