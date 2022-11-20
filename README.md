pyQuill plain text editor
=================
First project in **Python practice** cource.

**Table of Contents**

- [Gallery](#gallery)
- [Features](#features)
- [Installing](#installing)
- [Customization](#customization)
- [Contact](#contact)

# Gallery
White theme:
![White blank editor](/images/theme_white.png)

Default dark theme:
![Dark blank editor](/images/theme_black.png)


# Features
* Basic text editing: select, cut, copy, paste
* Open files, save files, print files
* Standard keyboard shortcuts support

# Installing
Clone this repository and install requirements (pyQt5 required)
```
git clone https://github.com/dm1trykrylov/pyQuill.git && cd pyQuill
pip install -r requirements.txt
```

Run pyQuill
`python3 pyQuill.py`

# Customization
It's easy to design your own themes using `settings.json`.
* Change `default_font` field to set another font
* Change `theme` to dark to use default dark theme or
* set `use_default_theme` to __true__ and provide path to your stylesheet in `stylesheet`

# Contacts
* Name: Dmitry Krylov
* Group: Б05-202
* tg: @dm1trykrylov
