
- https://docs.djangoproject.com/en/1.8/ref/templates/builtins/#striptags
- https://docs.djangoproject.com/en/1.9/ref/templates/builtins/#removetags (*custom filter tags)

<h2>Input:</h2>
<pre>
&lt;b&gt;Deskripsi Sample Blog Item 2.&lt;/b&gt;&lt;br /&gt;&lt;h3&gt;Teknik Tree&lt;/h3&gt; yang kami maksudkan disini adalah teknik untuk mencari 
sebuah website yang berkaitan dengan website yang saat ini anda temukan.
</pre>

<h2>1. Sample Method 1</h2>
<pre>{{ object.body|safe|truncatewords:"10" }}</pre>
<b><code>The output is:</code></b><br />
<b>Deskripsi Sample Blog Item 2.</b><br /><h3>Teknik Tree</h3> yang kami maksudkan disini adalah ...

<h2>2. Sample Method 2</h2>
<pre>{{ object.body|safe|striptags|truncatewords:"10" }}</pre>
<b><code>The output is:</code></b><br />
Deskripsi Sample Blog Item 2. Teknik Tree yang kami maksudkan disini adalah ...
