# Third party imports
import tkinter as tk

# Local application imports
from GUI.Main_screen import EmpowerU

def main():
    """
    The main function definition.

    Parameters:
    (None)

    Returns:
    (None)
    """
    root = EmpowerU(title="EmpowerU", width=860, height=620, bg="navy")
    root.mainloop()
    print("EmpowerU proper shutdown completed.")


if __name__ == "__main__":
    # DO NOT MODIFY
    main()
