#from graphviz import digraph
import Facebook
import Group
import Person
from graphviz import Digraph

dot = Digraph(comment='The Round Table',node_attr={'shape': 'plaintext'})



def create_graphviz():
  dot.node('Facebook','''<
  <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4" >
    <TR>
      <TD>facebook</TD>
    </TR>
    <TR>
      <TD>Users = 3<br/>groups=2</TD>
    </TR>
  </TABLE>>''')
  dot.node('Person1', '''<
  <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
    <TR>
      <TD>Person</TD>
    </TR>
    <TR>
      <TD>first_name = Patil<br/>last_name = Gowda<br/>dob = 01-02-1997<br/>password = patil<br/>post = hello friends <br/> username = patil gowda <br/> friends = rahul mogur</TD>
    </TR>
  </TABLE>>''')
  dot.node('Person2', '''<
  <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
    <TR>
      <TD>Person</TD>
    </TR>
    <TR>
      <TD>first_name = Rahul<br/>last_name = Mogur<br/>dob = 03-04-1997<br/>password = rahul<br/>post = hello guys <br/> username = rahul mogu <br/> friends = prashanth sharma</TD>
    </TR>
  </TABLE>>''')
  dot.node('Person3', '''<
  <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
    <TR>
      <TD>Person</TD>
    </TR>
    <TR>
      <TD>first_name = Prashanth<br/>last_name = Sharma<br/>dob = 05-06-1997<br/>password = prashanth<br/>post = Good day <br/> username = prashanth sharma <br/> friends = patil gowda</TD>
    </TR>
  </TABLE>>''')
  dot.node('Group1', '''<
  <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
    <TR>
      <TD>Group</TD>
    </TR>
    <TR>
      <TD>groupname = Friends <br/> groupmembers  = prashanth sharma,patil gowda,rahul mogur <br/> posts = Good night guys..., Bye...</TD>
    </TR>
  </TABLE>>''')
  dot.node('Group2','''<
  <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4" >
    <TR>
      <TD>Group</TD>
    </TR>
    <TR>
      <TD>groupname = sports group <br/>groupmembers = rahul mogur, patil gowda <br/>posts = this is sports group...</TD>
    </TR>
  </TABLE>>''')
  dot.edges([('Facebook','Person1'), ('Facebook','Person2'),('Facebook','Person3'),('Facebook','Group1'),('Facebook','Group2')])


  dot.render('test-output/round-table.gv', view=True) 
  dot.view()
  print(dot.source)
