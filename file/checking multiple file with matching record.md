This question hasbeen asked with someone there: http://stackoverflow.com/a/34572390/3445802
And this 2 options to solved it:

####Problem
1. File1.txt
<pre>
B21212
F12321
C12345
A09876
Q21212
D23234
A12345
</pre>

2. File2.txt
<pre>
A12345,Noddy in Toy Town
B21212,The Famous Five
E98767,Lord of The Rings
C12345,Casino Royale
A09876,Staff Handbook
D23234,Pinky and Perky
</pre>

<b>Need Answer:</b> how to find the book id from first file and search for it in file 2.

####Answer1 from http://stackoverflow.com/a/34572244/3445802
<pre>
with open('file2') as f:
    d = dict(i.strip().split(',') for i in f)
with open('file1') as f:
    l = f.read().splitlines()

for i in l:
    print(i, d.get(i, '&lt;Not Found&gt;'))
</pre>

<b>Demo:</b>
<pre>
B21212 The Famous Five
F12321 &lt;Not Found&gt;
C12345 Casino Royale
A09876 Staff Handbook
Q21212 &lt;Not Found&gt;
D23234 Pinky and Perky
A12345 Noddy in Toy Town
</pre>

####Answer2 from http://stackoverflow.com/a/34572390/3445802
<pre>
with open('file2.txt', 'r') as f:
    with open('file1.txt', 'r') as ini:
        _dict = dict(p.strip().split(',') for p in f)
        _list = ini.read().splitlines()

        for key in _list:
            if key not in _dict.keys():
                print key, ' &lt;is not found&gt;'
            else:
                print key, _dict.get(key)
</pre>

<b>Demo:</b>
<pre>
B21212 The Famous Five     
F12321  &lt;is not found&gt;      
C12345 Casino Royale           
A09876 Staff Handbook                   
Q21212  &lt;is not found&gt; 
D23234 Pinky and Perky           
A12345 Noddy in Toy Town
</pre>
