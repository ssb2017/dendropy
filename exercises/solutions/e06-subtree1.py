#! /usr/bin/env python

import collections
import dendropy

# read the tree
tree = dendropy.Tree.get(
        path="data/seasia.nex",
        schema="nexus")

# sort the taxa
to_retain = set()
# to_prune = set()
for nd in tree.leaf_node_iter():
    if not nd.annotations.get_value("malaya") and not nd.annotations.get_value("indochina"):
        to_retain.add(nd.taxon)
    # else:
    #     to_prune.add(nd.taxon)
tree.retain_taxa(to_retain)
# tree.prune_taxa(to_prune)
tree.purge_taxon_namespace()
print(tree.as_string("nexus"))


# tree1 = dendropy.Tree(tree)
# tree1.retain_taxa(to_retain)
# print(tree1.as_string("nexus"))

# tree2 = dendropy.Tree(tree)
# tree2.prune_taxa(to_prune)
# print(tree2.as_string("nexus"))
