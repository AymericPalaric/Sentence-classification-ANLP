import wikipediaapi

def import_wikipedia_articles(category_name, num_articles):
	wiki_wiki = wikipediaapi.Wikipedia(
		language='en',
		extract_format=wikipediaapi.ExtractFormat.WIKI,
		user_agent='MyCoolBot/1.0'
	)

	category = wiki_wiki.page("Category:" + category_name)
	articles = category.categorymembers.values()

	imported_articles = []
	count = 0

	for article in articles:
		if count >= num_articles:
			break

		if article.ns == wikipediaapi.Namespace.MAIN:
			page = wiki_wiki.page(article.title)
			imported_articles.append(page.text)
			count += 1

	return imported_articles



LABELS = ['Politics', 'Health', 'Finance', 'Travel', 'Food', 'Education','Environment', 'Fashion', 'Science', 'Sports', 'Technology', 'Entertainment']
Wiki_category = ['Politics', 'Health', 'Finance', 'Travel', 'Food', 'Education','Environment', 'Fashion', 'Science', 'Sports', 'Technology', 'Entertainment']

num_articles = 100

articles_dict = {}
for i,label in enumerate(LABELS):
	
	articles_dict[label] = import_wikipedia_articles(Wiki_category[i], num_articles)
	print(f'Imported {num_articles} articles for {label} category')

