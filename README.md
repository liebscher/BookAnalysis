# BookAnalysis
An analysis of my reading habits from Oct. 2015. Exported using Goodreads.com


## Methods

Organize data in machine-readable csv. The columns were selected from the information given by Goodreads.com, in addition to columns supplied by me.

First, descriptive statistics were needed and were compiled via *main.py*. Since October 2015, I have read approximately 46 books. 11,078 pages have been read (approximately, some books are in progress, and a couple books I skim read).

Most of my books are written by European and North American authors, with Asian authors making only 8.7%, and all other nationalities at 6.5%. Only 10.9% of my books were written by female authors (this is the primary author, not translators, editors, etc.). 45.6% of my books are fiction, whereas 34.8% are nonfiction (the remainder are memoir or neither \[some philosphy for instance is not strictly factual like non-fiction, but also not a narrative like fiction\]). 

The average book takes me 17 days to read, and is 241 pages long. The median book takes me 8 days to read, and is 213 pages. My longest book was 854 pages and took me 122 days (*The Magic Mountain* by Thomas Mann, that was a *long*, but rewarding novel!).

Second, nlp.py scrapes the Wikipedia articles for each distinct author (minus Russell Wild, who does not have a page). Using Rapid Automatic Keyword Extraction, key words were pulled from the articles and compiled into a master list. Still deciding how this is useful, but I foresee some sort of theme extraction being possible. Results will be found in the Results section. TODO: book/author recommendations based on these keywords.

| five_star | european | north_american | asian | other | author_gender | avg_rating | pages | org_publication_year | duration | favorite |
| :------------ | :------------ | :------------ | :------------ | :------------ | :------------ | :------------ | :------------ | :------------ | :------------ | :------------ |
| 1: five star book  | 1: eurpoean author  |  1: north american author | 1: asian author  | 1: author of other country  | 1: female  | Goodreads rating  |  number of pages | original publication year  | days to finish book  |  1: favorite book |

|fiction |nonfiction|contemporary|philosophy|politics|religion|science_tech_math|short_story|memoir|war_story|historical|
| :------------ | :------------ | :------------ | :------------ | :------------ | :------------ | :------------ | :------------ | :------------ | :------------ | :------------ |
|1: fiction book|1:non-fiction book|1:contemporary (last 20-30 years, depending on writing style)|1: philosophy book|1:political book|1:religious book|1:science, technology, or mathematics book|1:composed of short stories|1: memoir|1: war story|1:historical fiction (or non-fiction based on history)|

Iterated 250 over increments of 1/25 of the training/testing cutoff to determine the best training/testing ratio: 0.76-0.80.

Utilize a binary logistic regression model to fit the factors. Target factor is *five_star*, hence why the first data row has that column left blank (for single book testing).

## Results

The first ten keywords extracted by nlp.py are somewhat convoluted and seemingly unrelated:

('wright-patterson air force base', 23.28333333333333), ('τὸ μέγα καὶ τὸ μικρόν', 22.42857142857143), ('annalen der physik und chemie', 21.423856209150326), ('vonnegut married jane marie cox', 19.025831087151843), ('national book critics circle award', 18.116502834555572), ('united states air force academy', 17.34102564102564), ('non-painful referred sensations', 16.666666666666668), ('guillermo de la dehesa', 15.833333333333334), ('southern christian leadership conference', 15.666666666666666), ('roman de la science', 14.724941724941727)

I do not know Greek, so I cannot say what the second keyword represents. In general, these keywords are not very helpful if I wanted to find main ideas, but they could be useful if I was seeking out tangent subjects and topics.

Let's look at the 20th through 40th keywords, without scores:

'television mini-series roots', 'toni morrison collected news', 'black holes emit radiation', 'stephen hawking collected news', 'virtual paulo coelho foundation', 'varlam shalamov official site', 'titus aurelius fulvus antoninus', 'air force reserve', 'annalen der physik', 'khaled hosseini collected news', 'central asia institute', '19th-century literary realism', 'philosophy\njean-paul sartre', 'martin luther king', 'york times bestseller', 'simone de beauvoir', 'civil rights act', 'honoris causa conferred', 'high blood pressure', 'les temps modernes'

These are much more interesting. We begin to see related authors ('simone de beauvoir'), movements ('19th-century literary realism' and 'civil rights act'), specific topics ('black holes emit radiation'), and several other things. TODO: find out why these are not the top keywords.

Possible coefficients of factors which lead to 5 star books:

![Coefficients bar graph](coefficients.png)

The most significant flaw in this design is the lack of data. Insufficient data causes this implementation to act inconsistent when determining the model's coefficients. Must mean I need to read more!
