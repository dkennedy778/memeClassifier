# coding: utf-8

# In[ ]:

# Searching and Downloading Google Images/Image Links

# Import Libraries

# coding: UTF-8

# The MIT License (MIT)
#
# Copyright (c) 2015 Hardik Vasa
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

#This class is a lightly modified version of https://github.com/hardikvasa/google-images-download, using their python 3.6 fork.
#My pull version is pretty old, and this issue has made alot of the extra work I did superfluous

import time  # Importing the time library to check the time of code execution
import sys  # Importing the System Library
import os

def findMemes(search_keyword, keywords, searchCount):
    # Downloading entire Web Document (Raw Page Content)
    def download_page(url):
        version = (3, 0)
        cur_version = sys.version_info
        if cur_version >= version:  # If the Current Version of Python is 3.0 or above
            import urllib.request  # urllib library for Extracting web pages
            try:
                headers = {}
                headers[
                    'User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                req = urllib.request.Request(url, headers=headers)
                resp = urllib.request.urlopen(req)
                respData = str(resp.read())
                return respData
            except Exception as e:
                print(str(e))
        else:  # If the Current Version of Python is 2.x
            import urllib2
            try:
                headers = {}
                headers[
                    'User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
                req = urllib2.Request(url, headers=headers)
                response = urllib2.urlopen(req)
                page = response.read()
                return page
            except:
                return "Page Not found"


    # Finding 'Next Image' from the given raw page
    def _images_get_next_item(s):
        start_line = s.find('rg_di')
        if start_line == -1:  # If no links are found then give an error!
            end_quote = 0
            link = "no_links"
            return link, end_quote
        else:
            start_line = s.find('"class="rg_meta"')
            start_content = s.find('"ou"', start_line + 1)
            end_content = s.find(',"ow"', start_content + 1)
            content_raw = str(s[start_content + 6:end_content - 1])
            return content_raw, end_content


    # Getting all links with the help of '_images_get_next_image'
    def _images_get_all_items(page):
        items = []
        while True:
            item, end_content = _images_get_next_item(page)
            if item == "no_links":
                break
            else:
                items.append(item)  # Append all the links in the list named 'Links'
                time.sleep(0.1)  # Timer could be used to slow down the request for image downloads
                page = page[end_content:]
        return items


    ############## Main Program ############
    t0 = time.time()  # start the timer

    # Download Image Links
    i = 0
    while i < len(search_keyword):
        items = []
        iteration = "Item no.: " + str(i + 1) + " -->" + " Item name = " + str(search_keyword[i])
        print(iteration)
        print("Evaluating...")
        search_keywords = search_keyword[i]
        search = search_keywords.replace(' ', '%20')

        # make a search keyword  directory
        try:
            os.makedirs(search_keywords + str(searchCount))
        except OSError as e:
            if e.errno != 17:
                raise
                # time.sleep might help here
            pass

        j = 0
        while j < len(keywords):
            pure_keyword = keywords[j].replace(' ', '%20')
            url = 'https://www.google.com/search?q=' + search + pure_keyword + '&espv=2&biw=1366&bih=667&site=webhp&source=lnms&tbm=isch&sa=X&ei=XosDVaCXD8TasATItgE&ved=0CAcQ_AUoAg'
            raw_html = (download_page(url))
            time.sleep(0.1)
            items = items + (_images_get_all_items(raw_html))
            j = j + 1
        # print ("Image Links = "+str(items))
        print("Total Image Links = " + str(len(items)))
        print("\n")

        # This allows you to write all the links into a test file. This text file will be created in the same directory as your code. You can comment out the below 3 lines to stop writing the output to the text file.
        info = open('output.txt', 'a')  # Open the text file called database.txt
        info.write(str(i) + ': ' + str(search_keyword[i - 1]) + ": " + str(items) + "\n\n\n")  # Write the title of the page
        info.close()  # Close the file

        t1 = time.time()  # stop the timer
        total_time = t1 - t0  # Calculating the total time required to crawl, find and download all the links of 60,000 images
        print("Total time taken: " + str(total_time) + " Seconds")
        print("Starting Download...")

        ## To save imges to the same directory
        # IN this saving process we are just skipping the URL if there is any error

        k = 0
        errorCount = 0
        while (k < len(items)):
            version = (3, 0)
            cur_version = sys.version_info
            if cur_version >= version:  # version in above 3.x
                import urllib.request
                import urllib.error

                try:
                    req = urllib.request.Request(items[k], headers={
                        "User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"})
                    response = urllib.request.urlopen(req, None, 15)
                    output_file = open(search_keywords + str(searchCount) + "/" + str(k + 1) + ".jpg", 'wb') #added i here to get more output files

                    data = response.read()
                    output_file.write(data)
                    response.close();

                    print("completed ====> " + str(k + 1))

                    k = k + 1;

                except IOError as e:  # If there is any IOError
                    print(str(e))
                    errorCount += 1
                    print("IOError on image " + str(k + 1))
                    k = k + 1;

                except urllib.error.HTTPError as e:  # If there is any HTTPError

                    errorCount += 1
                    print("HTTPError" + str(k))
                    k = k + 1;
                except urllib.error.URLError as e:

                    errorCount += 1
                    print("URLError " + str(k))
                    k = k + 1;
                except Exception as e:
                    print("program hit an unexpected exception")
                    print(e)
                    k = k + 1;
        i = i + 1

    print("\n")
    print("Everything downloaded!")
    print("\n" + str(errorCount) + " ----> total Errors")

    # ----End of the main program ----#


    # In[ ]:

