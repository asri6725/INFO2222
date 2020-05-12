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
}
.disclaimer {
  font-size: 18px;
  background-color: white;
  padding: 20px;
  margin-top: 20px;
  height: 200px;
  border-radius: 15px;
}

.help{
  background-color: white;
  font-size: 18px;
  padding: 20px;
  margin-top: 20px;
  border-radius: 15px;
  height: 282px;
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
  margin-top: 60px;
}

.ttl{
  font-size: 28px;
  border-top-width: 1px;
  border-left-width: 1px;
  border-right-width: 1px;
  border-bottom-width: 1px;
  height: 40px;
  text-align: center;



}
#titlediv {

}

.txt{
  font-size: 20px;
  border-top-width: 1px;
  border-left-width: 1px;
  border-right-width: 1px;
  border-bottom-width: 1px;
  height: 350px;
  width: 100%;
}
#textdiv{
  padding-top: 20px;
}
.submit_btn{
  font-size: 18px;

}
#submitdiv{
  padding-top: 20px;
  text-align: center;
}
.red_text{
  color: red;
}

.create{
  font-size: 24px;
  padding-below: 0px;
}
.h4{
  font-size: 28px;
  margin-bottom: -5px;
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
  <h1> STUD <span class="red_text">HELP</span>  </h1>
</div>

<div class="topnav">
  <a href="#">Home</a>
  <a href="#">Unit</a>
  <a href="#">Academic Dishonesty</a>
</div>


<div class="row">
    <h4 class="h4"> Create a post! </h4>


  <div class="leftcolumn">
    <div class="card">
      <form action='{{server}}/homepage/{{username}}/{{subject}}' method="POST">
        <input type=hidden name=username value="{{username}}">

      <div id = titldiv>
          <input name="title" type="text" class="ttl" maxlength="100" placeholder="Title" style="width:100%;"/>
      </div>
      <div id = textdiv>
        <textarea class="txt" rows="4" cols="60" maxlength="250" placeholder="Enter your text here (250 character limit)"></textarea>
      </div>


      <!-- Attempt at image upload, optional to put in or not
      <form action="myform.cgi"> <input type="file" name="fileupload" value="fileupload" id="fileupload">
        <label for="fileupload"> Select a file to upload</label> <br><input type="image" src="/wp-content/uploads/sendform.png" alt="Submit" width="100">
       </form> -->

      <div id = submitdiv>
          <input value="Submit" type="submit" name="submit" class="submit_btn"/>
      </div>

      </form>
    </div>

  </div>

  <div class="rightcolumn">
    <div class="disclaimer">

      <h2>A Quick Heads Up!</h2>

      <p> Make sure your post aligns with the University of Sydney's
        <a href="https://www.sydney.edu.au/students/academic-integrity.html">Academic Integrity</a>
        policies and guidlines.
      </p>
    </div>

    <div class="help">
      <h3> Some Helpful Links </h3>

      <ul>
        <li> <a href="https://library.sydney.edu.au/">The USYD Library </a> </li>
        <br>
        <li> <a href="https://canvas.sydney.edu.au/login/canvas">Canvas Login </a> </li>
        <br>
        <li> <a href="https://sydneystudent.sydney.edu.au/">Sydney Studnet Login </a> </li>
        <br>
        <li> <a href="https://us.edstem.org/login">EdStem Login </a> </li>





    </div>
  </div>


</div>

<div class="footer">
  <h2>Footer</h2>
</div>

</body>
</html>
