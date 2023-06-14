#GIVEN VALUES
number_array = [1,2,3,4]
target = [5]


array_limit = 0
two_sum = ["[0], [1]"]


current_integer = []
num_in_list = []

#changed temp = -->
num_in_list.append(number_array)


index1 = []
index2 = []

1
# temp solution// take out current number from the  list the do current number + 
# every other elements excpet the one that was taken out
def TwoSum():
        global temp
        global number_array
        global target
        global num_in_list
        global temp_add
        global index1
        global index2
        #make function to add chosen index and add it to the rest of the numbers in the
        for i in num_in_list[0]:
                temp_add = num_in_list[0][0] + i
                if temp_add == target[0]:
                        print("<<", num_in_list[0][0],"+", i, "=", temp_add,">>")
                        firstnumber = index1.append(num_in_list[0][0]) 
                        secNumber = index2.append(i)
                        print("INDEX NUMBERS",index1, index2) 
                        break
                        
                      
                print(num_in_list[0][0], "+", i, "=", temp_add)

#make function to add index 
        
        if temp_add != target[0]:
                num_in_list[0][0] += 1
                print("!=",temp_add)
                TwoSum()

TwoSum()

        




















#idaes

#two vars 
# / first var starts with first integer 
# / second var is a list in which the first var goes through every number that was given in the number array

#while two_sum != target:























        #number_array[0] += num_array_len
        #if number_array == target:
        #    print(number_array, "works")
            
        #else:
        #    print(number_array, "not working still")
        #    
        #    break
            

