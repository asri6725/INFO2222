<!DOCTYPE html>
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
  display: inline-block;
  left: 10px;
  margin-left: -100px;
  margin-right: 0px;
  margin-top:-30px;
  height: 70px;
  vertical-align: text-bottom;
}
/* Style the top navigation bar */
.topnav {
  overflow: hidden;
  background-color: #333;}

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
  width: 65%;

}

/* Right column */
.rightcolumn {
  float: left;
  width: 35%;
  background-color: #f1f1f1;
  padding-left: 20px;
}

/* Add a card effect for articles */
.card {
  background-color: white;
  padding: 20px;
  margin-top: 20px;
  border-radius: 15px;
  height: 503px;;
}



.username{
  font-size: 12px;
  margin: -5px;
  text-indent: 2%;
  font-style: italic;
}
.question{
  /* border-style: solid;
  border-width: 0.5px;
  border-color: rgba(35, 177, 246, 0.65); */
  background: #F7F7F7;
  border-radius: 15px;
  padding: 1%;

}
.commentdiv{
  padding-top: 10px;
  text-indent: 5%;
}

.comment{
  padding-left: 1%;
  font-size: 18px;
  width: 80%;
}
.submit_btn{
  font-size: 16px;
  color: white;
  cursor: pointer;
  border: none;
  background: rgba(35, 177, 246, 0.65);
  border-radius: 15px;
  padding: 1% 2%;
  transition: 0.3s;
}
.submit_btn:hover {
    box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24),0 17px 50px 0 rgba(0,0,0,0.19);
}
.ttl{
  font-size: 28px;
  border-top-width: 1px;
  border-left-width: 1px;
  border-right-width: 1px;
  border-bottom-width: 1px;
  height: 40px;
  text-align: left;
  text-indent: 10px;
}
.txt{
  font-size: 20px;
  border-top-width: 1px;
  border-left-width: 1px;
  border-right-width: 1px;
  border-bottom-width: 1px;
  width: 100%;
}
#textdiv{
  text-indent: 40px;
}
.userComment{
  margin-top: 1%;
  background-color:  #F7F7F7;
  border-radius: 15px;
  text-indent: 10px;
  padding: 0.2%;
  font-size: 26px;
}
.disclaimer {
  border-style: solid;
  border-color: black;
  border-width: 1px;
  font-size: 18px;
  background-color: #A4D1E7;
  padding: 20px;
  margin-top: 20px;
  height: 200px;
  border-radius: 15px;
  transition: 0.3s;
}

.disclaimer:hover {
    box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24),0 17px 50px 0 rgba(0,0,0,0.19);
}

.help{
  border-style: solid;
  border-color: black;
  border-width: 1px;
  background-color: #A4D1E7;
  font-size: 18px;
  padding: 20px;
  margin-top: 20px;
  height: 282px;
  border-radius: 15px;
  transition: 0.3s;
}

.help:hover {
    box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24),0 17px 50px 0 rgba(0,0,0,0.19);
}
/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}

.row{
  padding-top: 20px;
  height: 100%;
  margin-top: -20px;
}

/* Footer */
.footer {
  padding: 20px;
  text-align: center;
  background: #ddd;
  margin-top: 20px;
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
#submitdiv{
  padding-top: 20px;
  text-align: center;
}
.red_text{
  color: red;
}

.h4{
  font-size: 28px;
  margin-bottom: -5px;
}

.txtlink{
  text-decoration: none;
  font-style: italic;
}
.txtlink:hover{
  text-decoration: underline;
  /* color: rgba(35, 177, 246, 0.65); */
  color: white;
}

.Footertxtlink{
  text-decoration: none;
  font-style: italic;

}
.Footertxtlink:hover{
  text-decoration: underline;
  color: rgba(35, 177, 246, 0.65);
}


.bottomchat{
  border-top-style: solid;
  border-top-color: black;
  border-top-width: thin;
  width: 95%;
  padding: 1%;

}
.message{
  width: 85%;
  font-size: 16px;
}
.chatbox{
  padding: 5px;
  margin-top: 2px;
  background: #A4D1E7;
  border-radius: 15px;
  text-align: center;
  border-color: black;
  max-height: 85%;
}

