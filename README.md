<!-- Best_README_template -->

# Huki cmd

A GUI terminal by Python3.

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<br />

<p align="center">
 <h3 align="center">A Better Project Than python-cmd</h3>
 <p align="center">
   You can use it by following the information in the directory.
   <br />
   <br />
   <a href="https://github.com/oneachina/Huki">View Repository</a>
   ·
   <a href="https://github.com/oneachina/Huki/issues">Report Bug or Feature</a>
   ·
   <a href="https://github.com/oneachina/Huki/pulls">Submit Pull Request</a>
</p>

中文请去[README_ZH.md](https://github.com/oneachina/Huki/blob/main/README_ZH.md)

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Differences from python-cmd](#differences-from-python-cmd)
- [Roadmap](#roadmap)
- [Getting Started](#getting-started)
- [File Structure](#file-structure)
- [Authors](#authors)

### Differences from [python-cmd](https://github.com/CodeCrafter-TL/python-cmd)
- Faster update cycle
- Better code structure
- Better code comments

### Roadmap
- [ ] Add more commands
- [x] Add plugin support
- [ ] Add more features
- [ ] Better UI
- [x] Add logging

### Getting Started
1. Download the latest [Release](https://github.com/oneachina/Huki/releases) from GitHub.

2. Execute the following command in your working directory:
```bash
git clone https://github.com/oneachina/Huki.git
```
3. Installing Required Packages
Execute the following command in your working directory after cloning:

```bash
pip install -r requirements.txt
```
After installation is complete, use the following command to start using Huki cmd:
```bash
python main.py
```
## File Structure
```
Huki-main
├── Events
│   ├── CustomPlainTextEdit.py
│   └── Event.py
├── Value
│   ├── constants.py
│   └── data.py
|── utils
│   ├── Logger_utils.py
│   └── thread_utils.py
├── README.md
├── LICENSE.txt
├── ui.py
├── main.py
```

> README.md: The help document you are reading

> LICENSE.txt: MIT License information for this project

> ui.py: UI code generated by PyQt5 UI code generator

> main.py: Main program file

> constants.py: Required program string information

## Authors
![github](https://img.shields.io/badge/GitHub-oneachina-green?logo=github)

![github](https://img.shields.io/badge/GitHub-CodeCrafterTL-green?logo=github)

*You can also view all **developers** who participated in this project in the contributors list.*

## Copyright Notice
This project is licensed under the MIT License - see [LICENSE.txt](https://github.com/oneachina/Huki/LICENSE.txt) for details

[project-path]:oneachina/Huki
[contributors-shield]: https://img.shields.io/github/contributors/oneachina/Huki.svg?style=square
[contributors-url]: https://github.com/oneachina/Huki/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/oneachina/Huki.svg?style=square
[forks-url]: https://github.com/oneachina/Huki/network/members
[stars-shield]: https://img.shields.io/github/stars/oneachina/Huki.svg?style=square
[stars-url]: https://github.com/oneachina/Huki/stargazers
[issues-shield]: https://img.shields.io/github/issues/oneachina/Huki.svg?style=square
[issues-url]: https://img.shields.io/github/issues/oneachina/Huki.svg
[license-shield]: https://img.shields.io/github/license/oneachina/Huki.svg?style=square
[license-url]: https://github.com/oneachina/Huki/blob/master/LICENSE.txt