import urllib2
import BeautifulSoup

import time
from time import gmtime, strftime

timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())


url = "https://tools.wmflabs.org/phetools/statistics.php"
req = urllib2.Request(url, headers={'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/11.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30"}) 
con = urllib2.urlopen(req)
soup = BeautifulSoup.BeautifulSoup(con)
tables = soup.findChildren('table')
allrows = soup.findAll('tr')
x = len(allrows)
fle = open("two.txt",'a')

wiki_content = """Last update in Sept 2016, will be updated bi-monthly.

{|class="wikitable sortable"
<th colspan="7" style="text-align:center">Page namespace (Pages of Books)</th>
<th colspan="5" style="text-align:center">Main namespace (Article)</th>
!style="background: #efefef;"|'''language'''
!style="background: #ffffff;"|'''all pages'''
!style="background: #ffa0a0;"|'''not proof.'''
!style="background: #b0b0ff;"|'''problem.'''
!style="background: #ddd;"|'''w/o text'''
!style="background: #ffe867;"|'''proofread'''
!style="background: #90ff90;"|'''validated'''
!style="background: #efefef;"|'''all pages'''
!style="background: #90ff90;"|'''with scans'''
!style="background: #ffa0a0;"|'''w/o scans'''
!style="background: #ddd;"|'''disamb'''
!style="background: #efefef;"|'''percent'''
|-
"""
fle.close()
fle1 = open("index.html",'w')
#fle1.write("<table border = '1'>")

table_head = """

<head>
  <title>Indic WikiSource Status</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"></script>
<style type="text/css">
.quality4 { background:#90ff90; }
.quality3 { background:#ffe867; }
.quality2 { background:#b0b0ff; }
.quality1 { background:#ffa0a0; }
.quality0 { background:#dddddd; }

.withscans { background:#c0c0ff; }
.naked { background:#ffa0a0; }
.disamb { background:#dddddd; }


</style>
</head>
<body>
<div class="container">

<h1> Indic WikiSource Stats </h1>
<p>

This table shows the number of pages that have been proofread using the ProofreadPage extension, at various Wikisource subdomains. It is updated daily. </p>

<p><b>Notes:</b></p>

<p>The "proofread" column counts all the pages that have been proofread : [category q3] + [category q4]</p>

<p>Language subdomains are ranked by the number of page verifications : [category q3] + 2x[category q4]</p>


<p>The "with scans" column counts pages whose text is transcluded from the "Page:" namespace.</p>


<p>The "disamb" column counts disambiguation pages.</p>


<p>The "percent" column shows the percentage of texts backed with scans, excluding disambiguation pages from the total:percent = [with scans]/([with scans] + [without scans])</p>


<p>A large number of texts at de.ws do not use transclusion, although they are backed with scans. In addition, a few wikisources still do not have a namespace for author pages; these pages are counted as texts without scans.</p>


<hr>

<table class="table table-striped table-bordered">
<tr>
<td></td>
<th colspan="6" style="text-align:center">Page namespace</th>
<th colspan="5" style="text-align:center">Main namespace</th>
</tr>
<tr>
<th>language</th>
<th>all pages</th>
<th class="quality1">not proof.</th>
<th class="quality2">problem.</th>
<th class="quality0">w/o text</th>
<th class="quality3">proofread</th>
<th class="quality4">validated</th>
<th>all pages</th>
<th class="withscans">with scans</th>
<th class="naked">w/o scans</th>
<th class="disamb">disamb</th>
<th>percent</th>
"""

fle1.write(table_head)


for i in range(0,x):
    if '<td>te</td>' in str(allrows[i]) or '<td>ta</td>' in str(allrows[i]) or '<td>ml</td>' in str(allrows[i]) or '<td>bn</td>' in str(allrows[i]) or '<td>kn</td>' in str(allrows[i]) or '<td>or</td>' in str(allrows[i]) or '<td>sa</td>' in str(allrows[i]) or '<td>as</td>' in str(allrows[i]) or '<td>mr</td>' in str(allrows[i]) or '<td>gu</td>' in str(allrows[i]) or '<td>pa</td>' in str(allrows[i]):
 #       fle = open("index.html",'w')
#	fle1.write("<table border = '1'>")
        #fle.write (str(allrows[i]).replace('</td><td>',' || ').replace('<tr><td>','| ').replace('</td></tr>','')+'\n')
        #fle.write (str('|-')+'\n')
        fle1.write(str(allrows[i]))
fle1.write("</table></div>")
fle1.write("<p align='right'> This list is updated daily once. Last update was on  " + timestamp + " GMT <br/>")
fle1.write("<p align='right'> Source : <a href = 'https://github.com/KaniyamFoundation/Indic_wikisource_stats'> https://github.com/KaniyamFoundation/Indic_wikisource_stats ")
fle1.close()
