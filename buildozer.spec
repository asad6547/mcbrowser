[app]
title = MC Browser
package.name = mcbrowser
package.domain = org.mcbrowser
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.2.1,kivymd==1.1.1,pyjnius
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,ACCESS_NETWORK_STATE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_licenses = True

[buildozer]
log_level = 2
warn_on_root = 1
