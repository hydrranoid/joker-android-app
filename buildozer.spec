[app]

# (str) Title of your application
title = JOKER APP

# (str) Package name
package.name = jokerapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (int) Android NDK version to use
android.ndk = 21

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,pandas,cython

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Version of your application
version = 0.1

# (list) Permissions
android.permissions = INTERNET

# (str) Android entry point
android.entrypoint = org.kivy.android.PythonActivity

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait
