"""
functions.py
molssi workshop: A python package for analyzing and visualizing xyz file.

Handles the primary functions
"""


def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format)

    Replace this function and doc string for your own project

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution
    """

    quote = "Change the quote"
    if with_attribution:
        quote += "\n\t- The Universe"
    return quote


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
