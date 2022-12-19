import os
import math

PORTFOLIO_IMAGE_DIR = 'app/static/img/portfolio'


def get_portfolio_images():
    portfolio_images = os.listdir(PORTFOLIO_IMAGE_DIR)
    for filename in list(portfolio_images):
        # ignore mac os directory cache files if present
        if '.DS_Store' in filename:
            portfolio_images.remove(filename)
            continue

    if not portfolio_images:
        raise RuntimeError('Unable to load portfolio images, none were supplied in directory!')

    num_rows = math.ceil(len(portfolio_images) / 3)
    images = {}
    curr_row = 0
    curr_idx = 0
    for filename in portfolio_images:
        if curr_idx == 3: # 3 rows total, including zero
            curr_row += 1
            curr_idx = 0
            continue

        row_images = images.setdefault(curr_row, [])
        row_images.append(filename)
        curr_idx += 1

    return (images, num_rows)
