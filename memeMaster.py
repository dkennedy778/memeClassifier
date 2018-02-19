from memeScraper import *

#See my issue on the google image downloader before using this class. https://github.com/hardikvasa/google-images-download/issues/25
#This issue has been resolved, making my work around pretty superfluous
#Per the issue, make sure you use the for loop to search for memes. Just using the method with a long list of keywords will provide useless results 



# This list is used to search keywords. You can edit this list to search for google images of your choice. You can simply add and remove elements of the list.
#search_keyword = ['memes']
#clean_secondary_keywords = ['forest','house','woods','football','wallpaper','band','restroom','family','football','lamp','religion','mountain','snowboarding','dad','school','teacher','happy','cool people','bus','city','movie','old','smile','park','pretty','flower','tradition','israel','Stalingrad','t-72 main battle tank','money','federal reserve','computer','programming','nice','fbi','things','mother','tears','anguish','theater','korea','tiger tank','me 262','xbox one','fog','landscape']
# This list is used to further add suffix to your search term. Each element of the list will help you download 100 images. First element is blank which denotes that no suffix is added to the search keyword of the above list. You can edit the list by adding/deleting elements from it.So if the first element of the search_keyword is 'Australia' and the second element of keywords is 'high resolution', then it will search for 'Australia High Resolution'
Meme_secondary_keywords = ['happen','miracles','fast','funny','cant','cook','husky','golden','moon','drunk','trump','she','girl','twitter','gamer','obama','biden','america','captain','deadpool','chris','quotes','church','kobe','lebron','messi','durant','work','office','boss','manager','friday', 'wednesday', 'dat boi','workout','running','kayne','fish','cat','coffee', 'dog','adopted','street','fox','frozen', 'snowman','calvin','fox', 'grumpy','bill','business','Kylo','old spice', 'rickroll','cowbell', 'u mad','doge', 'Matt', 'base','Good guy', 'Gangnam','LOL', 'ermahgerd', 'double', 'epic', 'fail', 'romance', 'rogers', 'Numa Numa', 'Black', 'David', 'Star Wars', 'Walmart', 'Achmed','Chuck Norris', 'Charlie', 'Ninja', 'Engrish', 'Bert', 'Jizz', 'Dramatic', 'Coke', 'weed']

#will print out a new subfolder for each variety word, substantially increases the accuracy of results
#for word in variety_keywords:
    # Secondarykeyword = []
    # Secondarykeyword.append(word)
    # memes = findMemes(search_keyword,Secondarykeyword,i)
    # i = i + 1
i = 1
#memes = findMemes("picture",clean_secondary_keywords,i)
memes = findMemes("meme",Meme_secondary_keywords,i)
i = i + 1
