<p align="center">
  <img src="https://github.com/ItzZyann/gd-patcher/raw/main/assets/gdp-logo.png" alt="Logo">
</p>

# Geometry Dash Patcher

This script allows you to patch the `libcocos2dcpp.so` file in Geometry Dash (v2.206 / v2.2.142) to enable various modifications. Only `armeabi-v7a` architecture is supported; `arm64-v8a` is not compatible with modifications for this version of Geometry Dash.

## Requirements

1. **Geometry Dash APK**: Version 2.206 / v2.2.142.
2. **APKTool**: Use `apktool m` (by Maximoff) for modifying the APK. You can find the APKTool version for Windows as well.
3. **Python Environment**: Python 2.7 installed.

## Patching Instructions

### Windows

1. **Extract Geometry Dash APK**:
   - Use APKTool to decompile the Geometry Dash APK:
     ```sh
     apktool d GeometryDash.apk
     ```
   - Navigate to the decompiled APK folder (`GeometryDash`).

2. **Prepare the Patch Script**:
   - Place the `gdpatcher.py` script inside the `GeometryDash` folder.

3. **Run the Patcher**:
   - Open Command Prompt (`cmd`) and navigate to the `GeometryDash` folder:
     ```sh
     cd path\to\GeometryDash
     ```
   - Execute the patcher script:
     ```sh
     python gdpatcher.py
     ```
   - Follow the prompts to select patches. Type `exit` to apply selected patches.

4. **Recompile the APK**:
   - After patching, recompile the APK using APKTool:
     ```sh
     apktool b GeometryDash -o ModifiedGeometryDash.apk
     ```

5. **Install the Modified APK**:
   - Transfer `ModifiedGeometryDash.apk` to your device and install it.

### Termux (Android)

1. **Install Termux**:
   - Install Termux from the Termux App Releases github or Google Play Store if you want, or in FDroid.

2. **Set Up Environment**:
   - Open Termux and install necessary packages:
     ```sh
     pkg update
     pkg upgrade
     pkg install python2 git
     ```
     
3. **Run the Patcher**:
   - Copy `gdpatcher.py` script to the `GeometryDash` folder if not already there.
   - Execute the patcher script:
     ```sh
     python2 gdpatcher.py
     ```
   - Follow the prompts to select patches. Type `exit` to apply selected patches.

4. **Recompile the APK**:
   - After patching, recompile the APK using APKTool_m, be sure to delete arm64-v8a folder.

5. **Install the Modified APK**:
   - Install it on your device.

## Credits

- **WylieMaster**: For initial script inspiration.

---