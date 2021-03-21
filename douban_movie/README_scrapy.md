# Scrapy Note
### 1. items.py
主要保存Scrapy抓取的内容 <br>
总体目标为三大类信息：
- TOP250电影的信息（`DoubanMovieItem`)
- TOP250电影中短评的信息 (`DoubanMovieCommentItem`)
- 每个短评所对应的用户信息 (`DoubanMovieUser`)

### 2. Spiders -> Movie_item.py
