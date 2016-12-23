
import itertools
import time
start_time = time.time()

partnumber = 8

file = input("Please input a file to scan  ",)


with open(file, 'r') as test_file:
    precedence_list = []
    for line in test_file.readline():
        #array = line.strip().encode('utf-8').split(',')
        array = line.strip(',')
        precedence_list.append(array)



if partnumber == 8:
    checktools = ['A','C','A','C','G','G','T','T']

else:
    print ("Error!!")


parts = [ i for i in checktools ]
#parts = [ i for i in range(0,partnumber) ]

DNA_sequences = []



#tool_changes = pplz.calc_tool_changes(sequence)

def calc_tool_changes(sequence):
    tool_changes = 0
    
    current_tool = sequence[0:]
    
    for part in sequence:

        #ind = 8
        #current_tool = checktools[ind]


        if checktools!= current_tool:
            tool_changes += 1
            #current_tool = checktools[0:]
            #ind += 1

    return tool_changes



for i in itertools.permutations(parts):
    sequence = list(i)
    
    DNA_sequences.append(sequence)
    print ("Brute Sequence: " , str(sequence))
        
    print ("The gripper changes: " , str(calc_tool_changes(sequence)))
        
    # break
#print ("Tool gripper changes: " , str(pplz.calc_tool_change(sequence)))
print ("Total sequences  : " , str(len(DNA_sequences)))
print (sequence)
print ("Total Time taken", str(round(time.time() - start_time, 1)),"seconds")

with open("Rogerfinal.txt", "a") as text_file:
    for seq in DNA_sequences:
        text_file.write("Brute Sequence:  %s\n" % str(seq))
        ##text_file.write("Orientation changes:   %s\n" % str(calc_orientation_changes(seq)))
        text_file.write("Tool gripper changes:  %s\n\n" % str(calc_tool_changes(seq)))
    text_file.write("Total sequences:   %s\n" % str(len(DNA_sequences)))
    text_file.write("Total Time taken:  %s" % str(round(time.time() - start_time, 1)))
