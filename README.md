# Scripts for resizing GUIs in Defold

## Setup

Install Python 3. Then:

```
pip install deftree
```

## Resize fonts project-wide in Defold

```
python resize_font.py <path_to_project_root> <name_of_font> <amount_to_scale>
```

This will look through all .gui files for text nodes with font `<name_of_font>` and
scale them by `<amount_to_scale>`.

**This doesn't support game object labels. Feel free to submit a PR**

## Resize GUI to a different design size

```
python resize_gui.py <path_to_project_root> <amount_to_scale>
```

This will look through all .gui files and scale all measurements (position, size, slice9)
by `<amount_to_scale>`. Use this after you changed your project's design 
resolution and after you re-exported all the assets at the new resolution.
