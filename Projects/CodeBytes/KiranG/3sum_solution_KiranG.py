from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()  # Step 1: Sort the array to handle duplicates easily
    result = []
    n = len(nums)
    #print(n)
    
    for i in range(n - 2):  # Step 2: Iterate over the array (excluding last two elements)
        if i > 0 and nums[i] == nums[i - 1]:  # Step 3: Skip duplicate values
            continue  # Avoid processing the same number twice as the first element
        
        left, right = i + 1, n - 1  # Step 4: Use two pointers
        #print(left, nums[left])
        #print(right, nums[right])
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            print(total)
            
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])  # Step 5: Store the valid triplet
                left += 1
                right -= 1
                
                # Step 6: Skip duplicate values after finding a triplet
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            
            elif total < 0:
                left += 1  # Increase left pointer to raise sum
            else:
                right -= 1  # Decrease right pointer to lower sum
    
    return result

# Asking for user input
nums = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Running the function
output = threeSum(nums)

# Displaying the output
print("\nInput Array:", nums)
print("Triplets that sum to zero:", output if output else "No valid triplets found")
