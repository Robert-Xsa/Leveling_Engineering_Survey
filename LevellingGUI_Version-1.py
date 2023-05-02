import tkinter
window = tkinter.Tk()
window.resizable(0,0)
window.title("LEVELLING-V1.0")
window["bg"] = "blue"
tkinter.Button(window,text = "BENCHMARK",width =25,command = lambda:BM(BenchMark)).grid(row = 0,column = 0)
BenchMark=tkinter.Entry(window)
BenchMark.grid(row= 0,column= 1)
tkinter.Button(window,text = "CHANGING POINT",width=25,command= lambda:Chan(ChangingPoint)).grid(row=1,column=0)
ChangingPoint = tkinter.Entry(window)
ChangingPoint.grid(row =1,column= 1)
tkinter.Button(window,text="BACKSITE",width = 25,command = lambda:Backsite(BackSite)).grid(row=2,column=0)
BackSite = tkinter.Entry(window)
BackSite.grid(row = 2,column = 1)
tkinter.Button(window,text = "INTERMMEDIATE",width=25,command = lambda:IntermmNum(Intermmediate)).grid(row=3,column=0)
Intermmediate = tkinter.Entry(window)
Intermmediate.grid(row = 3,column = 1)
tkinter.Button(window,text = "INTERMMEDIATE VALUE",width=25,command = lambda:IntermmVa(IntermmediateValue)).grid(row=4,column=0)
IntermmediateValue = tkinter.Entry(window)
IntermmediateValue.grid(row = 4,column = 1)
tkinter.Button(window,text = "FORESITE",width=25,command = lambda:Foresite(ForeSite)).grid(row = 5,column = 0)
ForeSite = tkinter.Entry(window)
ForeSite.grid(row = 5,column = 1)
tkinter.Button(window,text = "OK",width=25,command=lambda:Ok()).grid(row = 6,column = 0)
tkinter.Button(window,text = "SHIFT",width=17,command = lambda:shift(BenchMarkV)).grid(row = 6,column = 1)
global BenchMarkV
def BM(BenchMark):
    global BenchMarkV
    BenchMark = float(BenchMark.get())
    BenchMarkV = BenchMark
    BenchMarkL = tkinter.Label(window,text = "",fg ="red",width = 25)
    BenchMarkL.grid(row = 0,column=2)
    BenchMarkLL = str(BenchMarkV)
    BenchMarkL.config(text = BenchMarkLL)
    #print(BenchMarkV)
def Chan(ChangingPoint):
    global ChangingPointV
    ChangingPoint = int(ChangingPoint.get())
    ChangingPointV = ChangingPoint
    ChangingPointL = tkinter.Label(window,text = "",fg ="red",width=25)
    ChangingPointL.grid(row = 1,column=2)
    ChangingPointLL = str(ChangingPointV)
    ChangingPointL.config(text = ChangingPointLL)
    #print(ChangingPointV)
def Backsite(BackSite):
    global BackSiteV
    BackSite = float(BackSite.get())
    BackSiteV = BackSite
    BackSiteL = tkinter.Label(window,text = "",fg ="red",width=25)
    BackSiteL.grid(row = 2,column=2)
    BackSiteLL = str(BackSiteV)
    BackSiteL.config(text = BackSiteLL)
    #print(BackSiteV)
def IntermmNum(Intermmediate):
    global IntermmediateV
    Intermmediate = int(Intermmediate.get())
    IntermmediateV = Intermmediate
    IntermmediateL = tkinter.Label(window,text = "",fg ="red",width = 25)
    IntermmediateL.grid(row = 3,column=2)
    IntermmediateLL = str(IntermmediateV)
    IntermmediateL.config(text = IntermmediateLL)
    #print(IntermmediateV)
def IntermmVa(IntermmediateValue):
    global IntermmediateValueV
    IntermmediateValue = float(IntermmediateValue.get())
    IntermmediateValueV = IntermmediateValue
    IntermmediateValueL = tkinter.Label(window,text = "",fg ="red",width = 25)
    IntermmediateValueL.grid(row = 4,column=2)
    IntermmediateValueLL = str(IntermmediateValueV)
    IntermmediateValueL.config(text = IntermmediateValueLL)
    #print(IntermmediateValueV)
def Foresite(ForeSite):
    global ForeSiteV
    ForeSite = float(ForeSite.get())
    ForeSiteV = ForeSite
    ForeSiteL = tkinter.Label(window,text = "",fg ="red",width = 25)
    ForeSiteL.grid(row = 5,column=2)
    ForeSiteLL = str(ForeSiteV)
    ForeSiteL.config(text = ForeSiteLL)
    #print(ForeSiteV)
#Processing
def Ok():
    global Value_2
    global BenchMark
    Value = (BenchMarkV) + (BackSiteV)
    if IntermmediateV != 0:
        Value_1 = Value - IntermmediateValueV
        Value_1_L = tkinter.Label(window,text = "",fg ="red",width= 18)
        Value_1_L.grid(row = 7,column=1)
        Value_1_LL = str(Value_1)
        Value_1_L.config(text = Value_1_LL)
        VL = tkinter.Button(window,text = "INTERMMEDIATE REDUCED LEVEL",width = 25).grid(row = 7,column=0)
        #print(Value_1)
    elif IntermmediateV == 0:
        Value_2 = (Value) - (ForeSiteV)
        Value_2 = round(Value_2,3)
        Value_2L = tkinter.Button(window,text= "FORESITE REDUCED LEVEL",width=25).grid(row = 8,column = 0)
        Value_2L = tkinter.Label(window,text = "",fg = "red",width=18)
        Value_2L.grid(row = 8,column= 1)
        Value_2_L = str(Value_2)
        Value_2L.config(text = Value_2_L)
        #print(Value_2)
def shift(BenchMarkV):
    BenchMarkV = Value_2
    #print(BenchMarkV)
    Robert = tkinter.Button(window,text = "NEW BENCHMARK",width = 25).grid(row = 9,column = 0)
    BenchMark_1 = str(BenchMarkV)
    Gembe = tkinter.Label(window,text ="",fg = "red",width = 18)
    Gembe.grid(row=9,column = 1)
    Gembe.config(text = BenchMark_1)
    
window.mainloop()