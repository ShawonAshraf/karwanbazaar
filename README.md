# karwanbazaar
a scrapy based crawler to get articles from  [দৈনিক মতিকণ্ঠ](https://motikontho.wordpress.com/), a satire news site in Bangla


## running locally

```bash
git clone https://github.com/ShawonAshraf/karwanbazaar.git
cd karwanbazaar

# conda env
conda env create -f ghochu.yml
source activate karwanbazaar

# run
python main.py
```

## spiders
there are 4 spiders in the pipeline which need to run sequentially since each spider is dependent on the output from the 
others.

```bash
karwanbazaar/spiders
├── archives.py
├── article_content.py
├── article_urls.py
├── index.py
```

running order of the spiders:

```python
{
    0: index,
    1: archives,
    2: article_urls,
    3: article_content
}
```

all the spiders generate output files (`jsonl`, `txt`, `html`) which are saved in the `output` directory.

## final output
`articles.jsonl` contains the final output with all the posts in `jsonl` format.

this is the format of one line of the `articles.jsonl` file:

```json
{
  "article_id": "article id",
  "title": "title of the article", 
  "content": "content of the article"
}
```