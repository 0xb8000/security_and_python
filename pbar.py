from progressbar import ProgressBar
import time

pbar = ProgressBar(maxval=5)
pbar.start()


for i in range(4):
    pbar.update(i)
    time.sleep(1)

pbar.finish()
