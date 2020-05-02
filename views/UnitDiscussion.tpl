<html>
    <head>

    </head>
    <body>
        <h1> Discussion for {{unit}} </h1>
        <div>
        <p>-----------------This is the discussion titles like ed</p>
            %for i in title:
                % mod_i = ''.join(e for e in i if e.isalnum())
                <a href="/homepage/{{unit}}/{{mod_i}}"> {{i}} </a><br>
            % end
        </div>

        <div>
         <p>-----------------This is the discussion titles like ed</p> 
            <form action='http://localhost:8080/homepage/send/{{unit}}' method="post">
                <input name="title" type="text" placeholder="Title"/>
                <input name="content" type="text" placeholder="Content"/>
                <input value="Send" type="submit" />
            </form>
        </div>
    </body>
</html>