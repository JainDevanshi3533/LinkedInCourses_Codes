inputfile = open('values.txt', 'rt')   #read text
outputfile = open('output.txt', 'wt')
sum=0

print('processing the input file')
for line in inputfile :
    print(line.rstrip(), file = outputfile)   #writing each line in the output file
    sum+= int(line)

print("Total sum: ",sum,  file = outputfile )
outputfile.close()
print('Processing Completed')    
