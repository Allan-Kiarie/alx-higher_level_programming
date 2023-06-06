#!/usr/bin/python3
# 5-text_indentation.py
"""Defines a function that prints a new line after certain characters"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters:
    ., ? and :

    Args:
        text(str) = input text

    Raises:
        TypeError: if text is not string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_marks = ['.', ':', '?']
    lines = []
    line = ""

    for char in text:
        line += char

        if char in punctuation_marks:
            line = line.strip()
            lines.append(line)
            lines.append("")
            line = ""
        elif char == '\n':
            line = line.strip()
            lines.append(line)
            line = ""

    if line:
        line = line.strip()
        lines.append(line)

    for line in lines:
        print(line)
