'''
Created on Dec 28, 2016

@author: jpjohnson
'''

from Tkinter import *
from append_value import main as _apv
import tkFileDialog
import tkMessageBox as mbox
import os
import csv


class UserInput(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, background="gray")
        self.centerWindow()

        self.columnconfigure(1, weight=1)

        self.infilename = StringVar()
        self.infilename.set('Upload CSV file...')
        self.outfile_dir = StringVar()
        self.outfile_dir.set('Select Output Directory...')
        self.col_num = StringVar()
        self.col_num.set('')

        lbl1 = Label(self, text="Input File:", background="gray")
        lbl1.grid(sticky=W, pady=4, padx=4)
        entry1 = Entry(self, state=DISABLED, relief=SUNKEN, textvariable=self.infilename)
        entry1.grid(row=0, column=1, padx=4, ipadx=50, sticky=W+E)
        upload_button = Button(self, text="Select File...", command=self.browse_infile)
        upload_button.grid(row=0, column=2, padx=4, sticky=W+E)

        lbl2 = Label(self, text="Output Directory(Optional):", background="gray")
        lbl2.grid(sticky=W, pady=4, padx=4)
        entry2 = Entry(self, state=DISABLED, relief=SUNKEN, textvariable=self.outfile_dir)
        entry2.grid(row=1, column=1, padx=4, sticky=W+E)
        output_button = Button(self, text="Save to..", command=self.browse_dir)
        output_button.grid(row=1, column=2, padx=4, sticky=W+E)

        lbl3 = Label(self, text="CSV Column Number:", background="gray")
        lbl3.grid(sticky=W, pady=4, padx=4)
        col_num = Entry(self, validate="key", textvariable=self.col_num)
        col_num['validatecommand'] = (col_num.register(self.num_only), '%P', '%i', '%d')
        col_num.grid(row=2, column=1, padx=4, ipadx=5, sticky=W)

        excute_button = Button(self, text="Run")
        excute_button.bind('<Return>', self.run_file)
        excute_button.bind('<ButtonRelease-1>', self.run_file)
        excute_button.grid(row=3, column=2, sticky=W+E, padx=4)

        quitButton = Button(self, text="Close", command=self.on_quit)
        quitButton.grid(row=4, column=2, sticky=W+E, padx=4)

    def centerWindow(self):
        self.master.title("Append Data")
        self.pack(fill=BOTH, expand=True)

        w = 475
        h = 150
        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()
        x = (sw - w)/2
        y = (sh - h)/2
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def browse_infile(self):
        file_name = tkFileDialog.askopenfilename(filetypes=[('Text files', '*.CSV')])
        self.infilename.set(file_name)

    def browse_dir(self):
        file_dir = tkFileDialog.askdirectory()
        self.outfile_dir.set(file_dir)

    def run_file(self, event):
        column = self.col_num.get()
        input_file = self.infilename.get()
        out_file = ''
        out_dir = self.outfile_dir.get()
        file_name = os.path.basename(input_file)
        dir_path = os.path.dirname(input_file)

        infile = open(input_file, "rb")
        reader = csv.reader(infile)
        file_col_count = len(next(reader))

        # Check out directory
        if out_dir == 'Select Output Directory...' or out_dir == '':
            out_file = dir_path + '/' + 'new' + file_name
        else:
            out_file = out_dir + '/' + 'new' + file_name

        # Check input file
        if input_file == 'Upload CSV file...' or input_file == '':
            mbox.showerror('Error', 'Please Select a valid input File')
            return

        # Check column field compared to column count in file
        if column == '':
            mbox.showerror('Error', '"Column Number:" field requires a number')
            return
        elif int(column) == 0:
            mbox.showerror('Error', '"Column Number:" field cannot be 0')
            return
        elif int(column) > int(file_col_count):
            mbox.showerror('Error', '"Column Number:" Value exceeds number of'
                           ' columns in file: ' + str(file_col_count))
            return
        else:
            new_file = _apv(input_file, column, out_file)
            if new_file is not None:
                mbox.showinfo('Success', 'Writing of CSV to: ' + out_file + ' was successful')
                root.destroy()
            else:
                mbox.showerror('Error', 'Writing of CSV was not successful')

    def num_only(self, inStr, i, acttyp):
        ind = int(i)
        if acttyp == '1':  # insert
            if not inStr[ind].isdigit():
                return False
        return True

    def on_quit(self):
        if mbox.askokcancel("Close Program", "Are you sure to quit?"):
            root.destroy()


root = Tk()
root.geometry("350x300+300+300")
app = UserInput(root)
root.mainloop()
