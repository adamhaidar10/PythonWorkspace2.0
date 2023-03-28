#include <stdio.h>
#include <string.h>

void mangle(char *, int x);

char coded[][100] = 
{
  "adv adv mpcl nyhtz ibaaly",
  "xwn xwn inax pajvb ljbcna bdpja",
  "hkc gsjsb twjs ufoag dzowb tzcif",
  "vhyhq ilyh judpv fkrfrodwh fklsv"
};

int main()
{
  char decodes[4][26][100];
  char sentence[100];
  int i, j;
  for (j = 0; j < 4; j++)
      for (i = 0; i < 26; i++)
      {
        strcpy(sentence, coded[j]);
        mangle(sentence, i);
        strcpy(decodes[j][i], sentence);
      }
  printf("SOLUTION: %s\n", decodes[0][19]);
  printf("SOLUTION: %s\n", decodes[1][17]);
  printf("SOLUTION: %s\n", decodes[2][12]);
  printf("SOLUTION: %s\n", decodes[3][23]);
  return 0;
}

void mangle(char *str, int offset)
{
  int x;
  char y;
  char curr;
  for (x = 0; x < strlen(str); x++)
  {
      curr = str[x];
      if (curr > 'z' || curr < 'a')
          continue;
      else
      {
          if (str[x] + offset > 'z')
              str[x] = str[x] + offset - 26;
          else
              str[x] = str[x] + offset;
      }

  }
}