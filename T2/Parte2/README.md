# PE sections analysis

This project allows extract and analyse the sections from PE files.

## Project struture

```bash
|-data - default folder with PE files
|
|-src
|  |-compare_bins.py - compares sections of two PE fils
|  |-enumerate_sections.py - enumerates executable sections from PE
|
|-requiriments.txt - project dependencies
```

## Usage

### Enumerating sections from PE files

1. Put all PE files inside folder data.
2. Run the folowing command from project's root folder

   ```bash
   python src/enumerate_sections.py
   ```

   or pass outher folder path

   ```bash
   python src/enumerate_sections.py <dir_name>
   ```

   or pass a PE file

   ```bash
   python src/enumerate_sections.py <executable.exe>
   ```



### Comparing two PE files

1. Run the folowing command from project's root folder
  
  ```bash
  python src/compare_bins.py <executable1.exe> <executable2.exe>
  ```


