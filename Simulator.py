# Dependencies
from Library.Graph import Graph
from Library.PIDController import PIDController
from Library.Heater import Heater

# Simulator config
dt = 0.05
start = 0
end = 150
intervals = int((end - start) / dt)

# Process config
heater = Heater(envTemp = 20, k = 3.5, time = 23, delay = 3, deltaTime = dt)

# PID config
PID = PIDController(setPoint = 30, minLimit = 0, maxLimit = 5)
PID.Manual = 2.85 #2.85
PID.Kp = 3.6
PID.Ti = float("inf")
PID.TuneZNPI(11.55)                        # Kpu: 3.6, pu: 11.55
#PID.TuneRZNPI(11.55)                       # Kpu: 3.6, pu: 11.55
#PID.TuneGG(10)                             # Kpgg: 1.5, Tou: 10
PID.TuneSkogestad(0.22 / 1.425, 1, 3)      # Ki=S/U: 0.22 / 1.425 [deg C / V], Tc: 3, Tau: 3

# Graph config
graph = Graph(arrayLength = intervals, title = "ZN PI: Kpu=3.6, pu=11.55")

# Simulation loop
for i in range(start, intervals):

    # Reset SP
    if i > 100 / dt:
        PID.SetPoint = 25

    # Retrieve and regulate temperature
    pv = heater.GetTemperature()
    cv = PID.GetControlVariable(pv, dt)
    heater.SetVoltage(cv, dt)
    
    # Plot values
    graph.XAxis[i] = i * dt
    graph.YAxis_Temperature[i] = pv
    graph.YAxis_Voltage[i] = heater.Voltage
    graph.YAxis_SP[i] = PID.SetPoint

# Display graph
graph.Display()
