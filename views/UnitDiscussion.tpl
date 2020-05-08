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
      .Qcard {
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
        overflow: hidden;
        
      }
       .contactUs{
        float: left;
        padding-right: 3%;
      }
      .quicklinks{
        text-align: left;
        padding-left: 2%;
        float: left;
        border-left-style: solid;
        border-left-width: thin;
        border-left-color: grey;
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

/* Button to reveal and hide the option to create a post */
      .CreatePostBtn{
        margin-top: 20px;
        font-size: 18px;
        color: white;
        cursor: pointer;
        border: none;
        background: rgba(35, 177, 246, 0.65);
        border-radius: 15px;
        padding: 1% 2%;
        transition: 0.3s;
      }

      .CreatePostBtn:hover {
          box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24),0 17px 50px 0 rgba(0,0,0,0.19);
      }

      .ttl{
        opacity: 0.7;
        font-size: 28px;
        border-top-width: 1px;
        border-left-width: 1px;
        border-right-width: 1px;
        border-bottom-width: 1px;
        height: 40px;
        text-align: center;
      }

      .txt{
        padding-left: 1%;
        opacity: 0.7;
        font-size: 20px;
        border-top-width: 1px;
        border-left-width: 1px;
        border-right-width: 1px;
        border-bottom-width: 1px;
        height: 350px;
        width: 100%;
      }

      .txtlink:hover{
        text-decoration: underline;
        color: rgba(35, 177, 246, 0.65);
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
      </div>
      <div class="topnav">
        <a href="http://localhost:8080/homepage">Home</a>
        <a href="http://localhost:8080/homepage">Unit</a>
        <a href="http://localhost:8080/homepage">Academic Dishonesty</a>
        <a href="http://localhost:8080/messages">Messages</a>
        <a href="http://localhost:8080/signout">Logout</a>
      </div>
      <div class="row">
        <div class="leftcolumn">
          <div class="card">
            <img src="../img/john_doe.jpg" alt="icon" class="user_card_img">
            <h2>John Doe</h2>
            <p>Bachelor of Advanced Computing</p>
          </div>
          <div class="card">
            <h3>Unit</h3>
            {{unit}}
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
                  <form action = "{{server}}/homepage/{{unit}}/{{val}}" method="POST">
                      <input type=hidden name=title value="{{i}}">
                      <input type=submit name=submit value="{{i}}">
                  </form>
                </div>
              </div>
            % end
          </div>


          <div style="text-align: center;">
            <button onclick="myFunction()" class="CreatePostBtn">Want to create your own post? Click here!</button>
          </div>
          <div class="Qcard" id="myDIV" style="display: none;">
            <h3> Create a Post! </h3>

            <!-- <form action='http://{{server}}:8080/homepage/send/{{unit}}' method="post">
                <input name="title" type="text" placeholder="Title"/>
                <input name="content" type="text" placeholder="Content"/>
                <input value="Send" type="submit" />
            </form> -->
            <form action='{{server}}/homepage/send/{{unit}}' method="POST">
              <input type=hidden name=username value="{{username}}">
            <div id = titldiv>
                <input name="title" type="text" class="ttl" placeholder="Title" style="width:100%;"/>
            </div>
            <br>
            <div id = textdiv>
              <textarea class="txt" name="content"rows="4" cols="60" maxlength="250" placeholder="Enter your text here (250 character limit)"></textarea>
            </div>
            <p style="text-align:center;"> (Remember to make sure your post aligns with the University of Sydney's
              <a href="https://www.sydney.edu.au/students/academic-integrity.html" class="txtlink">Academic Integrity</a>
              policies and guidlines.)
            </p>
            <button class="CreatePostBtn" style="text-align:center">Post</button>
          </div>
        </div>
      </div>

      <script>
      function myFunction() {
        var x = document.getElementById("myDIV");
        if (x.style.display === "none") {
          x.style.display = "block";
        } else {
          x.style.display = "none";
        }
      }
      </script>


      <!--Footer -->
    <div class="footer">
      <div class="contactUs">
        <h4 style="font-size: 14px; text-align: left;"> Contact Us </h4>
        <p style="font-size: 14px; text-align: left;"> Got any questions or feedback?
          <br>
          Email us
          <a href="mailto:StudHelpTeam@outlook.com">StudHelpTeam@outlook.com</a>
        </p>
      </div>

      <div class="quicklinks">
        <h5 style="font-size: 14px; text-align: left; line-height:0px;"> Quick Links </h5>


    <!-- LINK TO PAGES WITHIN SITE -->
        <ul>
          <li> <a href="http://localhost:8080/#" class="Footertxtlink">Home</a> </li>
          <li> <a href="http://localhost:8080/#unit" class="Footertxtlink">Unit</a></li>
          <li> <a href="http://localhost:8080/#Academic_Dishonesty" class="Footertxtlink">Academic Dishonesty</a></li>
          <li> <a href="http://localhost:8080/messages" class="Footertxtlink">Messages</a> </li>
          <li> <a href="http://localhost:8080/signout" class="Footertxtlink">Signout</a> </li>
        </ul>
      </div>
    </body>
</html>
