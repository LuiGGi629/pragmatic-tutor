import datetime
import time
import concurrent.futures

import colorama


def main():
    t0 = datetime.datetime.now()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = executor.map(do_smth, secs)
        for res in results:
            print(res)
        # results = [executor.submit(do_smth, sec) for sec in secs]
        #
        # for f in concurrent.futures.as_completed(results):
        #     print(f.result())

    # threads = []
    #
    # for _ in range(10):
    #     task = Thread(target=do_smth, args=[1.5], daemon=True)
    #     threads.append(task)
    #
    # [t.start() for t in threads]
    # [t.join() for t in threads]

    dt = datetime.datetime.now() - t0
    print(colorama.Fore.YELLOW + f'total time: {dt.total_seconds():.2f} sec.', flush=True)


def do_smth(seconds):
    print(colorama.Fore.CYAN + f'\nSleep {seconds} sec(s)...')
    time.sleep(seconds)
    return colorama.Fore.RED + f'\nWoke up! after {seconds} sec(s).'


if __name__ == '__main__':
    main()
