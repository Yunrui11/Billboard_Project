# <p align="center">Secrets of the U.S. Music Billboard 1958-2023</p>
### <p align="center">By Team: Data Oven-Load</p>
$${\color{Salmon}Yunrui\space Bao,\space \color{CornflowerBlue}Qixin\space Lin,\space \color{OliveGreen}Erika\space Zhang,\space \color{WildStrawberry}Tianfang\space Zhu}$$
  
<br> 


This project delves into the world of trending music, specifically aiming to uncover the lyrical elements that contribute to a song’s (enduring) presence on the US Billboard charts. This endeavor holds significant relevance from a social science perspective as music often mirrors societal values, trends, and cultural shifts. By examining the characteristics of long-trending songs, we gain insights into the collective psyche and cultural dynamics of different eras.

## Project Goals
- This project is largely exploratory in nature. We explore rank (popularity) trends and assess song lyric content for sentiment scores and high-level themes to better understand the nature and behavior of US Billboard songs.  

### Initial Research Questions
- [Popularity] How are songs trending?
- [Sentiment] How do the sentiments in lyrics change over time?
- [Theme] What are some long-lasting themes in popular songs?

### Initial Findings
- [Popularity] Best-selling artists and songs are more likely to stay on top in recent decades.
- [Sentiment] Positive sentiment scores are decreasing on average in recent decades.
- [Theme] More popular themes have greater context diversity, and love is a trending topic over time. 

### Hypotheses & Supporting Evidence
- [Popularity] **Hypothesis 1: Technology reshapes how people access and consume music.**
  - _We produce preliminary evidence for this hypothesis:_ Analog transition to digital (cassettes to CDs, MP3, CDRs) in the 1990s initiated a notable uptick in song longevity and a notable decrease in the number of unique songs/artists reaching the top of the Billboard each week. 
- [Sentiment] **Hypothesis 2: People are actually struggling more in life** (socially, financially, politically, etc.). Music lyrics to some extent reflect these actual negative sentiments. 
- [Sentiment & Theme] **Hypothesis 3: People are using less positive words and phrases to talk about the same positive and negative themes.** 
  - _We produce preliminary evidence for this hypothesis:_ (e.g.) Artists are always writing about songs with some “Heartbreak” element. Some of these songs in the 60s-70s had high positive sentiment whereas Heartbreak-themed songs in the past two decades largely contained negative sentiments. 

## Data
We have three main sources of data.
1. [A clean Kaggle dataset with US Billboard data 1958-2021](https://www.kaggle.com/datasets/dhruvildave/billboard-the-hot-100-songs/data)
2. [US Billboard: 2021-2023](https://www.billboard.com/charts/hot-100/2021-01-02/)
3. [API for collecting song lyrics: Lyricsgenius](https://lyricsgenius.readthedocs.io/en/master/) from lyric website [Genius](https://www.genius.com)

## Libraries 
- BeautifulSoup4: 4.12.3
- LyricsGenius: 3.0.1
- Matplotlib: 3.7.1
- NumPy: 1.24.3
- OpenAI: 1.12.0
- Pandas: 2.1.1
- Regex: 2022.7.9
- Requests: 2.31.0
- Seaborn: 0.12.2
- Sklearn: 1.3.0
- Tqdm: 4.65.0
- Transformers: 4.38.1


## How to Navigate This Github Repository:
1. [**Data collection:**](data_collection) First, navigate to the data collection folder, which contains the jupyter notebooks we used to obtain the original data (Billboard2021-2023/lyrics) 
    - `billboard_web_crawler.ipynb` -- Crawler to scrape US Billboard
    - `lyric_scraping.ipynb` -- Interactions with *LyricGenius* API
2. [**Data:**](https://github.com/macs30122-winter24/final-project-data-oven-load/tree/main/data) The **data** folder includes some of the data files we scraped or generated. Most final data files are too large and attached as hyperlinks in Readme.
3. [**Data Processing:**](data_processing) In this folder, you can see all our codes for merging and cleaning the data, generating sentiment scores, lyric embedding, and theme analysis.
    - `lyric_processing.py` -- Prelimnary lyric cleaning 
    - `sentiment_analysis.ipynb` -- Sentiment analysis with *BERT*
    - `gpt_interactions.ipynb` -- Lyric Embedding and Themes coding with OpenAI APIs
    - `data_merge.ipynb` -- Merge analyses results
4. After cleaning and merging our data, we generate two files ready for data analysis: 
    - [merged_data.csv:](https://drive.google.com/file/d/14AaROgDJVYbZpf7eCRZCemYu-FctRFwb/view?usp=sharing) contains sentiment scores, **embeddings**, themes, and popularity metrics for **unique songs** on the last week they were on the board (this would capture the song's longevity, max-weeks-on-board, etc. This was used to analyze sentiment scores, themes, and lyric embeddings.
    - [Raw data zip:](https://drive.google.com/file/d/1sTb4eBkXBdlHKIIyNYv2zvm8C17MZuHx/view?usp=sharing) used for analyzing popularity, theme, and sentiment trends at the **weekly** level.
    - [full_billboard_with_themes.csv](https://drive.google.com/file/d/19Jr_gr8dSwpZ1KwMkQHlmH4y-ygH-pu4/view?usp=sharing) Final dataset for major visualizations and analyses.
5. [**Data Visualization:**](data_visualization) Most of the important graphs we produced to help interpret our dataset and make the final conclusions are included in this folder. 
    - `visualize_utils.py` -- Encapsulations of *useful* plotting functions 
    - `visualization_demo.ipynb` -- Demonstrations on function usage and sample plots
    - `visualization_theme_embedding_sentiments.ipynb` -- Some more complex plottings 
6. **Results presentation: Powerpoint**
    - [UPDATED Slides Presentation](https://docs.google.com/presentation/d/1u_OT2HYKaNffuOIFBGm5_8cou9XEmnuVI4_ATVPef48/edit#slide=id.g6bd56c9061_0_750) After reading the questions posted on the discussion board, we discovered that most of them were about how we used ChatGPT 3.5 for theme analysis and BERT for sentiment analysis. To address these questions, we added more slides to explain these two parts.
    - [OLD Slides Presentation](https://drive.google.com/file/d/1f83jJP74yVWpUySt6Vgk3LJ7XJgp1xTT/view?usp=sharing) the slides we used in class 
7. **Results presentation:** [Video](https://drive.google.com/file/d/1mR2gwaIOpgq6M0LO7jCCa_VS_OGMKr2H/view?usp=sharing)
      

## Responsibilities
- Yunrui Bao: Web-scraped and preprocessed US Billboard data for 2021-2023, developed visualization, interpretations, and explanations for sentimental analysis results, drafted proposals, and produced presentation slides. 
- Qixin Lin: Collected and preprocessed all song lyrics from API, produced sentiment scores for lyrics using BERT, developed interpretations for sentiment analysis results, drafted proposals, and produced presentation slides.  
- Erika Zhang: Preprocessed US Billboard data for 1958-2021, conducted data visualization, developed interpretations and narratives using sentiment scores and theme data, drafted proposals, and produced presentation slides. 
- Tianfang Zhu: Produced themes using GPT 3.5 turbo, cleaned song lyrics and produced embeddings using GPT, conducted data visualization, developed interpretations and narratives for popularity data, wrote progress report, produced presentation slides.  

<br>

#### Use of AI
We consulted ChatGPT to clarify and debug the code. 
