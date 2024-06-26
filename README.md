
# PackTXT

PackTXT is a Python CLI tool that allows you to pack and unpack project directories into and from `.txt` files. It supports packing from specific Git branches as well.

## Features

- Pack a Directory: Compress a specified directory into a `.txt` file.
- Pack a Git Branch: Compress files from a specified Git branch into a `.txt` file.
- Unpack a `.txt` File: Decompress a `.txt` file into a specified directory.

## Installation

You can install PackTXT via pip:

```bash
pip install packtxt
```

## Usage

### Pack a Directory

```bash
packtxt pack <directory_path> [--branch <branch_name>] [--output <output_path>]
```

### Unpack a `.txt` File

```bash
packtxt unpack <txt_file> [--output <output_dir>]
```

### Example Workflow

1. Initialize a Git Repository:

```bash
cd my_project
git init
```

2. Add Files to the Pack:

```bash
git add file1.txt dir2/
git commit -m "Add files to pack"
```

3. Pack Files from a Git Branch to a `.txt` File:

```bash
packtxt pack ./my_project --branch new-branch --output my_project.txt
```

4. Unpack the `.txt` File:

```bash
packtxt unpack my_project.txt --output unpacked_project
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
