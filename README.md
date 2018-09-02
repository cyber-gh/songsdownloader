# songsdownloader
basic app for downloading songs, under development
<h1> Song downloader app </h1>
<ol>
<h3>Requirements</h3>
<li>geckodriver(firefox), also add it to system path
<li>selenium, just pip install
</ol>

<h2>Description</h2> <br>
<p>
It takes a list of songs as a input(one per line + the author optional), currently named as sont_lists.txt. Then it automates 
download process from the following site: <a>https://www.mp3juices.cc/</a>. The parser is set to parse a json response from the spotify
web api of a get tracks from playlist. Will be developed in the future.
</p>

<p >
<font colo="red"> Bug to fix: </font> Currently the site from which this app is downloading has an ad which opens in new tab, sometimes crashing the app.
</p>
