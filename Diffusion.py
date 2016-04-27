# -*- coding: utf-8 -*-
__author__ = 'v-caearl'

''' Diffusion.py: Builds Module 10.2 (Diffusion) from S&S
#--------1---------2---------3---------4---------5---------6---------7---------8
Shiflet, Angela B.; Shiflet, George W. (2014-03-30). 
    Introduction to Computational Science: Modeling and Simulation for the 
    Sciences (Page 420). Princeton University Press. Kindle Edition. 

    Group Members:
        Alex Ducken
        Branden Livermore
        Charlie Nguyen
        Tyler McBride
    FirstBranch?
'''
import numpy as np
import sys, traceback


# ---- CONSTANTS ----
COLD = 0        #degC
AMBIENT = 25    #degC
HOT = 50        #degC
# ---- CONSTANTS ----

hotSites = [[0,0],[0,1]]
coldSites = [[1,0], [1,1]]
#coldSites = [[0,1],[2,3]]
#coldArr = np.array(coldSites)

def applyHotCold(bar, hotSites, coldSites):
    '''Function to accept a grid of temperatures and to return a grid with 
    heat and cold applied at hotSites and coldSites, respectively
    
    Pre: bar is a grid of values.
    hotSites and coldSites are lists of coordinates inside the grid for hot 
    and cold sites, respectively.
    AMBIENT, HOT, and COLD are global constants, and COLD≤AMBIENT≤HOT.

    Post: A grid of values as described above has been returned.
    '''
    newBar = bar
    
    #assign HOT to every newBar cell with coordinates in hotSites
    hotArr = np.array(hotSites)
    hotX = hotArr[:,0]
    hotY = hotArr[:,1]
    newBar[hotX,hotY] = HOT #prints row first, then column.
    
    #assign COLD to every newBar cell with coordinates in coldSites
    coldArr = np.array(coldSites)
    coldX = coldArr[:,0]
    coldY = coldArr[:,1]
    newBar[coldX,coldY] = COLD #prints row first, then column.    
    return newBar

#abar = np.full((2,3), AMBIENT).astype(int)

#abar = np.arange(6) #-testing
#abar.resize((2,3))
#print applyHotCold(abar, hotSites, coldSites)

def initBar(m,n,hotSites,coldSites):
    '''Function to return an mxn grid of temperatures:
    Cells with coordinates in hotSites have the value HOT; 
    cells with coordinates in coldSites have the value COLD; 
    and all other cells have the value AMBIENT
    ---
    applyHotCold converts these lists into arrays.
    Then slices these arrays back into 2 separate arrays for their x & y coords.
    
    These arrays are inserted into the index of newBar to change each matching value individually -- 
    (hotX[0],hotY[0]), 
    (hotX[1], hotY[1]), ...etc.
    
    The grid is displayed with (0,0) in the top left. 
    ---
    Pre: m and n are positive integers.
    hotSites and coldSites are lists of coordinates for hot and cold sites, 
    respectively.
    AMBIENT, HOT, and COLD are global constants, and COLD≤AMBIENT≤HOT.

    Post: An m × n grid of values as described before has been returned.
    '''
    #←mxn matrix of AMBIENT values
    ambientBar = np.full((m,n), AMBIENT)

    return applyHotCold(ambientBar, hotSites, coldSites)
#print initBar(5, 10, hotSites, coldSites)    

def diffusion(diffusionRate, site, N, NE, E, SE, S, SW, W, NW):
    '''Funciton to return the new temperature of a cell
    '''
    return(1-8*diffusionRate)*site \
            + diffusionRate*(N + NE + E +  SE + S + SW + W + NW)
    
def reflectingLat(lat):
    '''Function to accept a grid and to return a grid extended one cell in 
    each direction with reflecting boundary conditions
    Pre: lat is a grid.
    Post: A grid extended one cell in each direction with reflecting boundary 
    conditions was returned.
    '''
    #latNS← concatenation of first row of lat, lat, and last row of lat
    rowFirst = lat[0,:]
    rowLast = lat[-1,:]
    latNS = np.vstack([rowFirst, lat, rowLast])
    
    #return concatenation of 
    #first column of latNS, latNS, and last column of latNS
    colFirst = latNS[:,0]
    colLast = latNS[:,-1]
    return np.column_stack([colFirst, latNS, colLast])
    

#a = np.array([1,2,3])
#b = np.array([4,5,6])
#tempLat = np.arange(12)
#tempLat.resize(3,4)
#reflectingLat(tempLat)
#print np.concatenate((a,b))
#print np.vstack([a,b])

def diffusionSim(m, n, diffusionRate, t):
    '''Function to return a list of grids in a simulation of the diffusion of heat 
    through a metal bar
    Pre: m and n are positive integers for the number of grid rows and columns, respectively.
    diffusionRate is the rate of diffusion. 
    t is the number of time steps.
    diffusion is a function to return a new temperature for a grid point.
    Post: A list of the initial grid and the grid at each time step of the simulation was returned.
    '''
    #bar←initBar(m, n, hotSites, coldSites)
    #grids← list containing bar
    #do the following t times:
    #barExtended←reflectingLat(bar)
    #bar←applyDiffusionExtended(diffusionRate, barExtended)
    #bar←applyHotCold(bar, hotSites, coldSites)
    #grids← the list with bar appended onto the end of grids
    #return grids



    
