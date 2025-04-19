<style type="text/css">.rendered-markdown{font-size:14px} .rendered-markdown>*:first-child{margin-top:0!important} .rendered-markdown>*:last-child{margin-bottom:0!important} .rendered-markdown a{text-decoration:underline;color:#b75246} .rendered-markdown a:hover{color:#f36050} .rendered-markdown h1, .rendered-markdown h2, .rendered-markdown h3, .rendered-markdown h4, .rendered-markdown h5, .rendered-markdown h6{margin:24px 0 10px;padding:0;font-weight:bold;-webkit-font-smoothing:antialiased;cursor:text;position:relative} .rendered-markdown h1 tt, .rendered-markdown h1 code, .rendered-markdown h2 tt, .rendered-markdown h2 code, .rendered-markdown h3 tt, .rendered-markdown h3 code, .rendered-markdown h4 tt, .rendered-markdown h4 code, .rendered-markdown h5 tt, .rendered-markdown h5 code, .rendered-markdown h6 tt, .rendered-markdown h6 code{font-size:inherit} .rendered-markdown h1{font-size:28px;color:#000} .rendered-markdown h2{font-size:22px;border-bottom:1px solid #ccc;color:#000} .rendered-markdown h3{font-size:18px} .rendered-markdown h4{font-size:16px} .rendered-markdown h5{font-size:14px} .rendered-markdown h6{color:#777;font-size:14px} .rendered-markdown p, .rendered-markdown blockquote, .rendered-markdown ul, .rendered-markdown ol, .rendered-markdown dl, .rendered-markdown table, .rendered-markdown pre{margin:15px 0} .rendered-markdown hr{border:0 none;color:#ccc;height:4px;padding:0} .rendered-markdown>h2:first-child, .rendered-markdown>h1:first-child, .rendered-markdown>h1:first-child+h2, .rendered-markdown>h3:first-child, .rendered-markdown>h4:first-child, .rendered-markdown>h5:first-child, .rendered-markdown>h6:first-child{margin-top:0;padding-top:0} .rendered-markdown a:first-child h1, .rendered-markdown a:first-child h2, .rendered-markdown a:first-child h3, .rendered-markdown a:first-child h4, .rendered-markdown a:first-child h5, .rendered-markdown a:first-child h6{margin-top:0;padding-top:0} .rendered-markdown h1+p, .rendered-markdown h2+p, .rendered-markdown h3+p, .rendered-markdown h4+p, .rendered-markdown h5+p, .rendered-markdown h6+p{margin-top:0} .rendered-markdown ul, .rendered-markdown ol{padding-left:30px} .rendered-markdown ul li>:first-child, .rendered-markdown ul li ul:first-of-type, .rendered-markdown ol li>:first-child, .rendered-markdown ol li ul:first-of-type{margin-top:0} .rendered-markdown ul ul, .rendered-markdown ul ol, .rendered-markdown ol ol, .rendered-markdown ol ul{margin-bottom:0} .rendered-markdown dl{padding:0} .rendered-markdown dl dt{font-size:14px;font-weight:bold;font-style:italic;padding:0;margin:15px 0 5px} .rendered-markdown dl dt:first-child{padding:0} .rendered-markdown dl dt>:first-child{margin-top:0} .rendered-markdown dl dt>:last-child{margin-bottom:0} .rendered-markdown dl dd{margin:0 0 15px;padding:0 15px} .rendered-markdown dl dd>:first-child{margin-top:0} .rendered-markdown dl dd>:last-child{margin-bottom:0} .rendered-markdown blockquote{border-left:4px solid #DDD;padding:0 15px;color:#777} .rendered-markdown blockquote>:first-child{margin-top:0} .rendered-markdown blockquote>:last-child{margin-bottom:0} .rendered-markdown table th{font-weight:bold} .rendered-markdown table th, .rendered-markdown table td{border:1px solid #ccc;padding:6px 13px} .rendered-markdown table tr{border-top:1px solid #ccc;background-color:#fff} .rendered-markdown table tr:nth-child(2n){background-color:#f8f8f8} .rendered-markdown img{max-width:100%;-moz-box-sizing:border-box;box-sizing:border-box} .rendered-markdown code, .rendered-markdown tt{margin:0 2px;padding:0 5px;border:1px solid #eaeaea;background-color:#f8f8f8;border-radius:3px} .rendered-markdown code{white-space:nowrap} .rendered-markdown pre>code{margin:0;padding:0;white-space:pre;border:0;background:transparent} .rendered-markdown .highlight pre, .rendered-markdown pre{background-color:#f8f8f8;border:1px solid #ccc;font-size:13px;line-height:19px;overflow:auto;padding:6px 10px;border-radius:3px} .rendered-markdown pre code, .rendered-markdown pre tt{margin:0;padding:0;background-color:transparent;border:0}</style>
<div class="rendered-markdown"><h2></h2>
<p>Now that we have done the difficult part, it's time to find some insights from our data!</p>
<p>We will write SQL queries to find these insights.</p>
<h3><strong>Task 7</strong></h3>
<p>In the next task, you will write SQL queries to find and report the following values.</p>
<p><strong>Note:</strong></p>
<ul>
<li>Do not hard-code the solutions as they will be tested against another hidden dataset.</li>
<li>All float values must be converted to a string with 2 decimal precision.</li>
<li>For each query, write code in the function mentioned in the description and print out the response as instructed.</li>
</ul>
<p>Complete the functions in the <code>code/task7.py</code> file.</p>
<ol>
<li><p><strong>Total salary bill per year</strong> in ascending order of the year (space-separated)
<br  />Function: <code>def total_salary_bill_per_year()</code>
<br  />Output:</p>
<pre><code>2000 5579
2001 9987
...
</code></pre>
<h3>Evaluate</h3>
<p>{Check It!|assessment}(code-output-compare-2801884520)
<br  />{Check It!|assessment}(code-output-compare-2928525557)</p>
</li>
<li><p><strong>Sum of bonus given per year</strong> in ascending order of the year
<br  />Function: <code>def total_bonus_by_year()</code>
<br  />Output:</p>
<pre><code>2000 985
2001 887
...
</code></pre>
<h3>Evaluate</h3>
<p>{Check It!|assessment}(code-output-compare-3610213686)
<br  />{Check It!|assessment}(code-output-compare-4173227123)</p>
</li>
<li><p><strong>All-time month-wise hiring count</strong> in ascending order of the month (integer)
<br  />Function: <code>def monthly_hiring_stats()</code>
<br  />Output:</p>
<pre><code>1 888
2 24
...
12 87
</code></pre>
<h3>Evaluate</h3>
<p>{Check It!|assessment}(code-output-compare-933184456)
<br  />{Check It!|assessment}(code-output-compare-56806618)</p>
</li>
<li><p><strong>Value of the most expensive acquisition</strong>
<br  />Function: <code>def most_costly_acquisition()</code>
<br  />Output:</p>
<h3>Evaluate</h3>
<p>{Check It!|assessment}(code-output-compare-3898411283)
<br  />{Check It!|assessment}(code-output-compare-1800909509)</p>
</li>
<li><p><strong>Value of the most expensive &ldquo;Office&rdquo; acquisition</strong>
<br  />Function: <code>def most_costly_office_acquisition()</code>
<br  />Output:</p>
<h3>Evaluate</h3>
<p>{Check It!|assessment}(code-output-compare-3815044522)
<br  />{Check It!|assessment}(code-output-compare-3330058377)</p>
</li>
<li><p><strong>Total Campaign expenditure for each product ID</strong>, sorted in descending order of total expenditure
<br  />Function: <code>def product_wise_campaign_spending()</code>
<br  />Output:</p>
<pre><code>54 44932
12 43447
...
43 543
</code></pre>
<h3>Evaluate</h3>
<p>{Check It!|assessment}(code-output-compare-1341588859)
<br  />{Check It!|assessment}(code-output-compare-1396714614)</p>
</li>
<li><p><strong>Name of the top 5 products</strong> with maximum sales, in order
<br  />Function: <code>def top_5_products_by_sales()</code>
<br  />Output:</p>
<h3>Evaluate</h3>
<p>{Check It!|assessment}(code-output-compare-1771711838)
<br  />{Check It!|assessment}(code-output-compare-396784961)</p>
</li>
<li><p><strong>Name of the top 5 retail stores</strong> with maximum sales, in order
<br  />Function: <code>def top_5_retail_stores_by_sales()</code>
<br  />Output:</p>
<h3>Evaluate</h3>
<p>{Check It!|assessment}(code-output-compare-1287461202)
<br  />{Check It!|assessment}(code-output-compare-2183912877)</p>
</li>
</ol>
</div>