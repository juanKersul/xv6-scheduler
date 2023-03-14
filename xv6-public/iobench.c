#include "types.h"
#include "stat.h"
#include "user.h"
#include "fs.h"
#include "fcntl.h"

#define OPSIZE 16
#define TIMES 32
#define MINTICKS 250

static char path[] = "12iops";
static char data[OPSIZE];

int
main(int argc, char *argv[])
{
  int rfd, wfd;
  int pid = getpid();
  int i;

  path[0] = '0' + (pid / 10);
  path[1] = '0' + (pid % 10);

  memset(data, 'a', sizeof(data));

  int j = 0;
  int start = uptime();
  int ops = 0;
  for(;;) {
    int end = uptime();
    int elapsed = end - start;
    if (elapsed >= MINTICKS) {
        if(j<50){
          printf(1, "\t%d: %d IOP%dT,i=%d\n", pid, (int) (ops * MINTICKS / elapsed), MINTICKS,j);
          j++;
          start = end;
          ops = 0;
        }
    }

    wfd = open(path, O_CREATE | O_WRONLY);
    rfd = open(path, O_RDONLY);

    for(i = 0; i < TIMES; ++i) {
      write(wfd, data, OPSIZE);
    }
    for(i = 0; i < TIMES; ++i) {
      read(rfd, data, OPSIZE);
    }
    close(wfd);
    close(rfd);
    ops += 2 * TIMES;
  }

  exit();
  return 0;
}

