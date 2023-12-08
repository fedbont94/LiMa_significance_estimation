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
