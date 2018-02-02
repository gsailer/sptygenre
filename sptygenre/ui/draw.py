import matplotlib.pyplot as plt

def draw_wordcloud_with_matplot(wordcloud):
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.margins(x=0, y=0)
    plt.show()
