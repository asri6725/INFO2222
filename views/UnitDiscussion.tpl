<html>
    <head>

    </head>
    <body>
        <h1> Discussion for {{unit}} </h1>
        <div>
        <p>-----------------This is the discussion titles like ed</p>
            %for i in title:
                % mod_i = ''.join(e for e in i if e.isalnum())
               
                % val = None
                % for char in mod_i.lower():
                    %val = ord(char) - 96 
                    %end

                <form action = "http://10.86.163.196:8080/homepage/{{unit}}/{{val}}" method="POST">
                    <input type=hidden name=title value="{{i}}">
                    <input type=submit name=submit value="{{i}}">
                </form>
            % end
        </div>

        <div>
         <p>-----------------This is the discussion titles like ed</p> 
            <form action='http://10.86.163.196:8080/homepage/send/{{unit}}' method="post">
                <input name="title" type="text" placeholder="Title"/>
                <input name="content" type="text" placeholder="Content"/>
                <input value="Send" type="submit" />
            </form>
        </div>
    </body>
</html>