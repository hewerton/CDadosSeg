import sys
import os
import pefile


DATA_FOLDER = 'data/'


def __load_pe_file(file_path):
    """Loads a PE file.

    Parameters:
    -----------
    file_path: str
        Path where the ".exe" file is located.

    Returns:
    --------
    tuple
        A tuple with the filename at the first position and a PE instance at
        the second position.
    """

    pe_file = pefile.PE(file_path)

    return os.path.basename(file_path), pe_file


def __load__all_pe_files(dir):
    """Loads all PE files located at a given directory.

    Parameters:
    -----------
    dir: str
        Directory path.

    Returns:
    --------
    list of tuples
        A list of tuples where each tuple contains
        the filename at the first position and a PE instance at
        the second position.
    """

    filenames = os.listdir(dir)
    pe_files = []
    for filename in filenames:
        file_path = os.path.join(dir, filename)
        pe_files.append(__load_pe_file(file_path))

    return pe_files


def enumerate_exe_sections(*pe_files):
    """Searchs for PE sections that is executable.

    Parameters:
    -----------
    *pe_files: list
        List of tuples with filename and PE instance.

    Returns:
    --------
    list of tuples
        A list of tuples where each tuple contains
        the filename at the first position and a list of
        exeutable sections.
    """

    executable_sections = []
    for filename, pe_file in pe_files:
        sections = [section.Name.decode(
            'UTF-8').rstrip('\x00') for section in pe_file.sections if section.IMAGE_SCN_MEM_EXECUTE]
        executable_sections.append((filename, sections))

    return executable_sections


def print_exe_sections(exe_sections):
    """Prints the executable sections for 

    Parameters:
    -----------
    *exe_sections: list
        List of tuples with filename and executable sections.

    """

    header = "===================\n"\
        "Seções executáveis\n" \
        "==================="

    print(header)

    for filename, sections in exe_sections:
        print('{}: {}'.format(filename, sections))


if __name__ == '__main__':

    if len(sys.argv) < 2:

        print('Using default data folder.')

        dir = DATA_FOLDER
        pe_files = __load__all_pe_files(dir)
        sections = enumerate_exe_sections(*pe_files)
        print_exe_sections(sections)

    elif len(sys.argv) == 2:
        path = sys.argv[1]

        if path.endswith('.exe') and os.path.isfile(path):
            pe_file = __load_pe_file(path)
            sections = enumerate_exe_sections(pe_file)
            print_exe_sections(sections)

        elif os.path.isdir(path):
            pe_files = __load__all_pe_files(path)
            sections = enumerate_exe_sections(*pe_files)
            print_exe_sections(sections)

        else:
            raise ValueError(
                'The provided path must be a directory or a ".exe" file.')

    else:
        raise ValueError(
            'You must provide only one '
            'argument that can be a directory or a ".exe" file.')
