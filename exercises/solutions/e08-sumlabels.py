#! /usr/bin/env python

import dendropy

# our common namespace
tns = dendropy.TaxonNamespace()

# load the trees
t1 = dendropy.Tree.get(
    path="data/cetaceans.x.mcmc.con.support-as-brlens.nex",
    schema="nexus",
    taxon_namespace=tns,
    rooting="force-rooted", # or "force-unrooted" if trees unrooted
    )
t2 = dendropy.Tree.get(
    path="data/cetaceans.x.ml.con.support-as-labels.nex",
    schema="nexus",
    taxon_namespace=tns,
    rooting="force-rooted", # or "force-unrooted" if trees unrooted
    )
t3 = dendropy.Tree.get(
    path="data/cetaceans.x.mcct.support-as-annotes.nex",
    schema="nexus",
    taxon_namespace=tns,
    rooting="force-rooted", # or "force-unrooted" if trees unrooted
    )

# calculate the split hashes so that we can correlate splits
# across trees
t1.encode_bipartitions()
t2.encode_bipartitions()
t3.encode_bipartitions()
target_tree = t3

# for each internal node in tree 3
for nd in target_tree.preorder_internal_node_iter():

    # check/skip root node
    if nd is target_tree.seed_node:
        continue

    # the bipartition associated with the edge subtending this node
    bipartition = nd.edge.bipartition

    # set up label parts
    label_parts = []

    # look up edge corresponding to this node on tree1
    try:
        edge = t1.bipartition_edge_map[bipartition]
        # (support on tree1 is represented by branch length)
        label_parts.append(str(edge.length))
    except KeyError:
        label_parts.append("NA")

    # look up edge corresponding to this node on tree2
    try:
        edge = t2.bipartition_edge_map[bipartition]
        # support on tree2 is represented by internal node label
        label_parts.append(edge.head_node.label)
    except KeyError:
        label_parts.append("NA")

    try:
        edge = t3.bipartition_edge_map[bipartition]
        # support on tree3 is given by metadata
        label_parts.append(nd.annotations["support"].value)
    except KeyError:
        label_parts.append("NA")

    # assign label
    nd.label = "/".join(label_parts)

# output the tree
print(target_tree.as_string("newick"))
