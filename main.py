#Function to classify batteries by charge cycles

def count_batteries_by_usage(cycles):
    lowCount=0
    mediumCount=0
    highCount=0
    #Checking for valid input
    if isinstance(cycles, list):
        for i in range(len(cycles)):
            if cycles[i]<400:
                lowCount+=1
            if 400<=cycles[i] and cycles[i]<=919:
                mediumCount+=1
            if cycles[i]>=920:
                highCount+=1
    else:
        print("Invalid datatype")
    #return the values in the form of a dictionary
    return {
        "lowCount": lowCount,
        "mediumCount": mediumCount,
        "highCount": highCount
    }

def test_bucketing_by_number_of_cycles():
    print("Counting batteries by usage cycles...\n")
    counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
    #testing for the above case...
    assert(counts["lowCount"] == 2)
    assert(counts["mediumCount"] == 3)
    assert(counts["highCount"] == 1)
    print("Done counting :)")
    print(counts)

if __name__ == '__main__':
    test_bucketing_by_number_of_cycles()
