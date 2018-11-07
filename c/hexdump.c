/*
 * cz7asm, 2018
 */

#include <stdio.h>
#include <ctype.h>

void hexdump(const void *src, size_t size)
{
    const unsigned char *src8 = src;
    const int CNT = 16;

    for (size_t i=0; i < size; i++) {
        printf("%02X ", src8[i]);
        int rem = (i+1)%CNT;
        if ((i && !rem) || i+1==size) {
            if (rem)
                for (int j=0; j < rem; j++)
                    printf("   ");
            printf("|");
            for (int j=CNT-rem; j > 0; j--)
                putchar(isprint(src8[i-j])?src8[i-j]:'.');
            printf("|\n");
        }
    }
    putchar('\n');
}
