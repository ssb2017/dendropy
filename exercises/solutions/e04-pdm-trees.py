#! /usr/bin/env python

import dendropy

src = open("data/laurasiatherian.distances.ml.csv")
tns = dendropy.TaxonNamespace()
pdm = dendropy.PhylogeneticDistanceMatrix.from_csv(
        src=src,
        taxon_namespace=tns,)

tree_list = dendropy.TreeList(
        taxon_namespace=tns)

nj_tree = pdm.nj_tree()
nj_tree.label = "NJ"
tree_list.append(nj_tree)
upgma_tree = pdm.upgma_tree()
upgma_tree.label = "UPGMA"
tree_list.append(upgma_tree)

print(tree_list.as_string("nexus"))


