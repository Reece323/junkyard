# -*- coding: utf-8 -*-
import os
import tkinter as tk

from opencv.logic_logger import init_logging, logging
from opencv.gui_main import MainGUI

if __name__ == '__main__':
    init_logging()
    logging.info('Start software')
    this_dir = os.path.dirname(os.path.realpath(__file__))  # path to this directory
    os.chdir(this_dir)  # make path to this dir the current path
    app = MainGUI(tk.Tk())  # start the application
    if hasattr(app, 'camera'):  # object has attribute 'camera'
        app.mainloop()  # application is up and running
    logging.info('Finish software')
