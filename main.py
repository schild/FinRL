import os
from argparse import ArgumentParser

from finrl.apps import config


def build_parser():
    parser = ArgumentParser()
    parser.add_argument(
        "--mode",
        dest="mode",
        help="start mode, train, download_data" " backtest",
        metavar="MODE",
        default="train",
    )
    return parser


def main():
    parser = build_parser()
    options = parser.parse_args()
    if not os.path.exists(f"./{config.DATA_SAVE_DIR}"):
        os.makedirs(f"./{config.DATA_SAVE_DIR}")
    if not os.path.exists(f"./{config.TRAINED_MODEL_DIR}"):
        os.makedirs(f"./{config.TRAINED_MODEL_DIR}")
    if not os.path.exists(f"./{config.TENSORBOARD_LOG_DIR}"):
        os.makedirs(f"./{config.TENSORBOARD_LOG_DIR}")
    if not os.path.exists(f"./{config.RESULTS_DIR}"):
        os.makedirs(f"./{config.RESULTS_DIR}")

    if options.mode == "train":
        import finrl.train

        finrl.train.train_stock_trading()


if __name__ == "__main__":
    main()
