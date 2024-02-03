# nums = [1,2,3,4,6,7,8,]

# moves = 8 %len(nums)


# for i in range(0,moves):
#     print(f'loop {i+1}')
#     last = nums.pop()
#     nums.insert(0,last)

# print(nums)

# def check_dups():
#     nums = [1,2,3]
#     if nums == list(set(nums)):
#         return True
#     if nums != list(set(nums)): 
#         return False
    
# print(check_dups())

nums = [3,3,5,0,0,3,1,4]
def getttl(nums):
    nums = [3,3,5,0,0,3,1,4]
    largest = [0,0,0] #dif start end
    listallcombos = []
    largestpair = [0,[0,0,0],[0,0,0]]
    largestcombos = []
    count = 0
    for start1 in range(0,len(nums)):
        for end1 in range((start1+1),len(nums)):
            startval = nums[start1]
            endval = nums[end1]
            diff = (endval - startval)
            if diff > largest[0]:
                largest = [diff,start1,end1]
                #print(largest)
            if diff > 0 :
                listallcombos.append([diff,start1,end1])

    def checklargestcombo(largest,g1,g2):
        if (g1[0] + g2[0]) > largest[0]:
            return True
        return False

    def checkifin(g1,g2):
        rng = []
        for i in range(g1[1],g1[2]+1):
            rng.append(i)

        if g2[1] or g2[2]in rng:
            #print(g2,rng)
            return False
        return True

    def ranges_overlap(range1, range2):
        # Unpack the start and end values for each range
        start1 = range1[1]
        end1 = range1[2]
        start2 = range2[1]
        end2 = range2[2]

        # Check for overlap
        if end1 < start2 or end2 < start1:
            return False
        else:
            return True

    for grp1 in range(0,len(listallcombos)):
        for grp2 in range((grp1+1),len(listallcombos)):
            g1 = listallcombos[grp1]
            g2 = listallcombos[grp2]
            grpsum = g1[0] + g2[0]
            if checklargestcombo(largest,g1,g2) == True and ranges_overlap(g1,g2) == False and grpsum > largestpair[0]:
                largestpair = [grpsum,g1,g2]
                
            #checkifin(g1,g2)         

    if largestpair[0] > largest[0]:
        return largestpair[0]
    return largest

print(getttl(nums))


#print(listallcombos)


# #for i in listallcombos:
# def checklargestcombo(largest,g1,g2):
#     if (g1[0] + g2[0]) > largest[0]:
#         return True

# def checkifin(g1,g2):
#     rng = []
#     for i in range(g1[1],g1[2]+1):
#         rng.append(i)

#     if g2[1] or g2[2] in rng:
#         return False
#     return True

# for grp1 in range(0,len(listallcombos)):
#     for grp2 in range((grp1+1),len(listallcombos)):
#         g1 = listallcombos[grp1]
#         g2 = listallcombos[grp2]
#         if checklargestcombo(largest,g1,g2) and checkifin(g1,g2) and g1[0] + g2[0] > largestpair:
#             largestpair = [(g1[0] + g2[0]), g1,g2]
            




#print(largestpair)

