#include<stdio.h>
#include<stdlib.h>

void helper(int, int*, int, int *);

int countArrangement(int N) {
    int *nums = (int*) malloc(sizeof(int)*(N+1));
    int i, count = 0, cur_index = 1;
    for(i = 1; i <= N; ++i) {
        nums[i] = i;
    }
    
    helper(N, nums, cur_index, &count);
    return count;
}

void swap(int *a, int *b) {
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

void helper(int N, int *nums, int index, int *count) {
    int i;
    if (index == N+1) {
        *count += 1;
    }else {
        for(i = index; i <= N; ++i) {
            swap(&nums[i], &nums[index]);
            if ( (index % nums[index] == 0) || (nums[index] % (index) == 0) ) {
                helper(N, nums, index+1, count);
            }
            swap(&nums[i], &nums[index]);
        }
    }
}

int main()
{
	printf("%d\n",countArrangement(15));
	return 0;
}
