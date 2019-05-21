
import os 
  
# Function to rename multiple files 
def main():
      
    for filename in os.listdir("/Users/chirag.tubakad/Documents/Projects/temp/204/"): 
        dst = "204_" + filename
        src ='/Users/chirag.tubakad/Documents/Projects/temp/204/'+ filename 
        dst ='/Users/chirag.tubakad/Documents/Projects/temp/CSV_All/'+ dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 