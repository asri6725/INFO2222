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
        

        
    </body>
</html>