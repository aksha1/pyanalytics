#Topic: Assignment - Clustering - mtcars
#-----------------------------
#libraries
#pip install kneed
import matplotlib.pyplot as plt
from kneed import KneeLocator
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

from pydataset import data
mtcars = data('mtcars')
data = mtcars.copy()
data

#need for scaling : height & weight are in different scales
scaler = StandardScaler()
scaled_features = scaler.fit_transform(data)
scaled_features[:5]  #values between -3 to +3



from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
#scale data ex Yes/No, Ad_impression
data_scaled = scaler.fit_transform(data)
data_scaled



kmeans = KMeans( init = 'random', n_clusters=2 , n_init=3, max_iter=300, random_state=1)
kmeans
kmeans.fit(scaled_features)
y_kmeans = kmeans.predict(scaled_features)
kmeans.inertia_
kmeans.cluster_centers_  #average or rep values
kmeans.n_iter_  #in 6 times, clusters stabilised
kmeans.labels_[:5]
kmeans.cluster_centers_.shape
kmeans.cluster_centers_[0:1]
#mean of mpg, hp, wt
data.groupby(kmeans.labels_).agg({'mpg':'mean','hp':'mean','wt':'mean'})
##plot scatter wt vs mpg with color cluster
plt.scatter(x=...., y=..., c= ….)

plt.scatter(data_scaled[:, 0], data_scaled[:, 1], c=y_kmeans, s=50, cmap='viridis')


