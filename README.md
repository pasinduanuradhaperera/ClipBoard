# Clipboard for macOS ( Works in Linux and Windows Also )

A Python-based clipboard manager for macOS that mimics the functionality of the default clipboard manager in Windows (Win+V). This tool allows users to keep track of clipboard history, set history size limits, and manage copied items efficiently.  

## Features  
- **Dynamic Clipboard Monitoring**: Automatically saves copied text to the clipboard history.  
- **Adjustable History Limit**: Set the maximum number of clipboard entries (default is 20).  
- **History Display**: View clipboard history in a user-friendly GUI.  
- **Easy Management**: Clear history or copy items directly from the history.  
- **Cross-platform Support**: Primarily built for macOS, but compatible with other platforms supporting Python and `pyperclip`.  

## Installation  

1. Clone the repository:  
   ```bash  
   git clone [https://github.com/pasinduanuradhaperera](https://github.com/pasinduanuradhaperera)/Clipboard.git  
   cd Clipboard  
   ```  

2. Install the required dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  

3. Run the application:  
   ```bash  
   python clipboard.py  
   ```  

## Requirements  
- Python 3.7 or above  
- `tkinter` (pre-installed with Python)  
- `pyperclip`  

## Usage  

1. **Monitor Clipboard**: The application automatically tracks and saves new clipboard entries.  
2. **Set History Limit**: Use the GUI to adjust the maximum number of entries saved in history.  
3. **View & Manage History**: View all clipboard entries, clear history, or copy an item back to the clipboard.  

## Preview  
![Clipboard App Preview](https://raw.githubusercontent.com/pasinduanuradhaperera/ClipBoard/bcc63a3c875e90a2f2f0405b3280c6fd1346876f/Ui%20.png)  
*A simple and intuitive user interface.*

## Contributing  

We welcome contributions! If you'd like to contribute:  

1. Fork the repository.  
2. Create a new branch for your feature or bug fix.  
3. Commit your changes and submit a pull request.  

Please ensure your code adheres to the [PEP 8](https://pep8.org/) coding standards.  

## License  

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.  

## Acknowledgments  

- Inspired by Windows' default clipboard manager (Win+V).  
- Built with ❤️ by ![@pasinduanuradhaperera](https://github.com/pasinduanuradhaperera).  

---

Feel free to create issues or submit feature requests in the [Issues](https://github.com/pasinduanuradhaperera/Clipboard/issues) section.

