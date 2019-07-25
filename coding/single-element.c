int singleNonDuplicate(int* nums, int numsSize) {
    int start = 0;
    int end = numsSize - 1;
    int mid;
    
    while(start <= end) {
        mid = start + (end - start) / 2;
        
        if (mid == 0 || mid == numsSize-1)
            return nums[mid];
        
        if (nums[mid] != nums[mid-1] && nums[mid] != nums[mid+1])
            return nums[mid];
        
        if (mid % 2 == 1) {
            if (nums[mid] != nums[mid-1]) {
                end = mid-1;
            }else {
                start = mid + 1;
            }
        }else {
            if(nums[mid] == nums[mid+1]){
                start = mid + 1;
            }else {
                end = mid - 1;
            }
        }
    }
    return nums[mid];
}
