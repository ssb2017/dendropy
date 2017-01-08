#! /usr/bin/env python

import dendropy
import collections

tns = dendropy.TaxonNamespace()
tree = dendropy.Tree.get(
        path="data/Bininda-emonds_2007_mammals.nexus",
        schema="nexus",
        taxon_namespace=tns,
        rooting="force-rooted",)

groups = collections.defaultdict(list)
for taxon in tree.taxon_namespace:
    genus_name = taxon.label.split(" ")[0]
    groups[genus_name].append(taxon)

genus_trees = dendropy.TreeList(taxon_namespace=tns)
for genus_name in groups:
    genus_taxa = groups[genus_name]
    # print("{}: {}".format(genus_name, genus_taxa))
    if len(genus_taxa) > 2:
        genus_tree = tree.extract_tree_with_taxa(genus_taxa)
        genus_trees.append(genus_tree)
print(genus_trees.as_string("nexus"))


