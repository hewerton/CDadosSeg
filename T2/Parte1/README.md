# APK permissions analysis

This project allows extract and analyse the permissions from android apps manifest files.

## Project struture

```bash
|-data - folder with xml files
|
|-tmp - temporary folder with the APK files
|
|-src
|  |-config.py - config file with default folders paths
|  |-crawler.py - extract AndroidManifest.xml from APK
|  |-analysis.py - main project file
|
|-requiriments.txt - project dependencies
```

## Usage

### Extracting the AndroidManifest.xml from APK

1. Put all apk files inside folder tmp.
2. Run the folowing command from project's root folder

   ```bash
   python src/crawler.py
   ```

3. All xml files will be on data folder


### Analysing all manifest files

- All permissions - lists all permissions for each app
  
  ```bash
  python src/analysis.py all <dir_name>
  ```

- Unique and common permissions - lists unique permissions for each app, then lists the permissions common to all apps
  
  ```bash
  python src/analysis.py unique_and_common <dir_name>
  ```

> If no directory name (<dir_name>) is provided, the folder "data" is the default directory where the xml files is looked for.

