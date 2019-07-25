
#include <stdio.h>
#include <string.h>

void reverse(char *s, int start, int end){
   char tmp;
    while(start < end) {
        tmp = s[start];
        s[start] = s[end];
        s[end] = tmp;
        start++;
        end--;
    }
}

void reverseWords(char *s) {
    int start = 0;
    int end = strlen(s) - 1;
    int index = 0, i;
	int new_start = 0;

	if (strlen(s) <= 1)
		return;

    reverse(s, start, end);
    for(i = 0; i < strlen(s); i++){
        if (s[i] != ' ') {
            if (index != 0)
                s[index++] = ' ';
            
			new_start = index;
			start = i;
			end = i;
            while(s[end] != '\0' && s[end] != ' ')
				end++;
			
			while(start < end) 
				s[index++] = s[start++];
			
            reverse(s, new_start, index-1);
			i = end;
        }
    }
	s[index] = '\0';
}

int main() {
	char s[100];

	strcpy(s,"");
	printf("%s\n",s);
	reverseWords(s);
	printf("%s\n", s);

	strcpy(s,"T");
	printf("%s\n",s);
	reverseWords(s);
	printf("%s\n", s);

	strcpy(s,"The sky is blue");
	printf("%s\n",s);
	reverseWords(s);
	printf("%s\n", s);
	
	strcpy(s,"   The sky is blue");
	printf("%s\n",s);
	reverseWords(s);
	printf("%s\n", s);

	strcpy(s,"The sky is blue     ");
	printf("%s\n",s);
	reverseWords(s);
	printf("%s\n", s);

	strcpy(s,"The    sky    is     blue");
	printf("%s\n",s);
	reverseWords(s);
	printf("%s\n", s);

	strcpy(s,"   one.   +two three?   ~four   !five- ");
//	strcpy(s,"   one.   +two ");
	printf("%s\n", s);
	reverseWords(s);
	printf("%s\n", s);
	return 0;
}
