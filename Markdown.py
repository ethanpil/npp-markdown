# markdown.py for Notepad++ Python Scripting plugin
# https://github.com/ethanpil/npp-markdown
#
# A Notepad++ Python Scriping Plugin implementation of John Gruber's Markdown.
# Converts Markdown to HTML
# See: http://packages.python.org/Markdown/
#
# Version 1.0
#
## Installation
#  1. Copy **Markdown.py** to **\plugins\PythonScript\scripts\** in your NPP folder
#  2. Copy the **markdown** folder to **\plugins\PythonScript\lib\** in your NPP folder
#  3. Restart NPP. It will now appear as a menu item under Plugins...Python Script...Scripts
#
## Usage
#  1. Select the text to minify, or select nothing.
#  2. Go to the NPP menu, Plugins...Python Script...Scripts...Markdown and click!
#  3. If selected text is detected, it mins and replaces the selected text, otherwise the entire contents of current document.
#  4. Undo is available if you dont like the results
#
##Credits
# John Gruber - Markdown - http://daringfireball.net/projects/markdown/
# The Python Markdown Project - http://packages.python.org/Markdown/

import markdown

editor.beginUndoAction()

#If we have selected text, only minify that, otherwise, minify entire document
seltext = editor.getSelText()
seltextlen = len(seltext)

if seltextlen >= 1 :
	rawtext = seltext
	html = markdown.markdown(rawtext)
	editor.replaceSel(str(html))
else:
	rawtext = editor.getText()
	html = markdown.markdown(rawtext)
	editor.setText(str(html))	
	