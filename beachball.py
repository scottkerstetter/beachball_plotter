print("""
BEACHBALL PLOTTER

Version: 1.0
Author: S Kerstetter
Created: 2021-12-15

Creates earthquake focal mechanisms and saves a image file for each individual event.
Required data types (cols):
 - name (or some kind of unique id)
 - strike of nodal plane (0 - 180 degrees)
 - dip of nodal plane (0 - 90 degrees)
 - rake or sense of movement on nodal plane (0 -180 degrees). positive for reverse, negative for normal.
""")

print("loading obspy...")
from obspy.imaging.beachball import beachball
# obspy docs for beachball
# https://docs.obspy.org/packages/autogen/obspy.imaging.beachball.beachball.html#obspy.imaging.beachball.beachball


# **** USER INPUTS ****
# input file with list of required data
# comma separated values only
inputFile = "test_earthquakes.csv"
# directory for output files
saveDir = "C:\\Users\\kerst997\\Documents\\seismology\\focal_mechanisms\\"


# **** START SCRIPT ****
# functions up top, run script on bottom

def read_input_file(inputFile):
# reads input file (csv)
# extracts earthquake names, nodal plane info (strike, dip) and movement direction (rake)
    with open(inputFile) as csv:
        eqList = []
        for row in csv:
            row_items = row.split(',')
            eqDict = {"name":row_items[0],
                      "strike":int(row_items[1]),
                      "dip":int(row_items[2]),
                      "rake":int(row_items[3])
                      }
            eqList.append(eqDict)
    return eqList

def plot_focal_mech(eqDict, saveDir):
# accepts a single earthquake event as arg
# uses obspy 
    np_name = eqDict['name']
    np = [eqDict['strike'], eqDict['dip'], eqDict['rake']]
    figName = f'{np_name}_focal_mech.png'
    # call assign_color to choose which color-fill to use for focal mech plot
    c = assign_color(eqDict['rake'])
    # make a beachball.  link to docs at top
    beachball(np, size=200, linewidth=1, facecolor=c, outfile=saveDir+figName)
    return


def assign_color(val):
# assigns color based on sign and value
    # bool marking whether or not val is between min and max 
    is_between = 45 < abs(val) < 135
    
    if val > 0 and is_between:
        color = 'r'
    elif val < 0 and is_between:
        color = 'b'
    elif not is_between:
        color = 'y'
    else:
        color = 'black'
    
    return color

print("reading input file...")
# initiate script by passing input file
eventList = read_input_file(inputFile)

print("creating focal mechanisms...")
# iterate thru earthquake events to make focal mechs
counter = 0
for event in eventList:
    plot_focal_mech(event, saveDir)
    counter+=1

print(f"created {counter} focal mechanisms.")
print("MISSION COMPLETE")