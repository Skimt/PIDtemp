class Pipe:

    """
    The Pipe class object is a component of the Heater
    class object, wherein its purpose is to delay the PV. 
    """

    temperatures = list()
    temperature = 0             # [deg C]
    delayDt = 0                 # [sec]

    def __init__(self, delayDt = 0):

        self.delayDt = delayDt

    def Input(self, temperature):

        # There is no delay
        if self.delayDt == 0:
            self.temperature = temperature
            return

        # Delay the value
        self.temperatures.insert(0, temperature)

    def GetOutput(self):

        # There is no delay
        if self.delayDt == 0:
            return self.temperature
        
        # Get the delayed value
        if len(self.temperatures) > self.delayDt:
            self.temperature = self.temperatures[-1]
            self.temperatures.pop()
        
        return self.temperature