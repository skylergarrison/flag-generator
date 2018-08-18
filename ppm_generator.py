#-------------------------------------------------------------------------------
# Name:        myppmtest
# Purpose:
#
# Author:      Skyler
#
# Created:     16/09/2014
# Copyright:   (c) Skyler 2014
#-------------------------------------------------------------------------------

import ppmimageadt

def main ():
    width = 500
    height = 300
    
    flag = ppmimageadt.PPMImage(width, height)
    
    country = input("(f)rance, (g)ermany, or (l)ithuania?: ")
    
    if country is "g":
        for i in range(width):
            for j in range(height):
                if j < height//3:
                    flag[j, i] = 0, 0, 0  # r, g, b
                elif j < 2*height//3:
                    flag[j, i] = 255, 0, 0
                else:
                    flag[j, i] = 255, 204, 0
        flag.writeToFile("german.ppm")

    elif country is "f":
        for i in range(height):
            for j in range(width):
                if j < width//3:
                    flag[i, j] = 0, 85, 164  # r, g, b
                elif j < 2*width//3:
                    flag[i, j] = 255, 255, 255
                else:
                    flag[i, j] = 250, 60, 50
        flag.writeToFile("france.ppm")

    elif country is "l":
        for i in range(width):
            for j in range(height):
                if j < height//3:
                    flag[j, i] = 253, 185, 19  # r, g, b
                elif j < 2*height//3:
                    flag[j, i] = 0, 106, 68
                else:
                    flag[j, i] = 193, 39, 45
        flag.writeToFile("lithuania.ppm")

main()