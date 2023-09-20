import wordcloud as wc

text = "python 파이썬 test data user wordcloud"
wcText = wc.WordCloud(font_path="c:\\Windows\\Fonts\\맑은 고딕\\malgun.ttf",
                      background_color="white",
                      stopwords=["test", "data"],
                      min_font_size=10,
                      max_font_size=20,
                      width=1000,
                      height=1000
                      )
wcText.generate_from_text(text)
wcText.to_image().show()
wcText.to_file("test.png")