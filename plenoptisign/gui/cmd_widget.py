#!/usr/bin/env python

__author__ = "Christopher Hahne"
__email__ = "inbox@christopherhahne.de"
__license__ = """
Copyright (c) 2019 Christopher Hahne <inbox@christopherhahne.de>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

from plenoptisign import PX, PY, BTN_W

# make object for plot widget
class CmdWidget(tk.Frame):

    def __init__(self, parent):

        # inheritance
        tk.Frame.__init__(self, parent)
        self.parent = parent

        # run button
        run_btn = tk.Button(self, text="Update", width=int(BTN_W), command=self.parent.run)
        run_btn.grid(row=0, column=0, padx=PX, pady=PY)

        # save button
        sav_btn = tk.Button(self, text="Save config", width=BTN_W, command=self.parent.save_cfg)
        sav_btn.grid(row=0, column=1, padx=PX, pady=PY)

        # load button
        lod_btn = tk.Button(self, text="Load config", width=BTN_W, command=self.parent.load_cfg)
        lod_btn.grid(row=0, column=2, padx=PX, pady=PY)

        # about button
        abt_btn = tk.Button(master=self, text='About', width=int(BTN_W), command=self.parent.open_abt_win)
        abt_btn.grid(row=1, column=1, padx=PX, pady=PY)

        # quit button
        qit_btn = tk.Button(master=self, text='Quit', width=int(BTN_W), command=self.parent.quit_app)
        qit_btn.grid(row=1, column=2, padx=PX, pady=PY)