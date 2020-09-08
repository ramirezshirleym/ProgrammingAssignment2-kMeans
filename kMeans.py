# NAME: Shirley Ramirez
# Date: September 13, 2020
# DATA-51100, Fall 2020
# PROGRAMMING ASSIGNMENT #2

# INITIALIZATION
print("DATA-51100, Fall 2020\nNAME: Christopher Broadhurst, Alexander Cerdas, Shirley Ramirez \nPROGRAMMING ASSIGNMENT #2")

# Prompt user to enter the number of clusters
k = int(input("Enter the number of clusters: "))
print()

# Read input file
data = [float(line.rstrip()) for line in open('prog2-input-data.txt')]

# Initialize centroids to first k values from data
centroids = dict(zip(range(k), data[0:k]))

# Initialize clusters to empty lists
clusters = dict(zip(range(k), [[] for _ in range(k)]))

# Initialize dict mapping points to dummy values
point_assignments = dict(zip(data, [-1 for _ in data]))

# Initialize dict to store old point assignments
old_point_assignments = dict(zip(data, [-2 for _ in data]))


# ALGORITHM
# Function to place each point in the closest cluster
def assign_to_clusters():
    for cluster in clusters.values():
        cluster.clear()    
    for i, point in enumerate(data):
        min_distance = 1000
        closest_index = -1
        for j, centroid in enumerate(centroids.values()):
            distance = abs(point - centroid)
            if distance < min_distance : 
                min_distance = distance
                closest_index = j
        point_assignments[point] = closest_index
        clusters[closest_index].append(point)
        
# Function to update the locations of centroids of the k clusters
def update_centroids():
    for i,cluster in enumerate(clusters.values()):
        point_sum = sum(cluster)
        length = len(cluster)
        new_centroid = point_sum / length
        centroids[i] = new_centroid

# Reassign points to clusters until convergence occurs
iteration = 1
while point_assignments != old_point_assignments:
    print('Iteration ', iteration)
    old_point_assignments = dict(zip(point_assignments.keys(), point_assignments.values()))
    assign_to_clusters()
    update_centroids()
    print(clusters)
    print()    
    iteration +=1

# PRINT POINT_ASSIGNMENTS
for point_cluster in point_assignments.items():
    print('Point ', point_cluster[0], ' in cluster', point_cluster[1])
    
    