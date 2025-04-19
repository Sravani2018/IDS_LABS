<style type="text/css">.rendered-markdown{font-size:14px} .rendered-markdown>*:first-child{margin-top:0!important} .rendered-markdown>*:last-child{margin-bottom:0!important} .rendered-markdown a{text-decoration:underline;color:#b75246} .rendered-markdown a:hover{color:#f36050} .rendered-markdown h1, .rendered-markdown h2, .rendered-markdown h3, .rendered-markdown h4, .rendered-markdown h5, .rendered-markdown h6{margin:24px 0 10px;padding:0;font-weight:bold;-webkit-font-smoothing:antialiased;cursor:text;position:relative} .rendered-markdown h1 tt, .rendered-markdown h1 code, .rendered-markdown h2 tt, .rendered-markdown h2 code, .rendered-markdown h3 tt, .rendered-markdown h3 code, .rendered-markdown h4 tt, .rendered-markdown h4 code, .rendered-markdown h5 tt, .rendered-markdown h5 code, .rendered-markdown h6 tt, .rendered-markdown h6 code{font-size:inherit} .rendered-markdown h1{font-size:28px;color:#000} .rendered-markdown h2{font-size:22px;border-bottom:1px solid #ccc;color:#000} .rendered-markdown h3{font-size:18px} .rendered-markdown h4{font-size:16px} .rendered-markdown h5{font-size:14px} .rendered-markdown h6{color:#777;font-size:14px} .rendered-markdown p, .rendered-markdown blockquote, .rendered-markdown ul, .rendered-markdown ol, .rendered-markdown dl, .rendered-markdown table, .rendered-markdown pre{margin:15px 0} .rendered-markdown hr{border:0 none;color:#ccc;height:4px;padding:0} .rendered-markdown>h2:first-child, .rendered-markdown>h1:first-child, .rendered-markdown>h1:first-child+h2, .rendered-markdown>h3:first-child, .rendered-markdown>h4:first-child, .rendered-markdown>h5:first-child, .rendered-markdown>h6:first-child{margin-top:0;padding-top:0} .rendered-markdown a:first-child h1, .rendered-markdown a:first-child h2, .rendered-markdown a:first-child h3, .rendered-markdown a:first-child h4, .rendered-markdown a:first-child h5, .rendered-markdown a:first-child h6{margin-top:0;padding-top:0} .rendered-markdown h1+p, .rendered-markdown h2+p, .rendered-markdown h3+p, .rendered-markdown h4+p, .rendered-markdown h5+p, .rendered-markdown h6+p{margin-top:0} .rendered-markdown ul, .rendered-markdown ol{padding-left:30px} .rendered-markdown ul li>:first-child, .rendered-markdown ul li ul:first-of-type, .rendered-markdown ol li>:first-child, .rendered-markdown ol li ul:first-of-type{margin-top:0} .rendered-markdown ul ul, .rendered-markdown ul ol, .rendered-markdown ol ol, .rendered-markdown ol ul{margin-bottom:0} .rendered-markdown dl{padding:0} .rendered-markdown dl dt{font-size:14px;font-weight:bold;font-style:italic;padding:0;margin:15px 0 5px} .rendered-markdown dl dt:first-child{padding:0} .rendered-markdown dl dt>:first-child{margin-top:0} .rendered-markdown dl dt>:last-child{margin-bottom:0} .rendered-markdown dl dd{margin:0 0 15px;padding:0 15px} .rendered-markdown dl dd>:first-child{margin-top:0} .rendered-markdown dl dd>:last-child{margin-bottom:0} .rendered-markdown blockquote{border-left:4px solid #DDD;padding:0 15px;color:#777} .rendered-markdown blockquote>:first-child{margin-top:0} .rendered-markdown blockquote>:last-child{margin-bottom:0} .rendered-markdown table th{font-weight:bold} .rendered-markdown table th, .rendered-markdown table td{border:1px solid #ccc;padding:6px 13px} .rendered-markdown table tr{border-top:1px solid #ccc;background-color:#fff} .rendered-markdown table tr:nth-child(2n){background-color:#f8f8f8} .rendered-markdown img{max-width:100%;-moz-box-sizing:border-box;box-sizing:border-box} .rendered-markdown code, .rendered-markdown tt{margin:0 2px;padding:0 5px;border:1px solid #eaeaea;background-color:#f8f8f8;border-radius:3px} .rendered-markdown code{white-space:nowrap} .rendered-markdown pre>code{margin:0;padding:0;white-space:pre;border:0;background:transparent} .rendered-markdown .highlight pre, .rendered-markdown pre{background-color:#f8f8f8;border:1px solid #ccc;font-size:13px;line-height:19px;overflow:auto;padding:6px 10px;border-radius:3px} .rendered-markdown pre code, .rendered-markdown pre tt{margin:0;padding:0;background-color:transparent;border:0}</style>
<div class="rendered-markdown"><h2></h2>
<h1></h1>
<p>Now that we have developed a good understanding of how different data attributes are and learned to parse each of the different formats, we want to get all the data in a single format so we can perform relationship-based queries.</p>
<h3><strong>Task 6:</strong></h3>
<p>Let us build a new SQLite database that unifies data from SQLite (Sales), Excel (HR), JSON (Acquisitions), and CSV (Marketing). You will be working in <code>code/task6.py</code></p>
<p>Write a script that reads the following data files and creates a new SQLite database:</p>
<ul>
<li>SQLite database file path: <code>data/sales.db</code></li>
<li>Directory path containing Excel files: <code>data/*.xlsx</code></li>
<li>JSON file path: <code>data/acquisitions.json</code></li>
<li>CSV file path: <code>data/campaigns.csv</code></li>
</ul>
<p>The script should create a new SQLite database file called <code>output.db</code> in the <code>data</code> folder.</p>
<h4><strong>Table Naming Instructions</strong></h4>
<ul>
<li><strong>Excel Files:</strong> The table name should be of the format <code>&lt;SheetName&gt;</code>. If multiple Excel files have the same <code>&lt;SheetName&gt;</code>, merge the data into a single table.</li>
<li><strong>JSON Files:</strong> The table name should be of the format <code>&lt;FileName&gt;</code>.</li>
<li><strong>CSV Files:</strong> The table name should be of the format <code>&lt;FileName&gt;</code>.</li>
<li><strong>SQLite Files:</strong> Use the table names as they are.</li>
</ul>
<p><strong>Note:</strong> All the table names should be in title case as shown above.</p>
<h4><strong>Columns Naming Instructions</strong></h4>
<p>The name of the columns should be as they were in the original format.</p>
<ul>
<li><strong>Excel Files:</strong> The column name should be as the column names in the excel files.</li>
<li><strong>JSON Files:</strong> The column name should be exactly like the keys present in the json files.</li>
<li><strong>CSV Files:</strong> The column name should be as the column names in the csv files.</li>
<li><strong>SQLite Files:</strong> Keep the column names as they are.</li>
</ul>
<h4><strong>Additional Notes</strong></h4>
<ul>
<li>If any invalid input file is provided, simply print <code>"Invalid input"</code> and exit the program.</li>
<li>Hint: Check out <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html">Pandas</a> to have a simple conversion to SQL from different formats.</li>
<li>Convert date attributes to the format YYYY-MM-DD and store it as a string.</li>
</ul>
<h3>Evaluate</h3>
<p>{Check It!|assessment}(code-output-compare-2169788243)
<br  />{Check It!|assessment}(code-output-compare-1596709075)</p>
</div>