"""
This are some functions that are used in the significance calculator 
and in the significance calculator notebook

The significance is calculated using the Li & Ma formula
___author___ = "Federico Bontempo"
"""

import argparse
import numpy as np
from scipy.stats import norm


def get_args():
    p = argparse.ArgumentParser()
    p.add_argument(
        "-s",
        "--source",
        help="Number of events coming from the source wihtout background",
        default=50,
    )
    p.add_argument(
        "-bg",
        "--background",
        help="Number of background events",
        default=100,
    )
    p.add_argument(
        "-a",
        "--alpha",
        help="Ratio between time on source and time off source",
        default=1.0,
    )
    return p.parse_args()


def check_args(args):
    if (args.source + args.background) < 10:
        Warning("The minimum number of source evants >= 10 according to the paper.")
    if args.background < 10:
        Warning("The minimum number of background >= 10 according to the paper.")
    if (args.alpha > 10.0) or (args.alpha < 0.1):
        Warning("The paper guaraites a test for 0.1 < alpha < 10.0")
    return


def calculate_significance(
    N_on,
    N_off,
    alpha,
):
    """
    The significance is calculated using the Li & Ma formula
    """
    significance = (
        2**0.5
        * (
            N_on * np.log(((1 + alpha) / alpha) * (N_on / (N_on + N_off)))
            + N_off * np.log(((1 + alpha)) * (N_off / (N_on + N_off)))
        )
        ** 0.5
    )
    return significance


def calculate_Gaussian_probability(
    significance,
):
    """
    Calculate the p = N( u = S; 0, 1),
    probabilty of the bg producing the signal
    given the significance and assiuming a normal distribution
    """
    return norm.sf(significance)
