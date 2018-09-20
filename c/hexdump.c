/*
 * cz7asm, 2018
 */

#include <stdio.h>
#include <stddef.h>

void hexdump(const void *src, size_t size)
{
    const unsigned char *src8 = src;
    const int CNT = 16;

    for (size_t i=0; i < size; i++) {
        printf("%02X ", src8[i]);
        if ((i && !((i+1)%CNT))) {
            printf("|");
            for (int j=CNT-1; j >= 0; j--)
                putchar(isprint(src8[i-j])?src8[i-j]:'.');
            printf("|\n");
        }
    }
    putchar('\n');
}
