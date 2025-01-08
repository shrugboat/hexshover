# HexShover

HexShover is a simple python utility for writing hex code into files at addresses specified by the filenames of *.hex files located in the same directory as HexShover.py. This is useful for iterative romhacking testing and development.
DRAG_and_SHOVE.bat is included for drag and drop (and shove) functionality.
User can also drag files onto shortcuts to DRAG_and_SHOVE.bat (useful for complex project directory workflows).
## Example Folder Structure
    HexShover/
    ├── HexShover.py
    ├── DRAG_and_SHOVE.bat
    ├── ExampleNumberOne_0xF0938.hex
    ├── Example2_0xF0A2F.hex
    └── Video Game Rom (USA).z64

## Typical Usage
Dragging the example file "Video Game Rom (USA).z64" onto DRAG_and_SHOVE.bat will find all *.hex files in that directory (ignoring subdirectories) and Paste Write the contents of each hex file at the addresses specified in their filenames. 

* Paste Write actions will overwrite everything in the source file at those locations for the lengths of each hex file shoved.
* There is no limit to number of hex files that can be shoved this way.

## Naming Structure for Hex Files
    <DescriptiveText>_<HexAddress>.hex
* The file name should always end with a hexadecimal address prefixed by 0x (e.g., 0xF0938).
* The text before the hex address can be anything and is not used in the actual processing of the file.
* The file extension is always .hex.
