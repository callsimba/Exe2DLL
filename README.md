# Exe2DLL
# EXE ↔ DLL Converter


EXE ↔ DLL Converter is a user-friendly tool that allows you to seamlessly convert executable files (.exe) to dynamic link library files (.dll) and vice versa. This lightweight and efficient application is designed with a clean GUI to make the conversion process straightforward.



## Table of Contents
- [Features](#features)
- [Screenshots](#screenshots)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Credits](#credits)
- [License](#license)
- [Contribution](#contribution)

## Features

- **Two-way Conversion:**
  - Convert .exe files to .dll
  - Convert .dll files to .exe
- **Clean and Modern GUI:**
  - Built with PyQt5 for a professional and intuitive user interface
- **Safe Operations:**
  - Prevents overwriting existing files with validation and prompts
- **Hover Animations:**
  - Smooth animations for enhanced user experience
- **About Section:**
  - Credits to the developer and client

## Screenshots

### Main Application
![Screenshot 2024-11-29 011032](https://github.com/user-attachments/assets/187b206a-9933-47a2-ac38-e48d956c3b2e)


![Screenshot 2024-11-29 011044](https://github.com/user-attachments/assets/db4a59b4-4b92-49cc-9650-91f1cdf5e638)


## Requirements

- Python 3.7+
- PyQt5
- shutil (built-in)

## Installation

1. Clone the Repository
   ```
   git clone https://github.com/callsimba/Exe2DLL.git
   cd exe-dll-converter
   ```

2. Install Dependencies
   ```
   pip install -r requirements.txt
   ```

3. Run the Application
   ```
   python main.py
   ```

### Packaging into an Executable

You can package the application into a standalone executable using PyInstaller:

1. Install PyInstaller:
   ```
   pip install pyinstaller
   ```

2. Create the Executable:
   ```
   pyinstaller --onefile main.py --noconsole --icon=resources/icon.ico
   ```

The executable will be available in the `dist` folder.

## Folder Structure

```
project/
│
├── main.py               # Entry point of the application
├── gui.py                # GUI implementation
├── converter.py          # Conversion logic
├── requirements.txt      # Python dependencies
├── resources/            # Assets (icons, splash screen, styles)
│   ├── icon.ico
│   ├── styles.qss
│
└── dist/                 # Output folder for packaged executable (created by PyInstaller)
```

## Usage

1. Launch the application.
2. Select the EXE to DLL or DLL to EXE tab based on the conversion you need.
3. Use the Browse buttons to select the input file and specify the output destination.
4. Click the Convert button to initiate the process.
5. View the confirmation or error messages.

## Troubleshooting

- **File Not Found Error:** Ensure the input file exists at the specified path.
- **Permission Denied Error:** Run the application with appropriate permissions if accessing restricted files.
- **Icon Not Displayed in Executable:** Ensure the .ico file is included during packaging.

## Credits

- Developer: Simba for (CallEnki)

## License

This project is licensed under the MIT License.

## Contribution

Contributions are welcome! Please follow these steps:

1. Fork the repo
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a pull request
