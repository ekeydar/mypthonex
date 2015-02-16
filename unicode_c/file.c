#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char* subrange(char* src,int from,int to) {
  char* result = calloc(1,to-from+10);
  int i=0;
  int j=0;
  for (i=from ; i < to ; i++) {
    result[j] = src[i];
    j++;
  }
  return result;
}

int main() {
  char* text = "RT @FootyQuandary: Robinho, not the sharpest tool in the shed! \xf0\x9f\x98\x84\xf0\x9f\x98\x84 http://t.co/MdYpLTWhef";
  printf("text=%s\n",text);
  printf("strlen=%lu\n",strlen(text));
  printf("subrange(text,3,17)=%s\n",subrange(text,3,17));
  printf("subrange(text,66,88)=%s\n",subrange(text,66,88));
  return 0;
}


/*




 */
