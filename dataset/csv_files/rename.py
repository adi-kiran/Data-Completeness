# import os
# location = '/Users/chirag.tubakad/Documents/Projects/Data-Completeness-/dataset/csv_files/temp'

import os 
  
# Function to rename multiple files 
def main(): 
    i = 1109
      
    for filename in os.listdir("/Users/chirag.tubakad/Documents/Projects/Data-Completeness-/dataset/csv_files/204/"): 
        dst = str(i) + ".csv"
        src ='/Users/chirag.tubakad/Documents/Projects/Data-Completeness-/dataset/csv_files/204/'+ filename 
        dst ='/Users/chirag.tubakad/Documents/Projects/Data-Completeness-/dataset/csv_files/lol/'+ dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
        i += 1
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 