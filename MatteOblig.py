import numpy as np
import matplotlib.pyplot as plt

#Løsning av varmeligningen i to dimensjoner (Oblig Nikolai Nore TMA4121)


lengde = 50 # mm
a = 110
tid = 5 # (i sekund)
p = 50 #Punkter

dx = lengde/p
dy = lengde/p

dt = 0.2*min(dx**2 / (4*a),dy**2/(4*a))

u = np.zeros((p,p)) + 15 #Starttemperatur er 15 grader

#Grenseverdier

u[0, :] = 100
u[-1, :] = 100

#Visualisering
fig, axis = plt.subplots()

pcm = axis.pcolormesh(u, cmap=plt.cm.jet, vmin = 0, vmax = 100)
plt.colorbar(pcm, ax = axis)

#Simulering

Teller = 0

while Teller < tid:
    w = u.copy()

    for i in range(1,p-1):
        for j in range(1,p -1):

            dd_ux = (w[i-1,j] - 2*w[i,j] + w[i+1,j])/dx**2
            dd_uy = (w[i,j-1] - 2*w[i,j] + w[i,j+1])/dy**2

            u[i,j] = dt * a * (dd_ux + dd_uy) + w[i,j]

    Teller +=dt
    #Oppdaterer plot
    pcm.set_array(u)
    axis.set_title("Fordeling på t: {:.3f} [s].".format(Teller))
    plt.pause(0.001)

plt.show()