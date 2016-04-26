''' Diffusion.py: Builds Module 10.2 (Diffusion) from S&S
    Group Members:
        Alex Ducken
        Branden Livermore
        Charlie Nguyen
        Tyler McBride
    FirstBranch?
'''

__author__ = 'v-caearl'

def diffusion(diffusionRate, site, N, NE, E, SE, S, SW, W, NW):
    return(1-8*diffusionRate)*site + diffusionRate*(N + NE + E +  SE + S + SW + W + NW)