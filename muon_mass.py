#sulotion to the muon mass challenge in particle physics playground

import pps_tools as pps
import h5hep
import numpy 
import matplotlib.pylab as plt
import math


#data file
pps.download_from_drive('dimuons_1000_collisions.hdf5')

infile = 'data/dimuons_1000_collisions.hdf5'
collisions = pps.get_collisions(infile,experiment='CMS',verbose=False)

number_of_collisions = len(collisions)
print("# number of collisions: %d" % (number_of_collisions))

second_collision = collisions[1]   # the second event
print("First event: ",second_collision)
all_muons = second_collision['muons']    # all of the jets in the first event
print("All muons: ",all_muons)
first_muon = all_muons[0]    # the first jet in the first event
print("First muon: ",first_muon)   
muon_energy = first_muon['e']      # the energy of the first photon
print("First muon's energy: ",muon_energy)

energies = []
momentums = []
masses = []

for collision in collisions:
    
    muons = collision['muons']
    
    for muon in muons:
        energy = muon['e']
        energies.append(energy)

for collision in collisions:
    
    muons = collision['muons']
    
    for muon in muons:
        px = muon['px']
        py = muon['py']
        pz = muon['pz']
        p = math.sqrt(px**2 + py**2 + pz**2)
        momentums.append(energy)

#classical mass of muons
for i in range(len(collisions)):
  masses.append(momentums[i]**2 /energies[i])

#plt.hist(momentums, range=(0,50));
#plt.hist(energies, range=(0,50));
plt.hist(masses)

