"""
The heritability of beak depth in G. scandens seems low. It could be that this observed heritability was just achieved by chance and beak depth is actually not 
really heritable in the species. You will test that hypothesis here. To do this, you will do a pairs permutation test.
"""

# Initialize array of replicates: perm_replicates
perm_replicates = np.empty(10000)

# Draw replicates
for i in range(10000):
    # Permute parent beak depths
    bd_parent_permuted = np.random.permutation(bd_parent_scandens)
    perm_replicates[i] = heritability(bd_parent_permuted,
                                      bd_offspring_scandens)

# Compute p-value: p
p = np.sum(perm_replicates >= heritability_scandens) / len(perm_replicates)

# Print the p-value
print('p-val =', p) #output p-val = 0.0

"""
You get a p-value of zero, which means that none of the 10,000 permutation pairs replicates you drew had a heritability high enough 
to match that which was observed. This strongly suggests that beak depth is heritable in G. scandens, just not as much as in G. fortis.
If you like, you can plot a histogram of the heritability replicates to get a feel for how extreme of a value of heritability you might expect by chance.
"""
