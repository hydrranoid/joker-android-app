[app]

# (str) Title of your application
title = JOKER APP

# (str) Package name
package.name = jokerapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (int) Android SDK version to use
android.sdk = 24

# (int) Android NDK version to use
android.ndk = 21

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,pandas

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin, venv

# (list) List of exclusions using pattern matching
# Do not prefix with './'
#source.exclude_patterns = license,images/*/*.jpg

# (int) Application versioning (method 1)
version = 0.1

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of: landscape, portrait or all)
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

# (str) URL to open when clicking on the notification
#android.notifications.url = None

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Full name including package name for the Android entry point
#android.entrypoint.classname = org.kivy.android.PythonActivity

# (str) Android app theme, supported formats are `@android:style/Theme.Light` or `@style/Theme.AppCompat`
# android.apptheme = @android:style/Theme.NoTitleBar

# (str) Title of your application for the Android Notification Center
#android.notifications.title = JOKER APP

# (str) Additional permissions
#android.permissions = INTERNET

# (str) Android SDK path (if not set, it will automatically download pure SDK)
#android.sdk_path =

# (str) Android NDK path (if not set, it will automatically download pure NDK)
#android.ndk_path =

# (str) Android directory for Gradle
#android.gradle_path =

# (str) Android ant path (if not set, it will automatically download pure Ant)
#android.ant_path =

# (str) Android application metadata to set on your APK
#android.meta_data = my_key_name=my_key_value

# (bool) Indicate if the application should be indexed
#android.indexed = True

# (list) Android logcat filters to use
#android.logcat_filters = *:S python:D

# (bool) Copy library instead of linking (affects only Android)
#android.copy_libs = False

# (list) The Java classes to add as activities to the main Java class (android)
#android.add_activities = com.example.ExampleActivity

# (str) Android entry point for services
#android.service = org.kivy.android.PythonService

# (list) Android application meta-data to add in AndroidManifest.xml
#android.manifest_meta_data = com.google.android.maps.v2.API_KEY=my_google_api_key
