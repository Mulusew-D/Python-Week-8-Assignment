import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load dataset
df = pd.read_csv("data/metadata.csv")

# Basic info
print("Shape of dataset:", df.shape)
print(df.info())
print("Missing values:\n", df.isnull().sum())

# Clean data
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year
df = df.dropna(subset=['title', 'publish_time'])

# Publications by year
year_counts = df['year'].value_counts().sort_index()
plt.figure(figsize=(8,5))
plt.bar(year_counts.index, year_counts.values)
plt.title('Publications by Year')
plt.xlabel('Year')
plt.ylabel('Number of Publications')
plt.savefig("publications_by_year.png")
plt.show()

# Top 10 journals
top_journals = df['journal'].value_counts().head(10)
plt.figure(figsize=(10,5))
sns.barplot(x=top_journals.values, y=top_journals.index)
plt.title('Top 10 Journals Publishing COVID-19 Papers')
plt.xlabel('Number of Publications')
plt.ylabel('Journal')
plt.savefig("top_journals.png")
plt.show()

# Word Cloud for Titles
titles = " ".join(str(t) for t in df['title'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(titles)
plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Most Frequent Words in Paper Titles')
plt.savefig("wordcloud_titles.png")
plt.show()
