#! /usr/bin/env python

import dendropy
from dendropy.calculate import treescore

from dendropy.utility import messaging
_messenger = messaging.ConsoleMessenger()

trees_src_path = "data/cetaceans.mcmc.nex"
chars_src_path = "data/cetaceans.chars.nex"
burnin = 100

tns = dendropy.TaxonNamespace()

_messenger.info("Reading trees from: {}".format(trees_src_path))
trees = dendropy.TreeList.get(
        path=trees_src_path,
        schema="nexus",
        taxon_namespace=tns,
        tree_offset=burnin,
        )
_messenger.info("{} trees ({} taxa) read from: {}".format(
    len(trees),
    len(tns),
    trees_src_path))

_messenger.info("Reading character data from: {}".format(chars_src_path))
chars = dendropy.DnaCharacterMatrix.get(
        path=chars_src_path,
        schema="nexus",
        taxon_namespace=tns,
        )
_messenger.info("{} characters read from: {}".format(
    chars.sequence_size,
    chars_src_path))

# _messenger.info("Generating consensus tree ...")
# summary_tree = trees.consensus()
# summary_tree.comments.append("Consensus tree calculated after burn-in of {}".format(burnin))
_messenger.info("Generating MCC tree ...")
summary_tree = trees.maximum_product_of_split_support_tree()
summary_tree.comments.append("Maximum clade credibility tree calculated after burn-in of {}".format(burnin))

_messenger.info("Scoring consensus tree")
pscore = treescore.parsimony_score(
        summary_tree,
        chars,
        gaps_as_missing=True,)
_messenger.info("Parsimony score = {}".format(pscore))
summary_tree.annotations["parsimony_score"] = pscore

dataset = dendropy.DataSet()
dataset.comments.append("Post-burnin consensus tree scored under parsimony")
dataset.comments.append("Parsimony score = {}".format(pscore))
summary_tree_list = dataset.new_tree_list(taxon_namespace=tns)
summary_tree_list.append(summary_tree)
dataset.char_matrices.add(chars)
print(dataset.as_string("nexus"))
