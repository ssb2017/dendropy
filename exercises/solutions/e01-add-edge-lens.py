#! /usr/bin/env python

import random
import dendropy

from dendropy.utility import messaging
_messenger = messaging.ConsoleMessenger()

src_path = "data/pythonidae.mle.newick"
trees = dendropy.TreeList.get(
        path=src_path,
        schema="newick")
_messenger.info("{} trees read from: {}".format(len(trees), src_path))

rng = random.Random()
for tree in trees:
    for nd in tree.preorder_node_iter():
        if nd is tree.seed_node:
            nd.edge.length = rng.normalvariate(1.0, 1.0)
        else:
            pedge_len = nd.parent_node.edge.length
            nd.edge.length = rng.normalvariate(pedge_len, pedge_len)
print(tree.as_string("newick"))
