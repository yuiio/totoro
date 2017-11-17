<%
rebase('article.tpl')
from persistance import User
user = User()
%>

<h2>--- { Your tipsbox } ---</h2>

%if user.level < 1:

<p>Pour chaque level gagné, une nouvelle ressource débloquée <em>:-)</em></p>

%else:
    <ul>
    %for num in range(user.level):
        %if num < 7:
        <li><a href="/page/tips{{num+1}}">[Tips {{num+1}}]</a></li>
        %end
    %end
</ul>
%end