.usrmsg{
  overflow: hidden;
  overflow-y: auto;
  font-size: 20px;
  padding: 1px;
  margin-left: : 5%;
  margin-top: 3%;
  cursor: pointer;
  text-align: center;
  width: 90%;
}

.usrmsg:hover{
  background-color: #ddd;
  color: black;
}
input[type=text]:focus{
  border: 3px solid rgba(35, 177, 246, 0.65);
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
  <!-- The Header -->
  <h1>
    <img src="../img/cropped.png" alt="icon" class="icon">
    STUD <span class="red_text">HELP</span>
  </h1>
</div>

<!-- Navigation Bar -->
<div class="topnav">
  <a href="{{server}}/#">Home</a>
  <a href="{{server}}/#unit">Unit</a>
  <a href="{{server}}/#Academic_Dishonesty">Academic Dishonesty</a>
  <a href="{{server}}/messages">Messages</a>
  <a href="{{server}}/signout">Signout</a>
</div>
</div>

  <!-- The whole bottom section grouped into one div -->
<div class="row">

  <!-- All those relating to the main information on the page i.e.
        the left coloum-->
  <div class="leftcolumn">
    <div class="card" style="position: relative; overflow:auto;">


  <!-- /* Displays all usersnames that you have made a chat with
      CLicking one will take you to a chat with that individual person
       This div is formatted such that if there are several users you have chats with,
       you can scroll through with a scroll bar*/ -->

      <div class="chatbox" >
        <h6 style="font-size: 22px; "> Your Messages </h6>
        % for user in users:
            <form action = "/messages/{{user}}" method="POST">
                <input type="hidden" name="message_user" value="{{user}}" />
                <input type="submit" value="{{user}}" class="usrmsg"/>
            </form>

        % end


      </div>

      <!-- /* This div will stay at the bottom of the card div, here users can enter the username
          of someone they want to message along with what they want to message.
         This will create a new user in the above chat box, which can be clicked to open messages with them,
         also including the original message they sent to start the conversation.*/ -->

      <div class="bottomchat" style="position: absolute; bottom: 10px;">
        <form action="{{server}}/messages/send" method="POST">
            <input name="message_user" type="text" maxlength="10" placeholder="recipient (username 10 characters)" style="font-size: 18px;width:40%;"/>
            <input name="message" type="text" maxlength="100" placeholder="Message (100 characters)" style="font-size: 18px; width:40%; margin-left:10px;"/>
            <input type="Submit" value="Send" class="submit_btn" style="margin-Left:10px;"/>
        </form>


      </div>

    </div>
  </div>


  <!-- All those relating to the supplementary information on the page i.e.
        the right coloum-->
  <div class="rightcolumn">
    <div class="disclaimer">
      <h2>A Quick Heads Up!</h2>
      <p> Make sure your post aligns with the University of Sydney's
        <a href="https://www.sydney.edu.au/students/academic-integrity.html" class="txtlink">Academic Integrity</a>
        policies and guidlines.
      </p>
    </div>

  <!--Links to USYD sites -->
    <div class="help">
      <h3> Some Helpful Links </h3>
      <ul>
        <li> <a href="https://library.sydney.edu.au/" class="txtlink">The USYD Library </a> </li>
        <br>
        <li> <a href="https://canvas.sydney.edu.au/login/canvas" class="txtlink">Canvas Login </a> </li>
        <br>
        <li> <a href="https://sydneystudent.sydney.edu.au/" class="txtlink">Sydney Studnet Login </a> </li>
        <br>
        <li> <a href="https://us.edstem.org/login" class="txtlink">EdStem Login </a> </li>
    </div>
  </div>

</div>

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
      <li> <a href="{{server}}/#" class="Footertxtlink">Home</a> </li>
      <li> <a href="{{server}}/#unit" class="Footertxtlink">Unit</a></li>
      <li> <a href="{{server}}/#Academic_Dishonesty" class="Footertxtlink">Academic Dishonesty</a></li>
      <li> <a href="{{server}}/messages" class="Footertxtlink">Messages</a> </li>
      <li> <a href="{{server}}/signout" class="Footertxtlink">Signout</a> </li>
    </ul>
  </div>
</div>

</body>
</html>
