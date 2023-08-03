import numpy as np

width = 61
height = 21



lCC = (int(width/3) + 1, 8)
rCC = (2 * int(width/3) - 1, 10)




out = np.zeros([height, width])

# Code for printing the tagline
tagline = '< All code welcome! >'
tagline_startcoord = width/2
tstart = int(width/2 - len(tagline)/2)

out[18][tstart:tstart+len(tagline)+1] = range(len(tagline)+1)

print('\n\n')


for j in range(height):

    line = '\t\t'                                                       # initialise a new blank line

    for i in range(width):

        val = out[j][i]                                                 # figure out what I should be plotting

        if abs(5 - ((j - lCC[1])**2 + (i - lCC[0])**2)**0.5) < 1:

            if i < (lCC[0] + 4):

                char = 'C'
            else:
                char = ' '


        elif abs(5 - ((j - rCC[1])**2 + (i - rCC[0])**2)**0.5) < 1:

            if i < (rCC[0] + 4):

                char = 'C'
            else:
                char = ' '

        else:
                
            if val == 0: 
                char = ' '                                                  #print nothing unless it's the border

                if (i == 0) | (i == width-1) | (j == 0) | (j == height-1):  #print the border
                    char = '#'
            else:
                char = tagline[int(val-1)] #if the value of the output is not zero, treat it as indexing the tagline

        line = line + char

    print(f'{line}')



print('\n\n')   