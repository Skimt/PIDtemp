from Library.Pipe import Pipe

class Heater:

    """
    The Heater class object is a Process with which to return a PV. 
    It contains the mathematical model for the PV, and a pipe that
    delays said PV. The PV is thus put into and extracted from the Pipe.
    """

    k = 0                   # [deg C / V]
    t = 0                   # [sec]
    EnvTemp = 0     # [deg C]
    temperature = 0         # [deg C]
    voltage = 0             # [V]
    pipe = None

    def __init__(self, envTemp, k, time, delay, deltaTime):
        self.EnvTemp = envTemp
        self.k = k
        self.t = time
        self.pipe = Pipe(delayDt = delay / deltaTime)

    def SetVoltage(self, voltage, dt):
        self.Voltage = voltage
        self.temperature += (self.k * voltage - self.temperature) * dt / self.t
        self.pipe.Input(self.temperature)
    
    def GetTemperature(self):
        return self.EnvTemp + self.pipe.GetOutput()