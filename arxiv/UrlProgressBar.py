from tqdm import tqdm

class UrlProgressBar(object):
    def __init__(self):
        self.pbar = None
        self.downloaded = 0
        
    def __call__(self, block_num, block_size, total_size):
        if self.pbar is None:
            self.pbar = tqdm(range(total_size))

        if self.downloaded + block_size >= total_size:
            self.pbar.update(total_size - self.downloaded)
            self.downloaded = total_size
            self.pbar.close()
        else:
            self.downloaded += block_size
            self.pbar.update(n=block_size)