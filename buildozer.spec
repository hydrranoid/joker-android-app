name: Build APK

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Set up JDK
      uses: actions/setup-java@v2
      with:
        distribution: 'zulu'
        java-version: '11'

    - name: Install dependencies
      run: |
        sudo apt update
        sudo apt install -y python3-pip build-essential git
        pip install cython
        pip install buildozer

    - name: Build APK
      run: |
        cd ${{ github.workspace }}
        buildozer android debug

    - name: Upload APK
      uses: actions/upload-artifact@v2
      with:
        name: MyApp-APK
        path: bin/*.apk
