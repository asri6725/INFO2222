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
        float: right;
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
        border-radius: 15px;

      }

      .dropdown-content {
        display: none;
        position: absolute;
        background-color: #f1f1f1;
        min-width: 110px;
        box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
        z-index: 1;
        border-radius: 15px;
      }

      .dropdown-content a {
        color: black;
        padding: 12px 16px;
        text-decoration: none;
        display: block;
        border-radius: 15px;
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
        <a href="#">Home</a>
        <a href="#unit">Unit</a>
        <a href="#Academic_Dishonesty">Academic Dishonesty</a>
        <a href="http://localhost:8080/messages">Messages</a>
        <a href="http://localhost:8080/signout">Logout</a>   
      </div>
      <div class="row">
        <div class="leftcolumn">
          <div class="card">
            <img src="../img/john_doe.jpg" alt="icon" class="user_card_img">
            <h2>{{name}}</h2>
            <p>Bachelor of Advanced Computing</p>
          </div>
          <div class="card">
            <h3>Unit</h3>
            %for i in range(0,len(subject)):
              <div>
                <a href="{{server}}/homepage/{{subject[i]}}" style="text-decoration: none;">
                {{subject[i]}}
                </a>
              </div>
              <br>
            %end
          </div>
        </div>
        <div class="rightcolumn">
          <div class="card">
            <h2>Select units</h2>
            <h3>
              You may select upto 4 units<br>
              Click the unit you would like to add
            </h3>
            <div class="dropdown">
              <button class="dropbtn">select here</button>
              <div class="dropdown-content">
                <a href="#">
                  <form action = "{{server}}/homepage" method="POST">
                    <input type=hidden name=username value="{{name}}">
                    <input type=hidden name=unit value="MATH2068">
                    <input type=submit name=submit value="MATH2068">
                  </form>
                </a>
                <a href="#">
                  <form action = "{{server}}/homepage" method="POST">
                    <input type=hidden name=username value="{{name}}">
                    <input type=hidden name=unit value="COMP2022">
                    <input type=submit name=submit value="COMP2022">
                  </form>
                </a>
                <a href="#">
                  <form action = "{{server}}/homepage" method="POST">
                    <input type=hidden name=username value="{{name}}">
                    <input type=hidden name=unit value="INFO2222">
                    <input type=submit name=submit value="INFO2222">
                  </form>
                </a>
                <a href="#">
                  <form action = "{{server}}/homepage" method="POST">
                    <input type=hidden name=username value="{{name}}">
                    <input type=hidden name=unit value="COMP2017">
                    <input type=submit name=submit value="COMP2017">
                   </form>
                </a>
                <a href="#">
                  <form action = "{{server}}/homepage" method="POST">
                     <input type=hidden name=username value="{{name}}">
                     <input type=hidden name=unit value="DATA3404">
                     <input type=submit name=submit value="DATA3404">
                  </form>
                </a>
              </div>
          </div>
        </div>
        <a name="unit"> </a>
          %for i in range(0,len(subject)):
            <div class="unitcolumn">
              <a href="{{server}}/homepage/{{subject[i]}}" style="text-decoration: none;">
                <div class="card">
                  {{subject[i]}}
                  %if subject[i] == "COMP2022":
                    <p> Models of Computation<br>(6 CP) </p>
                    <img src="../img/cropped.png" alt="icon" class="unit_img">
                  %elif subject[i] == "DATA3404":
                    <p> Data Science Platforms<br>(6 CP) </p>
                    <img src="../img/cropped.png" alt="icon" class="unit_img">
                  %elif subject[i] == "MATH2068":
                    <p> Number Theory and Cryptography (6 CP)<br>  </p>
                    <img src="../img/cropped.png" alt="icon" class="unit_img">
                  %elif subject[i] == "INFO2222":
                    <p> Computing 2 Usability and Security (6 CP)<br> </p>
                    <img src="../img/cropped.png" alt="icon" class="unit_img">
                  %end
                </div>
              </a>
            </div>
          % end
        </div>
        <div class="rightcolumn">
          <div class="card">
            <h2> <a name="Academic_Dishonesty"> Academic Dishonesty </a></h2>
            <h3>Academic dishonesty and plagiarism</h3>
            <p>As a student of the University,<br>
              you are expected to promote a culture of academic integrity.<br>
              We consider any attempt to gain academic advantage by<br>
              dishonest or unfair means to be academic dishonesty – it is unacceptable.
            </p>
          </div>
        </div>
      </div>
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
      </div>
    </body>
</html>
