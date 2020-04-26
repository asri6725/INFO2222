<html>
    <head>

    </head>
    <body>
        <p> This is the homepage {{name}} </p>
        <div>
            %for i in range(0,len(subject)):
                <a href="/homepage/{{subject[i]}}">{{subject[i]}} </a>
            % end
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
        <input type=hidden name=unit value="comp2123">
        <input type=submit name=submit value="comp2123">
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
        
    </body>
</html>