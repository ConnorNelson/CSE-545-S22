// gcc -m32 -fno-stack-protector -no-pie -z execstack x.c -o x
// sudo sysctl -w kernel.core_pattern=core
// ulimit -c unlimited

void vuln()
{
    puts("Hello world");

    char buffer[8];
    read(0, buffer, 256);
}

int main()
{
    vuln();
}
