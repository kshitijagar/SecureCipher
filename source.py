# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 21:41:43 2022

@author: DELL
"""

from tkinter import *
from tkinter import filedialog
import random
import string
import random
all_letters= string.ascii_letters
def subs_cipher_encrypt(text,all_letters):
    dict1 = {}
    key = 6
    for i in range(len(all_letters)):
        dict1[all_letters[i]] = all_letters[(i+key)%len(all_letters)]
    plain_txt= text
    cipher_txt=[]
    for char in plain_txt:
        if char in all_letters:
            temp = dict1[char]
            cipher_txt.append(temp)
        else:
            temp =char
            cipher_txt.append(temp)        
    cipher_txt= "".join(cipher_txt)
    global c
    c=cipher_txt
    return c
def subs_cipher_decrypt(text,all_letters):
    global c
    key=6
    dict2 = {}    
    for i in range(len(all_letters)):
        dict2[all_letters[i]] = all_letters[(i-key)%(len(all_letters))]
    decrypt_txt = []
    for char in text:
        if char in all_letters:
            temp = dict2[char]
            decrypt_txt.append(temp)
        else:
            temp = char
            decrypt_txt.append(temp)
    decrypt_txt = "".join(decrypt_txt)
    c=decrypt_txt
    return c
key=['a','b','c','d','e','f','g','h','ij','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
random.shuffle(key)
global l
l=key
def vignere_encrypt(s):
    global c
    ke="dkfo"
    ret=''
    space=[]
    for i in s :
       if i==" ":
         space.append(1)
       else:
         space.append(0)
    s="".join(s.split())
    u=[]
    ke=ke.lower()
    for i in s:
      if i.isupper():
         u.append(1)
      if i.islower():
         u.append(0)
    s=s.lower()
    ke=list(ke)
    if len(s)>len(ke): 
      for i in range(len(s)-len(ke)):
         ke.append(ke[i%len(ke)])
    ke="".join(ke)
    for i in range(len(s)):
      if s.islower():
        ret+=chr((ord(ke[i])+ord(s[i])-194)%26+97) 
      elif s==" ":
        ret+=" "
    ret=list(ret)
    for i in range(len(u)):
      if u[i]==1:
        ret[i]=ret[i].upper() 
    for i in range(len(space)):
        if space[i]==1:
          ret.insert(i," ")
    ret=''.join(ret)    
    c=ret
    return c
def vignere_decrypt(s):
    global c
    ret=''
    ke="dkfo"
    space=[]
    for i in s :
       if i==" ":
         space.append(1)
       else:
         space.append(0)
    s="".join(s.split())
    u=[]
    for i in s:
      if i.isupper():
        u.append(1)
      if i.islower():
        u.append(0)
    s=s.lower()
    ke=ke.lower()
    ke=list(ke)
    if len(s)>len(ke):
      for i in range(len(s)-len(ke)):
         ke.append(ke[i%len(ke)])
    ke="".join(ke)
    for i in range(len(s)):
      if s.islower():
        ret+=chr((ord(s[i])-ord(ke[i]))%26+97)
      elif s==" ":
        ret+=" "
    ret=list(ret)
    for i in range(len(u)):
      if u[i]==1:
        ret[i]=ret[i].upper() 
    for i in range(len(space)):
        if space[i]==1:
          ret.insert(i," ")
    ret=''.join(ret) 
    c=ret
    return c


def polybius_square_encrypt(s):
    global c
    key=['a','b','c','d','e','f','g','h','ij','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    random.shuffle(key)
    global l
    l=key
    #to share the key in the encrypted file for decryption
    a=key.index('ij')+1
    c=0
    b=0
    global ci,cj,u,space
    #as uppercase letters have the same value as the lowercase values. i,j have the same values as well
    space=[]
    for i in s :
       if i==" ":
         space.append(1)
       else:
         space.append(0)
    s="".join(s.split())
    ci=[]
    cj=[]
    u=[]
    for i in s:
      if i.isupper():
        u.append(1)
      else:
        u.append(0)
    s=s.lower()  
    u.reverse()
    for i in s:
        if i=='i':
           ci.append(len(s)-s.index(i))
        if i=='j':
           cj.append(len(s)-s.index(i))
    for i in s:
        for j in key:
            if i==j:
                row=(key.index(j)+1)//5+1
                column=(key.index(j)+1)%5
                c=column*10+row
                b=b*100+c
        if i=='i'or i=='j':
                row=a//5+1
                column=a%5
                c=column*10+row
                b=b*100+c
    c=str(b)
    return c
def polybius_square_decrypt(n,key):
    global c
    
    n=int(n)
    s=''
    a=0
    d=1
    for i in u:
          a=n%100
          if i==0:
              if key[(a//10)-1+((a%10)-1)*5]!='ij':
               s+=key[(a//10)-1+((a%10)-1)*5]
               d+=1
              else :
                for a in ci:    
                  if a==d:
                    s+='i'        
                for a in cj:
                  if a==d:
                    s+='j'  
                d+=1   
          if i==1:   
              if key[(a//10)-1+((a%10)-1)*5]!='ij':
               s+=key[(a//10)-1+((a%10)-1)*5].upper()
               d+=1  
              else : 
                for a in ci:    
                  if a==d:
                    s+='I'        
                for a in cj:
                  if a==d:
                    s+='J'  
                d+=1
          n=n//100
          lis=list(s)
          lis.reverse()
          for i in range(len(space)):
              if space[i]==1:
                  lis.insert(i," ")
          ret="".join(lis)
    c=ret      
    return c



#Function for Atbash cypher
def atbash_encrypt(text):
    global c
    c=''
    for i in text:
        if i.isupper():
            c+=chr(25-(ord(i)-65)+65)
        elif i.islower():
            c+=chr(25-(ord(i)-97)+97)
        elif i==" ":
            c+=" "
    return c      
def atbash_decrypt(text):
    global c
    c=''
    for i in text:
        if i.isupper():
            c+=chr(25-(ord(i)-65)+65)
        elif i.islower():
            c+=chr(25-(ord(i)-97)+97)
        elif i==" ":
            c+=" "
    return c    



def ceasar_encrypt(text):
    global c
    c=''
    for i in text:
        if i.isupper():
            c+=chr((ord(i)-65+3)%26+65)
        if i.islower():
            c+=chr((ord(i)-97+3)%26+97)
        if i==" ":
            c+=" "



def ceasar_decrypt(text):
    global c
    c=''

    
    for i in text:
        if i.isupper():
            c+=chr((ord(i)-65-3)%26+65)
        elif i.islower():
            c+=chr((ord(i)-97-3)%26+97)
        elif i==" ":
            c+=" "
    

def file_input():
    global j 
    j=1
    root1.destroy()
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
    
    files=open(filename,"r")
    global text
    text=files.read()
    final(text)
def final(text):  
    global root2
    root2 =Tk() 

    root2.geometry() 

    root2.title("The encryption software") 
    root2.configure(background='black') 

 #   lblTitle=Label(root2,font=('georgia',15,),text='you have selected the file: '+filename,bd=21,bg='black',fg='aqua',justify=CENTER).grid(row=1,column=0,columnspan=3)
    lblTitle=Label(root2,font=('georgia',15,),text='Select the method to proceed with ',bd=21,bg='black',fg='aqua',justify=CENTER).grid(row=2,column=0,columnspan=2)
    clicked = StringVar()
    clicked.set("Ceaser cipher")
    drop=OptionMenu(root2,clicked,"Ceaser cipher","Atbash cipher","Substitution cipher","Vignere cipher","polybias square").grid(row=2,column=2)
    def func():
        optsel=clicked.get()
        print (optsel)
        if w==1:
            if optsel=="Ceaser cipher":
                ceasar_decrypt(text)
            elif optsel=="Atbash cipher":
                atbash_decrypt(text)
            elif optsel=="Substitution cipher":
                subs_cipher_decrypt(text,all_letters)
            elif optsel=="Vignere cipher":
                # global eko
                # eko= Entry(root2,width=50,borderwidth=5)
                # eko.grid(row=5, column=1,)
                # lbr=Label(root2,font=('georgia',15,),text='Key',bd=21,bg='black',fg='aqua',justify=CENTER).grid(row=5,column=0)

                # def submits():
                #     global eko
                #     global ke
                    
                #     ke=str(eko.get()) 
                #     vignere_decrypt(text,ke)
                # btk=Button(root2,padx=15,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=8,text='submit', bg='green',command=submits).grid(row=7,column=1) 
                vignere_decrypt(text)
                
            elif optsel=="polybias square":
                polybius_square_decrypt(text,l)
          
        elif w==2:
            if optsel=="Ceaser cipher":
                ceasar_encrypt(text)
            elif optsel=="Atbash cipher":
                atbash_encrypt(text)
            elif optsel=="Substitution cipher":
                subs_cipher_encrypt(text,all_letters)
            elif optsel=="Vignere cipher":
                # global ekt
                # ekt= Entry(root2,width=50,borderwidth=5)
                # ekt.grid(row=5, column=1,columnspan=2)
                # def submits():
                #     global ekt
                #     global ke
                    
                #     ke=str(ekt.get()) 
                #     print(ke)
                #     vignere_encrypt(text,ke)
                # btk=Button(root2,padx=15,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=8,text='submit', bg='green',command=submits).grid(row=7,column=1) 
                vignere_encrypt(text)
            elif optsel=="polybias square":
                polybius_square_encrypt(text)

        def done():
                root3.destroy()
                c=""
                text=""
                mainf()
             
        def new_window(c):
            global root3
            root2.destroy()
            root1.destroy()
            root3 =Tk() 
            root3.geometry()      
            root3.title("The encryption software") 
            root3.configure(background='black') 
         #   lblTitle=Label(root2,font=('georgia',15,),text='you have selected the file: '+filename,bd=21,bg='black',fg='aqua',justify=CENTER).grid(row=1,column=0,columnspan=3)
            lblTitle1=Label(root3,font=('georgia',15,),text="the output is:",bd=21,bg='black',fg='aqua',justify=CENTER).pack()
           
            
            lblTitle=Label(root3,font=('georgia',15,),text=c,bd=21,bg='black',fg='aqua',justify=CENTER).pack()
            bte4=Button(root3,padx=15,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=8,text='Done', bg='green',command=done).pack()
 
        def new_windows(optsel,c):
            o=random.randint(100000, 1000000)
            o=str(o)
            filen=optsel+"_"+o+".txt"
            file=open(filen,"w")
            file.write(c)
            file.close()
            
            global root3
            root2.destroy()
            root3 =Tk() 
            root3.geometry()      
            root3.title("The encryption software") 
            root3.configure(background='black') 
         #   lblTitle=Label(root2,font=('georgia',15,),text='you have selected the file: '+filename,bd=21,bg='black',fg='aqua',justify=CENTER).grid(row=1,column=0,columnspan=3)
            lblTitle1=Label(root3,font=('georgia',15,),text="the output is saved as:",bd=21,bg='black',fg='aqua',justify=CENTER).pack()
           
            lblTitle=Label(root3,font=('georgia',15,),text=filen,bd=21,bg='black',fg='aqua',justify=CENTER).pack()
            bte4=Button(root3,padx=15,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=8,text='Done', bg='green',command=done).pack()
 
        if j==1:
            new_windows(optsel,c)
    
    
    
        if j==2:
            new_window(c)    
       
    if w==2:
        bte=Button(root2,padx=15,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=8,text='encrypt', bg='green',command=func).grid(row=3,column=1,) 
    elif w==1:
        bte=Button(root2,padx=15,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=8,text='decrypt', bg='green',command=func).grid(row=3,column=1,) 

def text_input():
    global eki
    global j
    j=2
    blank1=Label(root1,font=('georgia',15,),text='   ',bd=21,bg='black',fg='aqua',justify=CENTER).grid(row=4,column=0,columnspan=3)
    eki= Entry(root1,width=50,borderwidth=5)
    eki.grid(row=5, column=0,columnspan=3)    
    blank=Label(root1,font=('georgia',15,),text='   ',bd=21,bg='black',fg='aqua',justify=CENTER).grid(row=6,column=0,columnspan=3)
    def submit():
        global eki
        global text
        print()
        tex = eki.get()
        text=str(tex)
        print(text)
        final(text)        
    btk=Button(root1,padx=15,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=8,text='submit', bg='green',command=submit).grid(row=7,column=1) 



def encrypt_file():
    root.destroy()
    global w
    w=2
    global root1
    root1 =Tk() 
    root1.geometry() 
    root1.title("The encryption software") 
    root1.configure(background='black') 
    lblTitle=Label(root1,font=('georgia',40,'bold'),text='ENCRYPT',bd=21,bg='black',fg='aqua',justify=CENTER).grid(row=0,column=0,columnspan=3)
    lblTitle=Label(root1,font=('georgia',15,),text='Select which form of input do you want to give',bd=21,bg='black',fg='aqua',justify=CENTER).grid(row=1,column=0,columnspan=3)
    bte=Button(root1,padx=15,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=8,text='file', bg='green',command=file_input).grid(row=3,column=0) 
    btd=Button(root1,padx=15,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=8,text='text', bg='green',command=text_input).grid(row=3,column=2 )



def decrypt_file():
    root.destroy()
    global w
    w=1
    global root1
    root1 =Tk() 
    root1.geometry() 
    root1.title("The encryption software") 
    root1.configure(background='black') 
    lblTitle=Label(root1,font=('georgia',40,'bold'),text='DECRYPT',bd=21,bg='black',fg='aqua',justify=CENTER).grid(row=0,column=0,columnspan=3)
    lblTitle=Label(root1,font=('georgia',15,),text='Select which form of input do you want to give',bd=21,bg='black',fg='aqua',justify=CENTER).grid(row=1,column=0,columnspan=3)
    bte=Button(root1,padx=15,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=8,text='file', bg='green',command=file_input).grid(row=3,column=0) 
    btd=Button(root1,padx=15,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=8,text='text', bg='green',command=text_input).grid(row=3,column=2 )

def mainf():
    global root
    root =Tk() 
    root.geometry() 
    root.title("CryptoCypher") 
    root.configure(background='black') 
    lblTitle=Label(root,font=('georgia',40,'bold'),text='CryptoCypher',bd=21,bg='black',fg='aqua',justify=CENTER).grid(row=1,column=0,columnspan=3)
    bte=Button(root,padx=15,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=8,text='Encrypt', bg='green',command=encrypt_file).grid(row=3,column=0) 
    btd=Button(root,padx=15,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=8,text='Decrypt', bg='green',command=decrypt_file).grid(row=3,column=2 )
    root.mainloop()
mainf()