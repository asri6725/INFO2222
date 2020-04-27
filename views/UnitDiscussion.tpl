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
        <div>
        
        </div>
    </body>
</html>