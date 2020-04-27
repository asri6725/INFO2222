<div>
    <p>-----------------This is the title</p>
    {{title}}
</div>
<div>
<p>-----------------This is it's content</p>
    {{content}}
</div>
<div>
    <p>-----------------This is the responses</p>
    %for i in responses:
        <p>-----------------user:</p>
        {{i}}
        <br>
        <p>-----------------response:</p>
        {{responses[i]}}
</div>