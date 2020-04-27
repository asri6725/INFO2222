<html>
    <head>

    </head>
    <body>
        <p> This is the homepage {{name}} </p>
        <div>
            <p>-----------------This is the subjects chosen by the user</p>
            %for i in range(0,len(subject)):
                <a href="/homepage/{{subject[i]}}">{{subject[i]}} </a><br>
            % end
        </div>
        <p>-----------------This is the subjects that can be added</p>
        <div>
        <form action = "/homepage" method="POST">
        <input type=hidden name=username value="{{name}}">
        <input type=hidden name=unit value="math2068">
        <input type=submit name=submit value="math2068">
     </form>  
        <form action = "/homepage" method="POST">
        <input type=hidden name=username value="{{name}}">
        <input type=hidden name=unit value="comp2022">
        <input type=submit name=submit value="comp2022">
     </form>  
     <form action = "/homepage" method="POST">
        <input type=hidden name=username value="{{name}}">
        <input type=hidden name=unit value="info2222">
        <input type=submit name=submit value="info2222">
     </form>  
     <form action = "/homepage" method="POST">
        <input type=hidden name=username value="{{name}}">
        <input type=hidden name=unit value="comp2017">
        <input type=submit name=submit value="comp2017">
     </form>  
     <form action = "/homepage" method="POST">
        <input type=hidden name=username value="{{name}}">
        <input type=hidden name=unit value="data3404">
        <input type=submit name=submit value="data3404">
     </form>  
      </div>
    </body>
</html>