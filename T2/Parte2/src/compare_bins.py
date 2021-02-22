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


def compare_bins(file_path1, file_path2):
    """Compares the sections of two PE files.

    Parameters:
    -----------
    file_path1: str
        Path where the first file is located.

    file_path2: str
        Path where the second file is located.

    Returns:
    --------
    tuple
        A tuple with the common sections at the first position, the unique
        sections of the first file at the second position and the unique
        sections of the second file at the third position.
    """

    _, pe_file1 = __load_pe_file(file_path1)
    _, pe_file2 = __load_pe_file(file_path2)

    sections_names1 = [section.Name.decode(
        'UTF-8').rstrip('\x00') for section in pe_file1.sections]

    sections_names2 = [section.Name.decode(
        'UTF-8').rstrip('\x00') for section in pe_file2.sections]

    common_sections = list(set.intersection(
        set(sections_names1), set(sections_names2)))
    unique_sections_pe_file1 = list(set(
        sections_names1).difference(set(sections_names2)))
    unique_sections_pe_file2 = list(set(
        sections_names2).difference(set(sections_names1)))

    return common_sections, unique_sections_pe_file1, unique_sections_pe_file2


def print_results(results):
    """Prints the common and unique sections of two PE files.

    Parameters:
    -----------
    results: tuple
        A tuple with the common sections at the first position, the unique
        sections of the first file at the second position and the unique
        sections of the second file at the third position.

    """

    header1 = "===================\n"\
        "Seções comuns aos dois arquivos executávies\n" \
        "==================="

    header2 = "===================\n"\
        "Seções presesentes apenas no primeiro executável\n" \
        "==================="

    header3 = "===================\n"\
        "Seções presesentes apenas no segundo executável\n" \
        "==================="

    common, unique1, unique2 = results

    print(header1)
    print(common)
    print(header2)
    print(unique1)
    print(header3)
    print(unique2)


if __name__ == '__main__':

    if len(sys.argv) == 3:
        path1 = sys.argv[1]
        path2 = sys.argv[2]

        verify_path1 = path1.endswith('.exe') and os.path.isfile(path1)
        verigy_path2 = path2.endswith('.exe') and os.path.isfile(path2)

        if verify_path1 and verigy_path2:
            results = compare_bins(path1, path2)
            print_results(results)
        else:
            raise ValueError(
                'The provided path must be a directory or a ".exe" file.')

    else:
        raise ValueError(
            'You must provide two '
            'arguments that must be ".exe" files.')
