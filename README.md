# Steganography - Hide Text in Images

This is a simple steganography tool that allows users to hide and reveal text messages within image files using Python and the `stegano` library. The graphical user interface (GUI) is built using `Tkinter`.

## Features
- Load an image file (PNG or JPG)
- Hide a secret message within the image
- Reveal hidden messages from an encoded image
- Save the modified image with the hidden message
- Reset the interface for new operations

## Dependencies
Ensure you have the following Python libraries installed:

```bash
pip install pillow stegano
```

## How to Use

1. **Open Image**: Click the "Open Image" button to select an image file.
2. **Enter Message**: Type your secret message in the text box.
3. **Hide Data**: Click the "Hide Data" button to encode the message within the selected image.
4. **Save Image**: Click the "Save Image" button to save the modified image with the hidden message.
5. **Show Data**: Click the "Show Data" button to reveal the hidden message from the image.
6. **Reset**: Click the "Reset" button to clear the interface and start over.

## Project Structure
```
├── main.py  # Python script containing the GUI and logic
├── logo.jpg  # Application icon
├── logo1.png  # UI logo
```

## Requirements
- Python 3.x
- Tkinter (comes pre-installed with Python)
- PIL (Python Imaging Library)
- Stegano (for hiding and revealing messages in images)


