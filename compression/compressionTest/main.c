//It's been a hot second since I've done anything with C

/*
This should perform exponential compression

*/


#include <stdio.h>
#include <string.h>

void main() {
  //input data
  char str[10];
  char str2num;
  char nums[30];
  
  printf("Enter a value :");
  scanf("%s", str);
  
  //convert to ascii values, combine to single number
  //printf("%s",str);
  
  int i=0;
  while(str[i]) {
    str2num = printf("%d",str[i]);
    //printf("%d\n",str2num);
    sprintf(str2num,"%d",str[i]); //singular char num
    //strcpy(nums,str2num); //append to list
    nums[3*i] = str2num;
    printf("%s\n",nums); //display list as it's appending
    i++; //increment to next char
    //printf("\n");
  }
  
  //calculate summation power values
  
  //compare original vs calculated bit numbers
}