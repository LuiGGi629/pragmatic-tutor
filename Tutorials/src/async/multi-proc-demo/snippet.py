import concurrent.futures
import datetime
import time
import multiprocessing

import colorama


def main():
    t0 = datetime.datetime.now()

    proc_count = multiprocessing.cpu_count()
    print(colorama.Fore.MAGENTA + f'Working on {proc_count} cores.')

    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = executor.map(do_smth, secs)

        # for res in results:
        #     print(res)

    dt = datetime.datetime.now() - t0
    print(colorama.Fore.YELLOW + f'total time: {dt.total_seconds():.2f} sec.', flush=True)


def do_smth(seconds):
    print(colorama.Fore.CYAN + f'Sleep {seconds} sec...')
    time.sleep(seconds)
    return colorama.Fore.RED + f'Woke up! {seconds}'


if __name__ == '__main__':
    main()
