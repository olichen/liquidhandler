import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from . import protocol_writer
from .gui import pipette_input_panel
from .gui import plate_input_panel
from .gui import config
import logging
from .helpers import log_helper
from platform import system
import traceback
import webbrowser
import subprocess
import os


class ProtocolGenerator:
    def __init__(self):
        # Initialize window
        self.window = tk.Tk()
        self.window.title('Protocol Generator')
        self.window.resizable(False, False)
        self.addMenubar()

        # Initialize the first input panel
        self.input_panels = []
        self.addPipettePanel()
        self.addPlatePanel()
        self.createBottomMenu()

        # Initialize log handler
        self.lh = log_helper.LogHandler()
        logger = logging.getLogger()
        logger.addHandler(self.lh)

    # Adds the File and Help menus
    def addMenubar(self):
        menubar = tk.Menu(self.window)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label='Generate Protocol', command=self.save)
        filemenu.add_command(label='Edit Labware', command=self.editLabware)
        filemenu.add_command(label='Quit', command=self.quit)
        menubar.add_cascade(label='File', menu=filemenu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label='Help', command=self.help)
        helpmenu.add_command(label='About', command=self.about)
        menubar.add_cascade(label='Help', menu=helpmenu)

        self.window.config(menu=menubar)

    # Adds a pipette selector panel
    def addPipettePanel(self):
        ip = pipette_input_panel.PipetteInputPanel(self.window)
        ip.grid(row=len(self.input_panels), sticky='nesw')
        self.input_panels.append(ip)

    # Add a plate selector panel
    def addPlatePanel(self):
        if len(self.input_panels) < 4:
            ip = plate_input_panel.PlateInputPanel(self.window)
            ip.grid(row=len(self.input_panels), sticky='nesw')
            self.input_panels.append(ip)

    # Add bottom menu: add transfer, remove transfer, generate protocol
    def createBottomMenu(self):
        frame = ttk.Frame(self.window)
        frame.grid(row=100, sticky='nesw')

        save = ttk.Button(frame, text='Generate', width=12, command=self.save)
        save.pack(side=tk.RIGHT)

        rem_input = ttk.Button(frame, text='Remove', width=12,
                               command=self.remPlatePanel)
        rem_input.pack(side=tk.RIGHT)

        add_input = ttk.Button(frame, text='Add', width=12,
                               command=self.addPlatePanel)
        add_input.pack(side=tk.RIGHT)

    # Remove a plate input panel
    def remPlatePanel(self):
        if len(self.input_panels) > 2:
            panel = self.input_panels.pop()
            panel.destroy()

    # Outputs the protocol to a file
    def save(self):
        pw = protocol_writer.ProtocolWriter()

        try:
            # Read in data from each input panel. Throws an exception if
            # invalid data is encountered
            for ip in self.input_panels:
                pw.addData(ip.getData())

            if ofile := filedialog.asksavefilename(title='Save Protocol'):
                pw.saveOutput(ofile)

                if self.lh.text:
                    log_helper.WarningMessageBox(self.window, self.lh.text)
                self.quit()
            else:
                self.lh.clear()
                self.window.focus()
        except Exception as e:
            traceback.print_exc()
            messagebox.showerror(title='Error', message=e)
            self.lh.clear()
            self.window.focus()

    # Open the labware.ini file for editing
    def editLabware(self):
        if not os.path.exists('./labware.ini'):
            cfg = config.Configuration('./labware.ini')
            cfg.writeFile('./labware.ini')

        OS = system().lower()
        if 'windows' in OS:
            opener = 'start'
        elif 'osx' in OS or 'darwin' in OS:
            opener = 'open'
        else:
            opener = 'xdg-open'
        subprocess.run(opener + ' labware.ini', shell=True)
        msg = 'Please restart the protocol generator after editing any labware'
        messagebox.showinfo(title='Labware', message=msg)

    # Exit the application
    def quit(self, event=None):
        self.window.destroy()

    # Open the home page on github
    def help(self):
        url = 'https://github.com/olichen/ot2_protocol_generator#readme'
        webbrowser.open(url)

    # Pop open an about box
    def about(self):
        msg = ('Version 1.0\n'
               'Copyright (c) 2020 Oliver Chen\n'
               'https://github.com/olichen/ot2_protocol_generator')
        messagebox.showinfo(title='About', message=msg)
