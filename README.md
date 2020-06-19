# Resize fonts project-wide in Defold

## Setup

Install Python 3. Then:

```
pip install deftree
```

## Usage:

```
python resize_font.py <path_to_project_root> <name_of_font> <amount_to_scale>
```

This will look through all .gui files for text nodes with font `<name_of_font>` and
scale them by `<amount_to_scale>`.

**This doesn't support game object labels. Feel free to submit a PR**