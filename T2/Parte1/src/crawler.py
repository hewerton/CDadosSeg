import sys
import os
from zipfile import ZipFile
from xml.dom import minidom


from androguard.core.bytecodes.apk import APK
import config


def list_apks(dir):
    """Lists all apk files inside temp folder.

    Parameters:
    -----------
    dir: str
        Folder where the APK files is located.

    Returns:
    --------
    list of str
        List with all APK files names.

    """
    apks = []
    all_files = os.listdir(dir)
    apks = [file for file in all_files if file.endswith('.apk')]
    return apks


def extract_manifest(apk_file_path):
    """Extracts the AndroidManifest.xml file from an APK and write it in
    a new file.

    Parameters:
    -----------
    apk_file_path: str
        APK relative file path

    """

    apk = APK(apk_file_path)

    app_name = apk.get_app_name()
    axml = apk.get_android_manifest_axml()
    version = apk.get_androidversion_name()
    manifest = minidom.parseString(
        axml.get_buff()).toprettyxml()

    # Building filename
    app_name = app_name.replace(' ', '')
    version = version.replace(' ', '_')
    manifest_filename = "{}-{}.xml".format(app_name, version)

    manifest_path = os.path.join(config.DATA_FOLDER, manifest_filename)

    with open(manifest_path, 'w', encoding='utf8') as file:
        file.write(manifest)


def main(dir):
    """Extracts AndroidManifest.xml from all APK files from a given directory.
    """
    apks = list_apks(dir)

    for apk_filename in apks:
        apk_file_path = os.path.join(dir, apk_filename)
        extract_manifest(apk_file_path)


if __name__ == '__main__':

    dir = config.TMP_FOLDER

    try:
        dir = sys.argv[1]
    except IndexError:
        print('Using default dir: "{}" located on the project\'s root folder'.format(
            config.TMP_FOLDER))

    main(dir)
