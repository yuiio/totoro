<%
rebase('article.tpl')
setdefault('feedback', None)
%>
<h2>{{title}}</h2>


{{!body}}


%if answer != solution:
<form action="/challenge/{{page_name}}" method="post">
  <input name="reponse" type="text" />
  <input value="[réponse]" type="submit" />
</form>
%end

%if answer:
<p>Votre réponse : <code>{{!answer}}</code></p>
%if feedback:
<p>{{!feedback}}</p>
%end
%end
