import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def dbscan(data, eps, minPts):
    # Start with all points labeled as 0
    labels = [0] * len(data)
    # Initial cluster setup
    cluster_index = 0

    # Main loop to find new core points
    for p in range(0, len(data)):
        # We only want to do something if a point hasn't be processed yet
        if not (labels[p] == 0):
            continue
        # Get the neighbors of p within the eps distance
        neighbor_points_indexes = region_query(data, p, eps)

        # Our point p doesn't have enough neighbours, so it's noise (-1)
        if len(neighbor_points_indexes) < minPts:
            labels[p] = -1
        else:
            # If it's not noise, we create a new cluster and expand it
            cluster_index += 1
            expand_cluster(
                data, labels, p, neighbor_points_indexes, cluster_index, eps, minPts
            )

    return labels


def expand_cluster(
    data, labels, p, neighbor_points_indexes, cluster_index, eps, minPts
):
    # Our core point gets the label of the current cluster
    labels[p] = cluster_index

    # This is (maybe) clever to avoid recursion. Create a FIFO queue to process all the neighbors.
    i = 0
    while i < len(neighbor_points_indexes):
        # Get the next neighbour's index from queue
        current_neighbour_point_index = neighbor_points_indexes[i]

        # Two cases:
        # 1. The neighbour point was noise when we checked for core point, so we know it didn't have
        # enough neighbours. But because it's in the neighbour list, we label it as part of the current
        # cluster
        # 2. The neighbour point was not labeled as part of another cluster, so we label it as part of the
        # current cluster as well.
        if labels[current_neighbour_point_index] == -1:
            labels[current_neighbour_point_index] = cluster_index
        elif labels[current_neighbour_point_index] == 0:
            labels[current_neighbour_point_index] = cluster_index
            # Look for the neighbours of the current neighbour point that we just added
            additional_neighbours = region_query(
                data, current_neighbour_point_index, eps
            )
            # If the current neighbour point has enough neighbours, we add them to the queue
            if len(additional_neighbours) >= minPts:
                neighbor_points_indexes = (
                    neighbor_points_indexes + additional_neighbours
                )
        # Next item in our fake queue
        i += 1


def region_query(data, p, eps):
    neighbors = []
    # Loop over all points in the dataset and when the distance is less than eps, add to neighbors
    # This is probably too inefficient, probably I don't need to loop over all points in `data` here, really
    for current_data_point_index in range(0, len(data)):
        if np.linalg.norm(data[p] - data[current_data_point_index]) < eps:
            neighbors.append(current_data_point_index)
    return neighbors


data = np.array(
    [
        [1, 2],
        [2, 2],
        [3, 1],
        [3, 1.2],
        [3, 4],
        [3.5, 4.5],
        [5, 6],
        [6, 2],
        [7, 8],
        [4, 7],
        [7.5, 8],
        [9, 10],
    ]
)

my_labels = dbscan(data, eps=2, minPts=2)
print(my_labels)

plt.rcParams["figure.figsize"] = [10, 10]
sns.scatterplot(x=data[:, 0], y=data[:, 1], hue=my_labels, palette="deep")
plt.show()
