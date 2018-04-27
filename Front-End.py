# -*- coding: UTF-8 -*-
import numpy as np
import os
import PIL.Image
import tkFont
from Tkinter import *
from PIL import Image, ImageTk
import paramiko


#Create the Registration window
master1 = Tk() #  (main) window
master1.title("Chatbot")  #Title the form
master1.configure(background = '#800000')
Label(master1, text="Simple ChatBot",fg='#FFFFFF',font=("Segoe UI Light", 40),bg='#800000').grid(row=0,columnspan=1,sticky=W,padx=20,pady=10)
Label(master1, text="________________",fg='#FFFFFF',font=("Segoe UI Light", 20),bg='#800000').grid(row=2,columnspan=1,sticky=W,padx=100,pady=0)

menubar = Menu(master1)
master1.config(menu=menubar)

fileMenu = Menu(menubar)





def about(event):
    about_window=Tk()
    about_window.title("About")
    about_window.configure(background = '#800011')
    Label(about_window, text="About",fg='#FFFFFF',font=("Segoe UI Light",30),bg='#800011').grid(row=0,sticky=W,padx=20,pady=20)
    Label(about_window, text="Simple ChatBot (with RSA Encryption)",fg='#FFFFFF',font=("Segoe UI Light",15),bg='#800011').grid(row=1,sticky=W,padx=20,pady=0)
    Label(about_window, text="Version 10.1604.21020.0",fg='#FFFFFF',font=("Segoe UI Light",15),bg='#800011').grid(row=2,sticky=W,padx=20,pady=0)
    Label(about_window, text="Developed by Joel Jogy",fg='#FFFFFF',font=("Segoe UI Light",15),bg='#800011').grid(row=3,sticky=W,padx=20,pady=0)
    Label(about_window, text="© Copyright 2018 MIT,Manipal",fg='#FFFFFF',font=("Segoe UI Light",15),bg='#800011').grid(row=4,sticky=W,padx=20,pady=0)
    Label(about_window, text="All rights reserved.",fg='#FFFFFF',font=("Segoe UI Light",15),bg='#800011').grid(row=5,sticky=W,padx=20,pady=0)
    Label(about_window, text=" ",fg='#FFFFFF',font=("Segoe UI Light",15),bg='#800011').grid(row=6,sticky=W,padx=20,pady=0)



def about2():
   return about(1)

def rsa():
    def main():
        n = e = d = 0
        while 1:
            print " 1. Set Public Key \n 0. Quit"
            choice = input("Enter Choice:")
            if choice == 1:
                n, e, d = set_keys()
            if choice == 0:
                break


    def prime(number):
        count=0
        try:
            for i in range(1,number+1):
                if number%i==0:
                    count+=1
            if count>2 or count==1:
                return 0
            else:
                return 1
        except MemoryError:
            return 1


    def set_keys():
        """This fuction asks for 2 primes. 
        It sets a public key and an encoding number, 'e'."""
        xyz=0
        while xyz==0:       
            p = input("Enter Prime Number (I): ")
            q = input("Enter Prime Number (II): ")
            xyz=1
##            test1=prime(p)
##            test2=prime(q)
##            if test1 == 1 and test2==1:
##                xyz=1
##            else:
##                print
##                print"Incorrect values for prime numbers."
##                print"Enter again"
##                print
            
        n = p * q
        m = (p - 1) * (q - 1)
        e = get_e(m)
        d = get_d(e, m)
        while d < 0:
            d += m
        print
        print "Public Key = ", n, "\n", "Encoding number 'e' = ", e, "\n", "Private Key = ",d
        print
        return [n, e, d]    


    def get_e(m):
        """Finds an e coprime with m."""
        e = 2
        while gcd(e, m) != 1:
            e += 1
        return e

    def gcd(a,b):
        """Euclid's Algorithm: Takes two integers and returns gcd."""
        while b > 0:
            a, b = b, a % b
        return a

    def get_d(e, m):
        """Takes encoding number, 'e' and the value for 'm' (p-1) * (q-1).
        Returns a decoding number."""
        x = lasty = 0 
        lastx = y = 1
        while m != 0: 
            q = e // m 
            e, m = m, e % m 
            x, lastx = lastx - q*x, x
            y, lasty = lasty - q*y, y
        return lastx

    if __name__ == "__main__":
        main()


def serverpage():
    os.startfile('TestServer.py')


def clientpage():
    os.startfile('TestClient.py')
    
# setting up the menu bar 
link=Label(master1, text="About",fg='#F5F5F5',font=("Segoe UI Light", 19),bg='#800000',cursor="arrow")
f = tkFont.Font(link, link.cget("font"))
f.configure(underline = True)
link.configure(font=f)
link.grid(row=4,columnspan=1,sticky=E,padx=15,pady=10)
link.bind("<Button-1>", about)

helpMenu = Menu(menubar)
helpMenu.add_command(label='About Chatbot',underline=0,command=about2)
helpMenu.add_separator()

fileMenu.add_command(label="RSA Settings", underline=0, command=rsa)
fileMenu.add_command(label="Exit", underline=0, command=None)
menubar.add_cascade(label="File", underline=0, menu=fileMenu)
menubar.add_cascade(label="Options", underline=0, menu=fileMenu)
menubar.add_cascade(label="Help", underline=0, menu=helpMenu)



# loading images for homepage
image_dashboard = PIL.Image.open("Server.png")
photo_dashboard = ImageTk.PhotoImage(image_dashboard)

image_status = PIL.Image.open("Client.png")
photo_status = ImageTk.PhotoImage(image_status)



# buttons for the homepage

#ServerButton
B1 = Button(master1, text=None,fg='#3498DB',font=("Segoe UI Semibold", 16),bg='#800000', command=serverpage,height = 80, width = 150,image=photo_dashboard,compound="top",borderwidth=0)
B1.grid(row=1,columnspan=1,sticky=W,padx=110,pady=20)

#ClientButton
B2 = Button(master1, text=None,fg='#3498DB',font=("Segoe UI Semibold", 16),bg='#800000', command=clientpage,height = 80, width = 200,image=photo_status,compound="top",borderwidth=0)
B2.grid(row=3,columnspan=1,sticky=W,padx=71,pady=40)
mainloop()
