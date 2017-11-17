<%
from persistance import User
user = User()
%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8"/>
    <title>Mission Totoro</title>
    <!--[if lt IE 9]><script src="/static/html5.js"></script><![endif]-->
    <link href='//fonts.googleapis.com/css?family=Source+Code+Pro:300&subset=latin,latin-ext' rel='stylesheet' type='text/css'>
    <link rel="stylesheet" type="text/css" href="/static/style.css"/>
</head>
<body>
  <header>
        <div>
            <h1 class="title-global"><a href="/">Mission Totoro</a></h1>
            %if user.logged:
            <nav>
                <ul>
                    <!-- <li><a href="/page/index">[Index]</a></li> -->
                    <li><a href="/page/wtf">[WTF?]</a></li>
                    <li><a href="/tips">[Tipsbox]</a></li>
                    <li><a href="/reset">[Reset score]</a></li>
                    <li><a href="/logout">[Log Out]</a></li>
                </ul>
            </nav>
            <div class="user">{{user.name}} <span class="star-count">{{user.level}}*</span></div>
            %end
        </div>
  </header>

  <main>
    {{!base}}
  </main>    
</body>
</html>

