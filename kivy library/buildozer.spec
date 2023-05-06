# Buildozer.spec file example for building an apk

[app]

# App name and package name
title = Example App
package.name = example

# Application version
version = 0.1

# Description of the application
description = This is a sample application for building an apk with Buildozer

# Author name
author = John Doe

# Author email
author_email = john.doe@example.com

# Minimum required Android version for the application
min_sdk = 21

# List of source files for the application
source.dir = C:\Users\user\Desktop\Programs\Python\GPT_app\kivy library
source.include_exts = py,kv

[buildozer]

# Android target platform
android.platform = 21

[android]

# Specify Android target platform
android.api = 21

# List of required Android permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE,CAMERA

# Orientation of the application
android.orientation = portrait

[python]

# Python version used in the application
python.version = 3.10

[requirements]

# List of required Python packages for the application
kivy = 1

[kivy]

# Use Kivy version
kivy.version = 1

# Kivy version for building the apk
kivy.branch = stable

