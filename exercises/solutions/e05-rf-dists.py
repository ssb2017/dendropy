#! /usr/bin/env python

import dendropy
from dendropy.calculate import treecompare
from dendropy.calculate import statistics


def calc_rfd_distribution(src_path):
    tns = dendropy.TaxonNamespace()
    trees = dendropy.TreeList.get(
            path=src_path,
            schema="nexus")
    rf_dists = []
    for idx1, t1 in enumerate(trees[:-1]):
        for idx2, t2 in enumerate(trees[idx1+1:]):
            rfd = treecompare.unweighted_robinson_foulds_distance(t1, t2)
            rf_dists.append(rfd)
    mean, var = statistics.mean_and_sample_variance(rf_dists)
    print("mean = {}, var = {}, 5/95% quantile = {}".format(
        mean,
        var,
        statistics.quantile_5_95(rf_dists)))

calc_rfd_distribution("data/cetaceans.bootstraps10.trees")
calc_rfd_distribution("data/cetaceans.mcmc10.nex")
