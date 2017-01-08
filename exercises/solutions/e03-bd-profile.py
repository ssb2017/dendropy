#! /usr/bin/env python

import dendropy
from dendropy import simulate
from dendropy.calculate import treecompare

from dendropy.utility import messaging
_messenger = messaging.ConsoleMessenger()

nreps = 100
ntax = 100

# generate a taxon namespace consisting of T001, T002, ... T100
tax_labels = ["T{:03d}".format(i+1) for i in range(ntax)]
tns = dendropy.TaxonNamespace(tax_labels)

out = open("../var/bdpd.txt", "w")
for rep in range(nreps):
    tree = simulate.birth_death_tree(
            birth_rate=0.10,
            death_rate=0.01,
            gsa_ntax=ntax * 3,
            taxon_namespace=tns)
    pdm = tree.phylogenetic_distance_matrix()

    ## The manual way
    # distances = []
    # for i1, t1 in enumerate(tns[:-1]):
    #     for i2, t2 in enumerate(tns[i1+1:]):
    #         distances.append(pdm.patristic_distance(
    #             taxon1=t1,
    #             taxon2=t2,
    #             is_normalize_by_tree_size=True,))
    # mean_d = sum(distances)/len(distances)

    # Here is how to do it the easy way!
    dists = pdm.distances(is_weighted_edge_distances=True, is_normalize_by_tree_size=True)
    mean_dists = sum(dists)/len(dists)
    out.write("{}\n".format(mean_dists))

out = open("../var/coalpd.txt", "w")
for rep in range(nreps):
    tree = simulate.pure_kingman_tree(
            taxon_namespace=tns)
    pdm = tree.phylogenetic_distance_matrix()

    ## The manual way
    # distances = []
    # for i1, t1 in enumerate(tns[:-1]):
    #     for i2, t2 in enumerate(tns[i1+1:]):
    #         distances.append(pdm.patristic_distance(
    #             taxon1=t1,
    #             taxon2=t2,
    #             is_normalize_by_tree_size=True,))
    # mean_d = sum(distances)/len(distances)

    # Here is how to do it the easy way!
    dists = pdm.distances(is_weighted_edge_distances=True, is_normalize_by_tree_size=True)
    mean_dists = sum(dists)/len(dists)
    out.write("{}\n".format(mean_dists))
