#include "stdio.h"
#include "string.h"

void reverse(char *st, char *en){
    char tmp;
    char *start = st;
    char *end = en;
    
    while(start != end) {
        tmp = *start;
        *start = *end;
        *end = tmp;
        start++;
        end--;
    }
}

void reverseWords(char *s) {
    char *start = s;
    char *end = s + strlen(s) - 1;
    
    reverse(start, end);
    printf("%s %s\n", s,__func__);
    end = s;
    start = s;
    while (end){
        while(end && *end != ' ')
            end++;
        reverse(start, end-1);
        start = end;
    }
}

int main(void) {
  char buf[100] = "Hello World";
  printf("%s\n", buf);
  reverseWords(buf);
  printf("%s %s\n",buf, __func__);
  return 0;
}
