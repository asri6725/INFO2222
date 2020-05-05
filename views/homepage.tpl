<html>
    <head>
      <style>
      * {
        box-sizing: border-box;
      }

      body {
        font-family: Arial;
        padding: 10px;
        background: #f1f1f1;
      }

      /* Header/Blog Title */
      .header {
        padding: 30px;
        text-align: center;
        background: white;
      }

      .header h1 {
        font-size: 50px;
      }
      .icon{
        display: block;
        position: fixed;
        left: 10px;
        margin-left: 440px;
        margin-right: 10px;
        margin-top:-15px;
        height: 75px;
        vertical-align: super;
      }

      /* Style the top navigation bar */
      .topnav {
        overflow: hidden;
        background-color: #333;
      }

      /* Style the topnav links */
      .topnav a {
        float: left;
        display: block;
        color: #f2f2f2;
        text-align: center;
        padding: 14px 16px;
        text-decoration: none;
      }

      /* Change color on hover */
      .topnav a:hover {
        background-color: #ddd;
        color: black;
      }

      /* Create two unequal columns that floats next to each other */
      /* Left column */
      .leftcolumn {
        float: left;
        width: 75%;
      }

      /* Right column */
      .rightcolumn {
        float: left;
        width: 25%;
        background-color: #f1f1f1;
        padding-left: 20px;
      }

      /* Fake image */
      .fakeimg {
        background-color: #aaa;
        width: 100%;
        padding: 20px;
      }

      /* Add a card effect for articles */
      .card {
        background-color: white;
        padding: 20px;
        margin-top: 20px;
      }

      /* Clear floats after the columns */
      .row:after {
        content: "";
        display: table;
        clear: both;
      }

      /* Footer */
      .footer {
        padding: 20px;
        text-align: center;
        background: #ddd;
        margin-top: 20px;
      }
      .red_text{
        color: red;
      }


      /* Responsive layout - when the screen is less than 800px wide, make the two columns stack on top of each other instead of next to each other */
      @media screen and (max-width: 800px) {
        .leftcolumn, .rightcolumn {
          width: 100%;
          padding: 0;
        }
      }

      /* Responsive layout - when the screen is less than 400px wide, make the navigation links stack on top of each other instead of next to each other */
      @media screen and (max-width: 400px) {
        .topnav a {
          float: none;
          width: 100%;
        }
      }
      </style>
    </head>
    <body>
      <div class="header">
        <h1>
          <img src="../img/cropped.png" alt="icon" class="icon">
          STUD <span class="red_text">HELP</span>
        </h1>
        <p>blah blah blah</p>
      </div>
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
          <input type=hidden name=unit value="MATH2068">
          <input type=submit name=submit value="MATH2068">
        </form>
        <form action = "/homepage" method="POST">
          <input type=hidden name=username value="{{name}}">
          <input type=hidden name=unit value="COMP2022">
          <input type=submit name=submit value="COMP2022">
        </form>
        <form action = "/homepage" method="POST">
          <input type=hidden name=username value="{{name}}">
          <input type=hidden name=unit value="INFO2222">
          <input type=submit name=submit value="INFO2222">
        </form>
        <form action = "/homepage" method="POST">
          <input type=hidden name=username value="{{name}}">
          <input type=hidden name=unit value="COMP2017">
          <input type=submit name=submit value="COMP2017">
       </form>
       <form action = "/homepage" method="POST">
          <input type=hidden name=username value="{{name}}">
          <input type=hidden name=unit value="DATA3404">
          <input type=submit name=submit value="DATA3404">
       </form>
      </div>
    </body>
</html>
