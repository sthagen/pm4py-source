
SKIP = '>>'


# TODO: fix with epsilon costs, i.e. use cost of label/model = 1000, sync with label = 0, sync with tau = 1
def construct_standard_cost_function(synchronous_product_net, skip):
    costs = {}
    for t in synchronous_product_net.transitions:
        if (skip == t.label[0] or skip == t.label[1]) and (t.label[0] is not None and t.label[1] is not None):
            costs[t] = 1
        else:
            costs[t] = 0
    return costs