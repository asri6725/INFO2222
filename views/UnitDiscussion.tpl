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

      input[type=submit]{
        background-color: transparent;
        border: none;
        text-align: center;
        color: black;
        margin-left: 13px;
        padding: 1px 2px;
        text-decoration: none;
        cursor: pointer;
        font-size: 13px;
      }
      a {
        color: black;
      }


      /* Header/Blog Title */
      .header {
        padding: 30px;
        text-align: center;
        background: white;
      }

      .header h1 {
        font-size: 50px;
        display: inline-block;

      }

      .icon{
        display: inline-block;
        left: 10px;
        margin-left: -100px;
        margin-right: 0px;
        margin-top:-30px;
        height: 70px;
        vertical-align: text-bottom;
        border-radius: 15px;
      }
      .user_card_img{
        display: block;
        height: 100px;
        border-radius: 15px;
      }
      .unit_img{
        display: block;
        /* height: 100px; */
        width: 100%;
        height: 200px;
        padding: 20px;
        border-radius: 15px;
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
      .rightcolumn {
        float: left;
        width: 75%;
        padding-left: 20px;
        border-radius: 15px;
      }

      .unitcolumn {
        float: left;
        width: 25%;
        padding: 3px;
        display: inline-table;
        border-radius: 15px;
      }


      /* Right column */
      .leftcolumn {
        float: left;
        width: 25%;
        border-radius: 15px;
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
        object-fit: cover;
        border-radius: 15px;
      }

      .discuss_card {
        background-color: #aaa;
        padding: 20px;
        margin-top: 20px;
        object-fit: cover;
        width: 45%;
        border-radius: 15px;
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
        border-radius: 15px;
      }
      .red_text{
        color: red;
      }

      .dropbtn {
        background-color: #4CAF50;
        color: white;
        padding: 16px;
        font-size: 16px;
        border: none;
        border-radius: 15px;

      }

      .dropdown {
        position: relative;
        display: inline-block;
      }

      .dropdown-content {
        display: none;
        position: absolute;
        background-color: #f1f1f1;
        min-width: 110px;
        box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
        z-index: 1;
      }

      .dropdown-content a {
        color: black;
        padding: 12px 16px;
        text-decoration: none;
        display: block;
      }

      .dropdown-content a:hover {background-color: #ddd;}

      .dropdown:hover .dropdown-content {display: block;}

      .dropdown:hover .dropbtn {background-color: #3e8e41;}



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
      </div>
      <div class="topnav">
        <a href="http://localhost:8080/homepage">Home</a>
        <a href="http://localhost:8080/homepage">Unit</a>
        <a href="http://localhost:8080/homepage">Academic Dishonesty</a>
      </div>
      <div class="row">
        <div class="leftcolumn">
          <div class="card">
            <img src="../img/john_doe.jpg" alt="icon" class="user_card_img">
            <h2>John Doe</h2>
            <p>Bachelor of Advanced Computing</p>
          </div>
          <div class="card">
            <h3>13123</h3>
            <div class="fakeimg"><p>Image</p></div>
            <div class="fakeimg"><p>Image</p></div>
            <div class="fakeimg"><p>Image</p></div>
          </div>
          <div class="card">
            <h3>13212312</h3>
            <p>Some text adfa..</p>
          </div>
        </div>
        <div class="rightcolumn">
          <div class="card">
            <h1> {{unit}} </h1>
            %if unit == "COMP2022":
              <h3> Models of Computation </h3>
            %elif unit == "DATA3404":
              <h3> Data Science Platforms </h3>
            %elif unit == "MATH2068":
              <h3> Number Theory and Cryptography </h3>
            %elif unit == "INFO2222":
              <h3> Computing 2 Usability and Security </h3>
            %end
          </div>
          <div class="card">
            <h2> Discussion Board </h2>
            %for i in title:
              <div class="discuss_card">
                <div>
                  % mod_i = ''.join(e for e in i if e.isalnum())

                  % val = None
                  % for char in mod_i.lower():
                      %val = ord(char) - 96
                      %end
                  <form action = "http://{{server}}:8080/homepage/{{unit}}/{{val}}" method="POST">
                      <input type=hidden name=title value="{{i}}">
                      <input type=submit name=submit value="{{i}}">
                  </form>
                </div>
              </div>
            % end
          </div>
          <div class="card">
            <h3> New Question </h3>
            <form action='http://{{server}}:8080/homepage/send/{{unit}}' method="post">
                <input name="title" type="text" placeholder="Title"/>
                <input name="content" type="text" placeholder="Content"/>
                <input value="Send" type="submit" />
            </form>
          </div>
        </div>
      </div>
      <div class="footer">
        <h2>{{unit}} Discussion Page</h2>
      </div>
    </body>
</html>
