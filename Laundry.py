#!/usr/bin/env python
# coding: utf-8

# In[5]:


from tkinter import *
from tkinter import filedialog,messagebox
import random
import time
import requests

def kasir_laundry():

    #Functions
    def reset():
        textReceipt.delete(1.0,END)
        e_berat.set('0')

        e_sprei.set('0')
        e_jas.set('0')
        e_bedcover.set('0')
        e_gaun.set('0')
        e_kostum.set('0')
        e_tas.set('0')
        e_sepatu.set('0')

        e_cuci_saja.set('2000')
        e_cuci_kering.set('2500')
        e_cuci_setrika.set('3000')
        e_setrika_saja.set('3500')

        e_express.set('5000')
        e_sameday.set('3000')
        e_normal.set('0')

        berat.config(state=NORMAL)

        textsprei.config(state=DISABLED)
        textjas.config(state=DISABLED)
        textbedcover.config(state=DISABLED)
        textgaun.config(state=DISABLED)
        textkostum.config(state=DISABLED)
        texttas.config(state=DISABLED)
        textsepatu.config(state=DISABLED)

        textcuci_saja.config(state=DISABLED)
        textcuci_kering.config(state=DISABLED)
        textcuci_setrika.config(state=DISABLED)
        textsetrika_saja.config(state=DISABLED)

        textexpress.config(state=DISABLED)
        textsameday.config(state=DISABLED)
        textnormal.config(state=DISABLED)

        var1.set(0)
        var2.set(0)
        var3.set(0)
        var4.set(0)
        var5.set(0)
        var6.set(0)
        var7.set(0)
        var8.set(0)
        var9.set(2000)
        var10.set(2500)
        var11.set(3000)
        var12.set(3500)
        var13.set(5000)
        var14.set(3000)
        var15.set(0)

        costofitemvar.set('')
        costofpelayananvar.set('')
        costofpenangananvar.set('')
        subtotalvar.set('')
        pajakvar.set('')
        bayarvar.set('')


    def save():
        if textReceipt.get(1.0,END)=='\n':
            pass
        else:
            url=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
            if url==None:
                pass
            else:

                bill_data=textReceipt.get(1.0,END)
                url.write(bill_data)
                url.close()
                messagebox.showinfo('Informasi', 'Nota berhasil disimpan!!')
    def receipt():
        global billnumber, date
        if costofitemvar.get() != '' or costofpelayananvar.get() != '' or costofpenangananvar.get() != '':
            textReceipt.delete(1.0, END)
            x = random.randint(100, 10000)
            billnumber = 'BILL' + str(x)
            date = time.strftime('%d/%m/%Y')
            textReceipt.insert(END, 'Receipt Ref:\t\t' + billnumber + '\t\t' + date + '\n')
            textReceipt.insert(END, '*********************************************************\n')
            textReceipt.insert(END, 'Item:\t\t\t\t Harga Item(Rp)\n')
            textReceipt.insert(END, '*********************************************************\n')

            if e_sprei.get() != '0':
                textReceipt.insert(END, f'Sprei\t\t\t\t\t{int(e_sprei.get()) * 5000}\n\n')

            if e_jas.get() != '0':
                textReceipt.insert(END, f'Jas\t\t\t\t\t{int(e_jas.get()) * 5000}\n\n')

            if e_bedcover.get() != '0':
                textReceipt.insert(END, f'Bedcover\t\t\t\t{int(e_bedcover.get()) * 5000}\n\n')

            if e_gaun.get() != '0':
                textReceipt.insert(END, f'Gaun:\t\t\t\t\t{int(e_gaun.get()) * 5000}\n\n')

            if e_kostum.get() != '0':
                textReceipt.insert(END, f'Kostum:\t\t\t\t{int(e_kostum.get()) * 5000}\n\n')

            if e_tas.get() != '0':
                textReceipt.insert(END, f'Tas:\t\t\t\t\t{int(e_tas.get()) * 5000}\n\n')

            if e_sepatu.get() != '0':
                textReceipt.insert(END, f'Sepatu:\t\t\t\t{int(e_sepatu.get()) * 5000}\n\n')

            textReceipt.insert(END, '*********************************************************\n')
            textReceipt.insert(END, 'Pelayanan:\t\t\t Harga Pelayanan(Rp)\n')
            textReceipt.insert(END, '*********************************************************\n')

            if var9.get() == 1:
                textReceipt.insert(END, f'Cuci Saja:\t\t\t\t{2000}\n\n')

            if var10.get() == 1:
                textReceipt.insert(END, f'Cuci Kering:\t\t\t{2500}\n\n')

            if var11.get() == 1:
                textReceipt.insert(END, f'Cuci Setrika:\t\t\t{3000}\n\n')

            if var12.get() == 1:
                textReceipt.insert(END, f'Setrika Saja:\t\t\t{3500}\n\n')


            textReceipt.insert(END, '********************************************************\n')
            textReceipt.insert(END, 'Penanganan:\t\t\t Harga Penanganan(Rp)\n')
            textReceipt.insert(END, '********************************************************\n')

            if var13.get() == 1:
                textReceipt.insert(END, f'Express:\t\t\t\t{5000}\n\n')

            if var14.get() == 1:
                textReceipt.insert(END, f'Sameday:\t\t\t\t{3000}\n\n')

            if var15.get() == 1:
                textReceipt.insert(END, f'Normal:\t\t\t\t{0}\n\n')

            textReceipt.insert(END, '*******************************************************\n')
            if costofitemvar.get() != 'Rp ':
                textReceipt.insert(END, f'Cost Of Item\t\t\t{costofitemvar.get()}\n\n')
            if costofpelayananvar.get() != 'Rp ':
                textReceipt.insert(END, f'Cost Of Pelayanan\t\t\t{costofpelayananvar.get()}\n\n')
            if costofpenangananvar.get() != 'Rp ':
                textReceipt.insert(END, f'Cost Of Penanganan\t\t{costofpenangananvar.get()}\n\n')

            textReceipt.insert(END, f'Sub Total\t\t\t\t{subtotalvar.get()}\n\n')
            textReceipt.insert(END, f'Pajak Tax\t\t\t\t{pajakvar.get()}\n\n')
            textReceipt.insert(END, f'Total Cost\t\t\t\t{bayarvar.get()}\n\n')
            textReceipt.insert(END, '******************************************************\n')

        else:
            messagebox.showerror('Error', 'Tidak ada item yang dipilih')

    def totalcost():
        global  priceofBerat, priceofItem, priceofPelayanan, priceofPenanganan, subtotalofItems

        if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or             var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or             var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0:

            item1 = float(e_berat.get())
            item2 = int(e_sprei.get())
            item3 = int(e_jas.get())
            item4 = int(e_bedcover.get())
            item5 = int(e_gaun.get())
            item6 = int(e_kostum.get())
            item7 = int(e_tas.get())
            item8 = int(e_sepatu.get())

            item9 = int(e_cuci_saja.get())
            item10 = int(e_cuci_kering.get())
            item11 = int(e_cuci_setrika.get())
            item12 = int(e_setrika_saja.get())

            item13 = int(e_express.get())
            item14 = int(e_sameday.get())
            item15 = int(e_normal.get())

            priceofBerat=item1*5000

            priceofItem=(item2*5000)+(item3*5000)+(item4*5000)+(item5*5000) + (item6 * 5000) + (item7 * 5000) +(item8 * 5000)


            priceofPelayanan = 0
            if var9.get() == 1:
                priceofPelayanan = item9
            if var10.get() == 1:
                priceofPelayanan = item10
            if var11.get() == 1:
                priceofPelayanan = item11
            if var12.get() == 1:
                priceofPelayanan = item12


            priceofPenanganan=0
            if var13.get() == 1:
                priceofPenanganan = item13
            if var14.get() == 1:
                priceofPenanganan = item14
            if var15.get() == 1:
                priceofPenanganan = item15

            costofitemvar.set('Rp ' + str(priceofItem))
            costofpelayananvar.set('Rp ' + str(priceofPelayanan))
            costofpenangananvar.set('Rp ' + str(priceofPenanganan))

            subtotalofItems = priceofBerat + priceofItem + priceofPelayanan + priceofPenanganan
            subtotalvar.set('Rp ' + str(subtotalofItems))

            pajakvar.set('Rp 500')

            bayarcost = subtotalofItems + 500
            bayarvar.set('Rp ' + str(bayarcost))

        else:
            messagebox.showerror('Error','Tidak ada item yang dipilih!')

    def berat():
        berat.config(state=NORMAL)
        berat.delete(0, END)
        berat.focus()

    def sprei():
        if var2.get()==1:
            textsprei.config(state=NORMAL)
            textsprei.delete(0,END)
            textsprei.focus()
        else:
            textsprei.config(state=DISABLED)
            e_sprei.set('0')

    def jas():
        if var3.get() == 1:
            textjas.config(state=NORMAL)
            textjas.delete(0,END)
            textjas.focus()

        else :
            textjas.config(state=DISABLED)
            e_jas.set('0')

    def bedcover():
        if var4.get()==1:
            textbedcover.config(state=NORMAL)
            textbedcover.delete(0,END)
            textbedcover.focus()

        else:
            textbedcover.config(state=DISABLED)
            e_bedcover.set('0')


    def gaun():
        if var5.get() == 1:
            textgaun.config(state=NORMAL)
            textgaun.focus()
            textgaun.delete(0, END)
        elif var5.get() == 0:
            textgaun.config(state=DISABLED)
            e_gaun.set('0')


    def kostum():
        if var6.get() == 1:
            textkostum.config(state=NORMAL)
            textkostum.focus()
            textkostum.delete(0, END)
        elif var6.get() == 0:
            textkostum.config(state=DISABLED)
            e_kostum.set('0')


    def tas():
        if var7.get() == 1:
            texttas.config(state=NORMAL)
            texttas.focus()
            texttas.delete(0, END)
        elif var7.get() == 0:
            texttas.config(state=DISABLED)
            e_tas.set('0')


    def sepatu():
        if var8.get() == 1:
            textsepatu.config(state=NORMAL)
            textsepatu.focus()
            textsepatu.delete(0, END)
        elif var8.get() == 0:
            textsepatu.config(state=DISABLED)
            e_sepatu.set('0')


    def cuci_saja():
        if var9.get() == 1:
            textcuci_saja.config(state=DISABLED)
            textcuci_saja.focus()
            textcuci_saja.delete(0, END)
        elif var9.get() == 0:
            textcuci_saja.config(state=DISABLED)
            e_cuci_saja.set('0')


    def cuci_kering():
        if var10.get() == 1:
            textcuci_kering.config(state=DISABLED)
            textcuci_kering.focus()
            textcuci_kering.delete(0, END)
        elif var10.get() == 0:
            textcuci_kering.config(state=DISABLED)
            e_cuci_kering.set('0')


    def cuci_setrika():
        if var11.get() == 1:
            textcuci_setrika.config(state=DISABLED)
            textcuci_setrika.focus()
            textcuci_setrika.delete(0, END)
        elif var11.get() == 0:
            textcuci_setrika.config(state=DISABLED)
            e_cuci_setrika.set('0')

    def setrika_saja():
        if var12.get() == 1:
            textsetrika_saja.config(state=DISABLED)
            textsetrika_saja.focus()
            textsetrika_saja.delete(0, END)
        elif var12.get() == 0:
            textsetrika_saja.config(state=DISABLED)
            e_setrika_saja.set('0')

    def express():
        if var13.get() == 1:
            textexpress.config(state=DISABLED)
            textexpress.focus()
            textexpress.delete(0, END)
        elif var13.get() == 0:
            textexpress.config(state=DISABLED)
            e_express.set('0')


    def sameday():
        if var14.get() == 1:
            textsameday.config(state=DISABLED)
            textsameday.focus()
            textsameday.delete(0, END)
        elif var14.get() == 0:
            textsameday.config(state=DISABLED)
            e_sameday.set('0')


    def normal():
        if var15.get() == 1:
            textnormal.config(state=DISABLED)
            textnormal.focus()
            textnormal.delete(0, END)
        elif var15.get() == 0:
            textnormal.config(state=DISABLED)
            e_normal.set('0')




    root=Tk()

    root.geometry('1270x750+0+0')

    root.resizable(0,0)

    root.title('Kasir PickMeL Laundry')

    root.config(bg='firebrick4')

    topFrame=Frame(root,bd=10,relief=RIDGE,bg='firebrick4')
    topFrame.pack(side=TOP)

    labelTitle=Label(topFrame,text='PickMeL Laundry',font=('arial',30,'bold'),fg='yellow',bd=9,
                     bg='red4',width=51)
    labelTitle.grid(row=0,column=0)

    beratFrame=Frame(root,bd=10,relief=RIDGE,bg='firebrick4')
    beratFrame.pack(side=TOP)


    #frames

    menuFrame=Frame(root,bd=10,relief=RIDGE,bg='firebrick4')
    menuFrame.pack(side=LEFT)

    costFrame=Frame(menuFrame,bd=4,relief=RIDGE,bg='firebrick4',pady=10)
    costFrame.pack(side=BOTTOM)

    itemFrame=LabelFrame(menuFrame,text='Item Tambahan',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4',)
    itemFrame.pack(side=LEFT)

    pelayananFrame=LabelFrame(menuFrame,text='Pelayanan',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4')
    pelayananFrame.pack(side=LEFT)

    penangananFrame=LabelFrame(menuFrame,text='Penanganan',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4')
    penangananFrame.pack(side=LEFT)

    rightFrame=Frame(root,bd=15,relief=RIDGE,bg='red4')
    rightFrame.pack(side=RIGHT)

    calculatorFrame=Frame(rightFrame,bd=1,relief=RIDGE,bg='red4')
    calculatorFrame.pack()

    recieptFrame=Frame(rightFrame,bd=4,relief=RIDGE,bg='red4')
    recieptFrame.pack()

    buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE,bg='red4')
    buttonFrame.pack()

    #Variables

    var1=IntVar()
    var2=IntVar()
    var3=IntVar()
    var4=IntVar()
    var5 = IntVar()
    var6 = IntVar()
    var7 = IntVar()
    var8 = IntVar()
    var9 = IntVar()
    var10 = IntVar()
    var11 = IntVar()
    var12 = IntVar()
    var13 = IntVar()
    var14 = IntVar()
    var15 = IntVar()


    e_berat=StringVar()

    e_sprei=StringVar()
    e_jas = StringVar()
    e_bedcover=StringVar()
    e_gaun = StringVar()
    e_kostum = StringVar()
    e_tas = StringVar()
    e_sepatu = StringVar()

    e_cuci_saja=StringVar()
    e_cuci_kering = StringVar()
    e_cuci_setrika= StringVar()
    e_setrika_saja = StringVar()


    e_express=StringVar()
    e_sameday = StringVar()
    e_normal = StringVar()

    costofitem=StringVar()
    costofpelayanan=StringVar()
    costofpenanganan=StringVar()
    subtotalvar=StringVar()
    pajakvar=StringVar()
    bayarvar=StringVar()

    e_berat.set('0')

    e_sprei.set('0')
    e_jas.set('0')
    e_bedcover.set('0')
    e_gaun.set('0')
    e_kostum.set('0')
    e_tas.set('0')
    e_sepatu.set('0')

    e_cuci_saja.set('2000')
    e_cuci_kering.set('2500')
    e_cuci_setrika.set('3000')
    e_setrika_saja.set('3500')

    e_express.set('5000')
    e_sameday.set('3000')
    e_normal.set('0')

    ##berat
    berat = Label(beratFrame, text='Berat/kg', font=('arial', 17, 'bold'), fg='white', bd=9,
                  bg='red4', width=10)
    berat.grid(row=2, column=0)

    ##item

    sprei=Checkbutton(itemFrame,text='Sprei',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var2
                     ,command=sprei)
    sprei.grid(row=0,column=0,sticky=W)

    jas=Checkbutton(itemFrame,text='Jas',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var3
                     ,command=jas)
    jas.grid(row=1,column=0,sticky=W)

    bedcover=Checkbutton(itemFrame,text='Bed Cover',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var4
                     ,command=bedcover)
    bedcover.grid(row=2,column=0,sticky=W)

    gaun=Checkbutton(itemFrame,text='Gaun',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var5
                      ,command=gaun)
    gaun.grid(row=3,column=0,sticky=W)

    kostum=Checkbutton(itemFrame,text='Kostum',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var6
                      ,command=kostum)
    kostum.grid(row=4,column=0,sticky=W)

    tas=Checkbutton(itemFrame,text='Tas',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var7
                      ,command=tas)
    tas.grid(row=5,column=0,sticky=W)

    sepatu=Checkbutton(itemFrame,text='Sepatu',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var8
                       ,command=sepatu)
    sepatu.grid(row=6,column=0,sticky=W)

    #Entry  berat
    berat=Entry(beratFrame,font=('arial',18,'bold'),bd=7,width=14,textvariable=e_berat)
    berat.grid(row=2,column=2)

    #Entry Fields for Items

    textsprei=Entry(itemFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_sprei)
    textsprei.grid(row=0,column=1)

    textjas=Entry(itemFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_jas)
    textjas.grid(row=1,column=1)

    textbedcover=Entry(itemFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_bedcover)
    textbedcover.grid(row=2,column=1)

    textgaun = Entry(itemFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_gaun)
    textgaun.grid(row=3, column=1)

    textkostum = Entry(itemFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_kostum)
    textkostum.grid(row=4, column=1)

    texttas= Entry(itemFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_tas)
    texttas.grid(row=5, column=1)

    textsepatu= Entry(itemFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_sepatu)
    textsepatu.grid(row=6, column=1)


    #Pelayanan
    cuci_saja=Checkbutton(pelayananFrame,text='Cuci Saja',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var9
                      ,command=cuci_saja)
    cuci_saja.grid(row=0,column=0,sticky=W)

    cuci_kering=Checkbutton(pelayananFrame,text='Cuci Kering',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var10
                       ,command=cuci_kering)
    cuci_kering.grid(row=1,column=0,sticky=W)

    cuci_setrika=Checkbutton(pelayananFrame,text='Cuci Setrika',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var11
                       ,command=cuci_setrika)
    cuci_setrika.grid(row=2,column=0,sticky=W)

    setrika_saja=Checkbutton(pelayananFrame,text='Setrika Saja',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var12
                         ,command=setrika_saja)
    setrika_saja.grid(row=3,column=0,sticky=W)

    saja=Label(pelayananFrame,text=' ',font=('arial',26,'bold'))
    saja.grid(row=4,column=0,sticky=W)

    saja1=Label(pelayananFrame,text=' ',font=('arial',26,'bold'))
    saja1.grid(row=5,column=0,sticky=W)

    saja2=Label(pelayananFrame,text=' ',font=('arial',26,'bold'))
    saja2.grid(row=6,column=0,sticky=W)

    #entry fields for pelayanan

    textcuci_saja= Entry(pelayananFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_cuci_saja)
    textcuci_saja.grid(row=0, column=1)

    textcuci_kering = Entry(pelayananFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_cuci_kering)
    textcuci_kering.grid(row=1, column=1)

    textcuci_setrika= Entry(pelayananFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_cuci_setrika)
    textcuci_setrika.grid(row=2, column=1)

    textsetrika_saja = Entry(pelayananFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_setrika_saja)
    textsetrika_saja.grid(row=3, column=1)


    #Penanganan

    express=Checkbutton(penangananFrame,text='Express',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var13
                         ,command=express)
    express.grid(row=0,column=0,sticky=W)

    sameday=Checkbutton(penangananFrame,text='Sameday',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var14
                          ,command=sameday)
    sameday.grid(row=1,column=0,sticky=W)

    normal=Checkbutton(penangananFrame,text='Normal',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var15
                           ,command=normal)
    normal.grid(row=2,column=0,sticky=W)

    saja=Label(penangananFrame,text=' ',font=('arial',26,'bold'))
    saja.grid(row=3,column=0,sticky=W)

    saja1=Label(penangananFrame,text=' ',font=('arial',26,'bold'))
    saja1.grid(row=4,column=0,sticky=W)

    saja2=Label(penangananFrame,text=' ',font=('arial',26,'bold'))
    saja2.grid(row=5,column=0,sticky=W)

    saja3=Label(penangananFrame,text=' ',font=('arial',26,'bold'))
    saja3.grid(row=6,column=0,sticky=W)

    #entry fields 

    textexpress = Entry(penangananFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_express)
    textexpress.grid(row=0, column=1)

    textsameday = Entry(penangananFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_sameday)
    textsameday.grid(row=1, column=1)

    textnormal = Entry(penangananFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_normal)
    textnormal.grid(row=2, column=1)


    #costlabels & entry fields

    labelCostofItem=Label(costFrame,text='Harga Item',font=('arial',16,'bold'),bg='firebrick4',fg='white')
    labelCostofItem.grid(row=0,column=0)

    costofitemvar = StringVar()  # Define costofitemvar as a StringVar

    textCostofItem = Entry(costFrame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly', textvariable=costofitemvar)
    textCostofItem.grid(row=0, column=1, padx=41)


    labelCostofPelayanan=Label(costFrame,text='Pelayanan',font=('arial',16,'bold'),bg='firebrick4',fg='white')
    labelCostofPelayanan.grid(row=1,column=0)

    costofpelayananvar = StringVar() 
    textCostofPelayanan=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofpelayananvar)
    textCostofPelayanan.grid(row=1,column=1,padx=41)

    labelCostofPenanganan=Label(costFrame,text='Penanganan',font=('arial',16,'bold'),bg='firebrick4',fg='white')
    labelCostofPenanganan.grid(row=2,column=0)

    costofpenangananvar = StringVar() 
    textCostofPenanganan=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofpenangananvar)
    textCostofPenanganan.grid(row=2,column=1,padx=41)

    labelSubTotal=Label(costFrame,text='Total Harga',font=('arial',16,'bold'),bg='firebrick4',fg='white')
    labelSubTotal.grid(row=0,column=2)

    subtotalvar = StringVar() 
    textSubTotal=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=subtotalvar)
    textSubTotal.grid(row=0,column=3,padx=41)

    labelPajak=Label(costFrame,text='Pajak',font=('arial',16,'bold'),bg='firebrick4',fg='white')
    labelPajak.grid(row=1,column=2)

    pajakvar = StringVar() 
    textPajak=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=pajakvar)
    textPajak.grid(row=1,column=3,padx=41)

    labelTotalCost=Label(costFrame,text='Pembayaran',font=('arial',16,'bold'),bg='firebrick4',fg='white')
    labelTotalCost.grid(row=2,column=2)

    bayarvar = StringVar() 
    textTotalCost=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=bayarvar)
    textTotalCost.grid(row=2,column=3,padx=41)

    #Buttons

    buttonTotal=Button(buttonFrame,text='Total',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,
                       command=totalcost)
    buttonTotal.grid(row=0,column=0)

    buttonReceipt=Button(buttonFrame,text='Struk',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5
                         ,command=receipt)
    buttonReceipt.grid(row=0,column=1)

    buttonSave=Button(buttonFrame,text='Simpan',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5
                      ,command=save)
    buttonSave.grid(row=0,column=2)



    buttonReset=Button(buttonFrame,text='Hapus',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,
                       command=reset)
    buttonReset.grid(row=0,column=4)

    #textarea for receipt

    textReceipt=Text(recieptFrame,font=('arial',12,'bold'),bd=3,width=42,height=14)
    textReceipt.grid(row=0,column=0)

    #Calculator
    operator='' #7+9
    def buttonClick(numbers): #9
        global operator
        operator=operator+numbers
        calculatorField.delete(0,END)
        calculatorField.insert(END,operator)

    def clear():
        global operator
        operator=''
        calculatorField.delete(0,END)

    def answer():
        global operator
        result=str(eval(operator))
        calculatorField.delete(0,END)
        calculatorField.insert(0,result)
        operator=''



    calculatorField=Entry(calculatorFrame,font=('arial',16,'bold'),width=32,bd=4)
    calculatorField.grid(row=0,column=0,columnspan=4)

    button7=Button(calculatorFrame,text='7',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,
                   command=lambda:buttonClick('7'))
    button7.grid(row=1,column=0)

    button8=Button(calculatorFrame,text='8',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,
                   command=lambda:buttonClick('8'))
    button8.grid(row=1,column=1)

    button9=Button(calculatorFrame,text='9',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6
                   ,command=lambda:buttonClick('9'))
    button9.grid(row=1,column=2)

    buttonPlus=Button(calculatorFrame,text='+',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6
                      ,command=lambda:buttonClick('+'))
    buttonPlus.grid(row=1,column=3)

    button4=Button(calculatorFrame,text='4',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6
                   ,command=lambda:buttonClick('4'))
    button4.grid(row=2,column=0)

    button5=Button(calculatorFrame,text='5',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6
                   ,command=lambda:buttonClick('5'))
    button5.grid(row=2,column=1)

    button6=Button(calculatorFrame,text='6',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6
                   ,command=lambda:buttonClick('6'))
    button6.grid(row=2,column=2)

    buttonMinus=Button(calculatorFrame,text='-',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6
                       ,command=lambda:buttonClick('-'))
    buttonMinus.grid(row=2,column=3)

    button1=Button(calculatorFrame,text='1',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6
                   ,command=lambda:buttonClick('1'))
    button1.grid(row=3,column=0)

    button2=Button(calculatorFrame,text='2',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6
                   ,command=lambda:buttonClick('2'))
    button2.grid(row=3,column=1)

    button3=Button(calculatorFrame,text='3',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6
                   ,command=lambda:buttonClick('3'))
    button3.grid(row=3,column=2)

    buttonMult=Button(calculatorFrame,text='*',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6
                      ,command=lambda:buttonClick('*'))
    buttonMult.grid(row=3,column=3)

    buttonAns=Button(calculatorFrame,text='=',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,
                     command=answer)
    buttonAns.grid(row=4,column=0)

    buttonClear=Button(calculatorFrame,text='Hapus',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6
                       ,command=clear)
    buttonClear.grid(row=4,column=1)

    button0=Button(calculatorFrame,text='0',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6
                   ,command=lambda:buttonClick('0'))
    button0.grid(row=4,column=2)

    buttonDiv=Button(calculatorFrame,text='/',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,
                     command=lambda:buttonClick('/'))
    buttonDiv.grid(row=4,column=3)

    root.mainloop()
    
if __name__ == '__main__': 
        kasir_laundry()
    


# In[ ]:





# In[ ]:




