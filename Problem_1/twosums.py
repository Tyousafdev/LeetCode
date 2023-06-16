#GIVEN VALUES
nums = [2,5,6,7]
target = [11]


array_limit = 0
two_sum = ["[0], [1]"]


current_number = nums[0]
num_in_list = []

#changed temp = -->
num_in_list.append(nums)


index1 = []
index2 = []

temp_var = []
# temp solution// take out current number from the  list the do current number + 
# every other elements excpet the one that was taken out
def TwoSum():
        
        #make function to add chosen index and add it to the rest of the numbers in the
        for i in nums:
                temp_add = current_number + i
                if temp_add == target[0]:
                        print("<<", num_in_list[0][0],"+", i, "=", temp_add,">>")
                        firstnumber = index1.append(num_in_list[0][0])
                        secNumber = index2.append(i)
                        
                        temp_var.append(index2)
                        

                        if index1[0] in nums:
                                index_param1 = nums.index(index1[0])
                                print("Index of", index1[0], "is", index_param1)
                                

                        if temp_var[0][0] in nums:
                                index_param2 = nums.index(temp_var[0][0])
                                print("Index of", temp_var[0][0], "is", index_param2)

                        #therefore 
                        print(num_in_list)
                        print(f"Output: [{index_param1}, {index_param2}]")
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
            

