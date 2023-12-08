"""
This script calculates the significance of a source given the number of
events coming from the source and the number of background events.
The significance is calculated using the Li & Ma formula.
The probability of the background producing the signal is also calculated
assuming a normal distribution.

The script can be run from the command line as:
    
        python significance_calculator.py -s 50 -bg 100 -a 1.0
    
    where -s is the number of events coming from the source,
    -bg is the number of background events,
    -a is the ratio between time on source and time off source.

__author__ = "Federico Bontempo"
"""


from utils.utils_functions import (
    calculate_significance,
    calculate_Gaussian_probability,
    get_args,
    check_args,
)


def main(args):
    check_args(args)
    significance = calculate_significance(
        N_on=args.source + args.background,
        N_off=args.background,
        alpha=args.alpha,
    )
    gauss_probability = calculate_Gaussian_probability(significance)

    print(
        f"Signal events: {args.source}\n"
        f"Background events: {args.background}\n"
        f"Time on source / Time off source = {args.alpha}\n"
        f"\nSignificance: {significance:.2f}\n"
        f"Gauss probabilty it is background: {gauss_probability:.2e}\n"
        f"Probability it is a source: {(1 - gauss_probability):.2e}\n"
    )
    return


if __name__ == "__main__":
    print("\n===== This scripts estimates the significance of a source =====\n")
    main(args=get_args())
    print("-------------------- Program finished --------------------")
