from cs50 import get_int
height = 0
isValid = False

while isValid == False:
    height = get_int("How high would you like the pyramid? 1-23: ")
    if (height >=0) and (height < 24):
        isValid = True

for i in range(height-1, 0, -1):
    for k in range(i):
        print(" ",end="")
    for j in range(height - i):
        print("#",end="")
    #for mario more uncomment this section
      #  // printf("  ");
       # // for (int j = 0; j < (height - i); j++)
        #// {
        #//     printf("#");
        #// }
    if i != height:
        print()
