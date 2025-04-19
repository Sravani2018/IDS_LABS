<style type="text/css">.rendered-markdown{font-size:14px} .rendered-markdown>*:first-child{margin-top:0!important} .rendered-markdown>*:last-child{margin-bottom:0!important} .rendered-markdown a{text-decoration:underline;color:#b75246} .rendered-markdown a:hover{color:#f36050} .rendered-markdown h1, .rendered-markdown h2, .rendered-markdown h3, .rendered-markdown h4, .rendered-markdown h5, .rendered-markdown h6{margin:24px 0 10px;padding:0;font-weight:bold;-webkit-font-smoothing:antialiased;cursor:text;position:relative} .rendered-markdown h1 tt, .rendered-markdown h1 code, .rendered-markdown h2 tt, .rendered-markdown h2 code, .rendered-markdown h3 tt, .rendered-markdown h3 code, .rendered-markdown h4 tt, .rendered-markdown h4 code, .rendered-markdown h5 tt, .rendered-markdown h5 code, .rendered-markdown h6 tt, .rendered-markdown h6 code{font-size:inherit} .rendered-markdown h1{font-size:28px;color:#000} .rendered-markdown h2{font-size:22px;border-bottom:1px solid #ccc;color:#000} .rendered-markdown h3{font-size:18px} .rendered-markdown h4{font-size:16px} .rendered-markdown h5{font-size:14px} .rendered-markdown h6{color:#777;font-size:14px} .rendered-markdown p, .rendered-markdown blockquote, .rendered-markdown ul, .rendered-markdown ol, .rendered-markdown dl, .rendered-markdown table, .rendered-markdown pre{margin:15px 0} .rendered-markdown hr{border:0 none;color:#ccc;height:4px;padding:0} .rendered-markdown>h2:first-child, .rendered-markdown>h1:first-child, .rendered-markdown>h1:first-child+h2, .rendered-markdown>h3:first-child, .rendered-markdown>h4:first-child, .rendered-markdown>h5:first-child, .rendered-markdown>h6:first-child{margin-top:0;padding-top:0} .rendered-markdown a:first-child h1, .rendered-markdown a:first-child h2, .rendered-markdown a:first-child h3, .rendered-markdown a:first-child h4, .rendered-markdown a:first-child h5, .rendered-markdown a:first-child h6{margin-top:0;padding-top:0} .rendered-markdown h1+p, .rendered-markdown h2+p, .rendered-markdown h3+p, .rendered-markdown h4+p, .rendered-markdown h5+p, .rendered-markdown h6+p{margin-top:0} .rendered-markdown ul, .rendered-markdown ol{padding-left:30px} .rendered-markdown ul li>:first-child, .rendered-markdown ul li ul:first-of-type, .rendered-markdown ol li>:first-child, .rendered-markdown ol li ul:first-of-type{margin-top:0} .rendered-markdown ul ul, .rendered-markdown ul ol, .rendered-markdown ol ol, .rendered-markdown ol ul{margin-bottom:0} .rendered-markdown dl{padding:0} .rendered-markdown dl dt{font-size:14px;font-weight:bold;font-style:italic;padding:0;margin:15px 0 5px} .rendered-markdown dl dt:first-child{padding:0} .rendered-markdown dl dt>:first-child{margin-top:0} .rendered-markdown dl dt>:last-child{margin-bottom:0} .rendered-markdown dl dd{margin:0 0 15px;padding:0 15px} .rendered-markdown dl dd>:first-child{margin-top:0} .rendered-markdown dl dd>:last-child{margin-bottom:0} .rendered-markdown blockquote{border-left:4px solid #DDD;padding:0 15px;color:#777} .rendered-markdown blockquote>:first-child{margin-top:0} .rendered-markdown blockquote>:last-child{margin-bottom:0} .rendered-markdown table th{font-weight:bold} .rendered-markdown table th, .rendered-markdown table td{border:1px solid #ccc;padding:6px 13px} .rendered-markdown table tr{border-top:1px solid #ccc;background-color:#fff} .rendered-markdown table tr:nth-child(2n){background-color:#f8f8f8} .rendered-markdown img{max-width:100%;-moz-box-sizing:border-box;box-sizing:border-box} .rendered-markdown code, .rendered-markdown tt{margin:0 2px;padding:0 5px;border:1px solid #eaeaea;background-color:#f8f8f8;border-radius:3px} .rendered-markdown code{white-space:nowrap} .rendered-markdown pre>code{margin:0;padding:0;white-space:pre;border:0;background:transparent} .rendered-markdown .highlight pre, .rendered-markdown pre{background-color:#f8f8f8;border:1px solid #ccc;font-size:13px;line-height:19px;overflow:auto;padding:6px 10px;border-radius:3px} .rendered-markdown pre code, .rendered-markdown pre tt{margin:0;padding:0;background-color:transparent;border:0}</style>
<div class="rendered-markdown"><h2></h2>
<p>The acquisitions team employs JSON to store data due to loose structure of the nature of attributes present due to difference in the nature of attributes in each acquisition. We have the <code>acquisitions.json</code> file in the <code>data</code> folder which contains a list of acquisitions. Each object in the list may have different set of keys.</p>
<p><strong>Task 3</strong> Implement the following functions in the in <code>code/task3.py</code> file present in your file tree.</p>
<ol>
<li><p>Write a function <code>analyze_json</code> which takes the json file path as a parameters and prints out all the different keys present in all the json objects and also displays the number of occurrences of each key. If an invalid filename is given (missing or invalid JSON file), the function should print &ldquo;Invalid filename provided&rdquo;.</p>
<h3>Example output</h3>
<p>If the file provided contains the following data</p>
<pre><code class="json">  [
    {
      "name": "Jon Doe",
      "age": 10,
    },
    {
      "name": "Jane Doe",
      "age": 10,
      "salary": 105000
    }
  ]
</code></pre>
<p>The output should be</p>
<pre><code class="shell">  age: 2
  name: 2
  salary: 1
</code></pre>
</li>
<li><p>Write a function <code>print_json_schema</code> which takes a json file path as a parameter and prints the schema of the file.</p>
</li>
<li><p>The schema of a json is its list of key's present in all the objects, sorted in alphabetical order.</p>
</li>
<li><p>File name and json attributes should be separated by a <strong>&ldquo;: &ldquo;</strong></p>
</li>
<li><p>Remove the file extension from the filename</p>
<h3>Example output</h3>
<p>If the given json file contains the following structure (say file name is <code>sample.json</code>)</p>
<pre><code class="json">  [
    {
      "name": "Jon Doe",
      "age": 10,
    },
    {
      "name": "Jane Doe",
      "age": 10,
      "salary": 105000
    }
  ]
</code></pre>
<p>The output should be</p>
<pre><code class="shell">sample: age, name, salary
</code></pre>
</li>
</ol>
<p>Check out Python's official JSON module <a href="https://docs.python.org/3/library/json.html">here</a>!</p>
<h3>Evaluation</h3>
<p>{Check It!|assessment}(code-output-compare-1745444007)
<br  />{Check It!|assessment}(code-output-compare-1081856758)</p>
<p>{Check It!|assessment}(code-output-compare-2429570925)</p>
<p>{Check It!|assessment}(code-output-compare-3191721582)</p>
<p><strong>IMPORTANT</strong></p>
<p>After testing your function use it to understand the schema of your <code>sales.db</code>, you can use <code>main.py</code> for that purpose. Make notes of your current understanding of the data. You will need to include a <code>data_exploration3.png</code> in your <code>images</code> folder with your current understanding of the acquisitions data. This can be a diagram handwritten or using a software tool, just make sure that is readable and professional.</p>
</div>