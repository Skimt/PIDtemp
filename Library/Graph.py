import matplotlib.pyplot as mpl

class Graph:

    """
    Contains all the MatPlotLib garbage. 
    """

    XAxis = []
    YAxis_Temperature = []
    YAxis_Voltage = []
    YAxis_VMax = []
    YAxis_SP = []
    YAxis_EnvTemp = []

    axes1 = () 
    axes2 = ()

    def __init__(self, arrayLength = 1, title = ""):
        
        # Preallocate
        self.XAxis = [0] * arrayLength                 
        self.YAxis_Temperature = [0] * arrayLength 
        self.YAxis_Voltage = [0] * arrayLength 
        self.YAxis_VMax = [0] * arrayLength 
        self.YAxis_SP = [0] * arrayLength 
        self.YAxis_EnvTemp = [0] * arrayLength 

        figure = mpl.figure()
        self.axes1 = figure.subplots()

        self.axes1.set_title(title)
        self.axes1.set(xlabel = "Time [s]")
        self.axes1.set_ylabel("Temperature [deg C]", color = "#2e7de8")
        self.axes1.grid()
        self.axes2 = self.axes1.twinx()
        self.axes2.set_ylabel("Control Signal [V]", color = "#e44d98")

        #self.axes1.set_xlim(0, 150)
        #self.axes2.set_xlim(0, 150)
        #self.axes1.set_ylim(20, 34)
        #self.axes2.set_ylim(0, 6)

    def SetTitle(self, title):
        self.axes1.set_title(title)

    def Display(self):

        self.axes1.plot(self.XAxis, self.YAxis_Temperature, color = "#73a8f0")
        self.axes2.plot(self.XAxis, self.YAxis_Voltage, color = "#e44d98", linewidth = 1)
        self.axes1.plot(self.XAxis, self.YAxis_SP, color = "darkred", linewidth = 1)
        #self.axes1.legend(labels = ("Temp", "SP"))
        mpl.show()