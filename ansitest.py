from itertools import cycle
import progressbar
import time
import sys

def esc(code):
    return f'\033[{code}m'

def xprogress(percent=0, width=30):
    left = width * percent // 100
    right = width - left
    print('\r[', '#' * left, ' ' * right, ']',
          f' {percent:.0f}%',
          sep='', end='', flush=True)


def progress(count, total, status='', bar_len=60):
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    fmt = '[%s] %s%s ...%s' % (bar, percents, '%', status)
    print('\b' * len(fmt), end='')  # clears the line
    sys.stdout.write(fmt)
    sys.stdout.flush()



print(esc('31;1;4') + 'really' + esc(0) + ' important')

# def progres(count, total, status='', bar_len=60):
#     filled_len = int(round(bar_len * count / float(total)))

#     percents = round(100.0 * count / float(total), 1)
#     bar = '=' * filled_len + '-' * (bar_len - filled_len)

#     fmt = '[%s] %s%s ...%s' % (bar, percents, '%', status)
#     print('\b' * len(fmt), end='')  # clears the line
#     sys.stdout.write(fmt)
#     sys.stdout.flush()

# for frame in cycle(r'-\|/-\|/'):
#     print('\r', frame, sep='', end='', flush=True)
#     sleep(0.5)

# for i in range(101):
#     progress(i)
#     time.sleep(0.1)

# for i in progressbar.progressbar(range(100), redirect_stdout=True):
#     print('Some text', i)
#     time.sleep(0.2)

# bar = progressbar.ProgressBar(max_value=progressbar.UnknownLength)
# for i in range(20):
#     time.sleep(0.1)
#     bar.update(i)

widgets=[
    ' [', progressbar.Timer(), '] ',
    progressbar.Bar(),
    ' (', progressbar.ETA(), ') ',
]
for i in progressbar.progressbar(range(20), widgets=widgets):
    time.sleep(0.1)

total = 1000
i = 0
while i < total:
    progress(i, total, status='Doing very long job')
    time.sleep(0.5)  # emulating long-playing job
    i += 1
