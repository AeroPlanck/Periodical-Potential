def run_model(model):
        model.run(50000)


if __name__ == "__main__":
    import numpy as np
    from itertools import product
    from main import ThreeBody
    from multiprocessing import Pool


    rangeLambdas = np.concatenate([
        np.arange(0.01, 0.1, 0.02), np.arange(0.1, 1, 0.2)
    ])
    distanceDs = np.concatenate([
        np.arange(0.1, 1, 0.2)
    ])
    rangeGamma = np.concatenate([
        np.arange(1.0, 11.0, 0.1)
    ])
    kappa = [3]
    period = [0.5]

    savePath = "./data"

    models = [
        ThreeBody(l, d, g, k, T, agentsNum=200, boundaryLength=5,
                tqdm=True, savePath=savePath, overWrite=False)
        for l, d, g, k, T in product(rangeLambdas, distanceDs, rangeGamma, kappa, period)
    ]

    with Pool(32) as p:
        p.map(run_model, models)