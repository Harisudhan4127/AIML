# PageRank Algorithm

pages = {
    'A': ['B', 'C'],
    'B': ['C'],
    'C': ['A'],
    'D': ['C']
}

N = len(pages)
d = 0.85

# Initialize PageRank values
rank = {page: 1 / N for page in pages}

# Calculate PageRank iteratively
for iteration in range(100):
    new_rank = {}

    for page in pages:
        new_rank[page] = (1 - d) / N

        for source in pages:
            if page in pages[source]:
                new_rank[page] += d * rank[source] / len(pages[source])

    rank = new_rank

# Display final ranking
print("Final PageRank:")
for page, value in sorted(
    rank.items(), key=lambda item: item[1], reverse=True
):
    print(page, ":", round(value, 4))

# Find the most important webpage
print("Most Important Webpage:", max(rank, key=rank.get))