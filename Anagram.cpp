//Solution for https://www.hackerrank.com/challenges/make-it-anagram

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string.h>
using namespace std;


int main() {
   char arr1[10000],arr2[10000];
    int count=0;
    gets(arr1);
    gets(arr2);
    
    for(int i=0;i<strlen(arr1);i++)
        {
        for(int j=0;j<strlen(arr2);j++)
            {
            if((arr1[i]==arr2[j])&&(arr1[i]!='#')&&((arr2[j]!='#')))
                {
                arr1[i]='#';
                arr2[j]='#';
                break;
            }
        }
    }
    for(int i=0;i<max(strlen(arr1),strlen(arr2));i++)
    {
        if(arr1[i]!='#'&& i<strlen(arr1))
            count++;
        if(arr2[i]!='#'&& i<strlen(arr2) )
            count++;
    }
    cout<<count;
    return 0;
}
