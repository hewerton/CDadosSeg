import sys
import os
from xml.dom import minidom

import config


def __load_files(dir):
    """Loads the contents from all xml files from a given direcotry.

    Parameters:
    dir (str): directory where the files is located.

    Returns:
    list: a dictonary with the content from each xml processed where the key is
    the appname.
    """
    xml_contents = {}
    filenames = os.listdir(dir)
    for filename in filenames:
        filepath = os.path.join(dir, filename)
        with open(filepath, 'r') as file:
            xml_contents[filename[:-4]] = file.read()

    return xml_contents


def __extract_info(xml_content):
    """Extracts the app info from the xml content.

    Parameters:
    -----------
    xml_content : str
        String representing the xml content

    Returns:
    --------
    list
        list with all app's permissions.

    """

    permissions_names = []
    parsed_xml = minidom.parseString(xml_content)

    # extracts all apps permissions
    permissions = parsed_xml.getElementsByTagName('uses-permission')

    for perm in permissions:
        name = perm.getAttribute(
            'android:name')

        # filtering android permissions
        if name.startswith('android'):
            permissions_names.append(name.split('.')[-1])

    return permissions_names


def __load_data(dir):
    """Loads data from all files present in a given directory.

    Parameters:
    -----------
    dir: str, optional
        Directory path whre the xmls files is located.

    Returns:
    dict
        A dictionary where the key is the app name and the value is a list of
        permissions.
    """

    infos = {}
    xmls = __load_files(dir)
    for appname, xml in xmls.items():
        info = __extract_info(xml)
        infos[appname] = info
    return infos


def list_permissions_by_app(dir):
    """Lists all permissions from each app. The permissions list is organized
    by app.
    """

    header = "===================\nPermissões por APK\n==================="

    infos = __load_data(dir)

    print(header)

    for appname, permissions in infos.items():

        line = '{}: {}\n'.format(appname, permissions)
        print(line)


def list_unique_permissions_by_app(dir):
    """Lists unique permissions for each app comparing with all apps listed from
    the manifests directory.
    """

    header = "===================\nPermissões únicas por APK\n==================="

    infos = __load_data(dir)

    infos_sets = {}
    for appname, perm_list in infos.items():
        infos_sets[appname] = set(perm_list)

    print(header)

    for appname, perm_set in infos_sets.items():
        remaining_sets = [s for name,
                          s in infos_sets.items() if name is not appname]

        unique_perms = perm_set.difference(*remaining_sets)

        line = '{}: {}\n'.format(appname, list(unique_perms))
        print(line)


def list_common_permissions(dir):
    """Lists commom permissions from all apps listed from the manifests
    directory.
    """

    header = "===================\nPermissões comuns das APKs\n==================="

    infos = __load_data(dir)

    infos_sets = {}
    for appname, perm_list in infos.items():
        infos_sets[appname] = set(perm_list)

    print(header)

    all_sets = infos_sets.values()
    common_perms = set.intersection(*all_sets)

    line = '{}\n'.format(list(common_perms))
    print(line)


if __name__ == '__main__':

    fun = ""
    dir = config.DATA_FOLDER

    try:
        fun = sys.argv[1]
    except IndexError:
        print('You have to provide a function name: "all" or "unique_and_common".')
        sys.exit(1)

    try:
        dir = sys.argv[2]
    except IndexError:
        print('Using default dir: "{}" located on the project\'s root folder'.format(
            config.DATA_FOLDER))

    if fun == 'all':
        list_permissions_by_app(dir)
    elif fun == 'unique_and_common':
        list_unique_permissions_by_app(dir)
        list_common_permissions(dir)
    else:
        print('Function not recognized. Try "all" or "unique_and_commom".')
