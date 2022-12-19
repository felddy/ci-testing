#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
    if (argc >= 2 && strcmp(argv[1], "--version") == 0)
    {
        FILE *fp = fopen("image_version.txt", "r");
        if (fp == NULL)
        {
            fprintf(stderr, "Failed to open image_version.txt\n");
            return 1;
        }

        char buf[1024];
        while (fgets(buf, sizeof(buf), fp) != NULL)
        {
            printf("%s", buf);
        }
        fclose(fp);
        return 0;
    }

    sleep(1);

    FILE *fp = fopen("target_platform.txt", "r");
    if (fp == NULL)
    {
        fprintf(stderr, "Failed to open target_platform.txt\n");
        return 1;
    }

    char buf[1024];
    if (fgets(buf, sizeof(buf), fp) != NULL)
    {
        printf("I am running on %s", buf);
    }
    fclose(fp);

    fp = fopen("build_platform.txt", "r");
    if (fp == NULL)
    {
        fprintf(stderr, "Failed to open build_platform.txt\n");
        return 1;
    }

    if (fgets(buf, sizeof(buf), fp) != NULL)
    {
        printf("I was built on %s", buf);
    }
    fclose(fp);

    sleep(1);
    return 0;
}
