import pps_tools as pps
import h5hep
import matplotlib.pylab as plt
pps.download_from_drive('small_cms_test_file.hdf5')

infile = 'data/small_cms_test_file.hdf5'
collisions = pps.get_collisions(infile,experiment="CMS",verbose=False)

number_of_collisions = len(collisions)
print("number of electron-positron collisions: %d" % (number_of_collisions))

#see details about a certain particle in the collision
print(collisions[0]['muons'])

#see collision in 3d plot
pps.display_collision3D(collisions[0]);



