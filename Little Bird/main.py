from turtle import *


# --- The balance settings
x0 = -250
y0 = 400
scale = 2
line_size = 8

# --- Set the pencile size
pensize(line_size)

# --- This function draws n-points connets them together and then fills
def draw_line(*points, stroke_color="black", fill_color="white"):
  color(stroke_color, fill_color)
  begin_fill()
  for i, point in  enumerate(points):
    if i == 0:
      penup()
      goto(scale * (point[0] + x0), -1 * scale *  (point[1] - y0))
      pendown()
    elif i == len(points)-1:
      goto(scale * (point[0] + x0), -1 * scale *  (point[1] - y0))
      goto(scale * (points[0][0] + x0), -1 * scale * (points[0][1] - y0))
    else:
      goto(scale * (point[0] + x0), -1 * scale *  (point[1] - y0))
  end_fill()

# --- This function draws a circle
def draw_circle(x, y, radius, stroke_color, fill_color):
  color(stroke_color, fill_color)
  pensize(line_size)
  begin_fill()
  penup()
  goto( scale * (x + x0), -1 * scale * (y - y0) - radius)
  pendown()
  circle(radius)
  end_fill()

# Follow the instructions
draw_line((168,283),(158,293),(177,310),(189,306),(197,295),(188,280), stroke_color="#f78201", fill_color="#f78201")
draw_line((188,279),(196,266),(176,282), stroke_color="#ca6001", fill_color="#ca6001")
draw_line((176,282),(153,265),(160,240),(196,266), stroke_color="#f56e00", fill_color="#f56e00")
draw_line((153,265),(160,239),(146,261), stroke_color="#f2b707", fill_color="#f2b707")
draw_line((119,269),(153,265),(176,282),(168,283), stroke_color="#24050e", fill_color="#24050e")
draw_line((119,269),(151,265),(146,261), stroke_color="#7e5d6d", fill_color="#7e5d6d")
draw_line((119,269),(137,285),(168,284), stroke_color="#503a44", fill_color="#503a44")
draw_line((137,285),(158,292),(168,283), stroke_color="#8f2c00", fill_color="#8f2c00")
draw_line((137,285),(130,304),(158,292), stroke_color="#c94f02", fill_color="#c94f02")
draw_line((130,306),(150,318),(158,293), stroke_color="#b44509", fill_color="#b44509")
draw_line((164,332),(177,310),(158,293),(150,319), stroke_color="#f79e06", fill_color="#f79e06")
draw_line((197,294),(224,304),(223,280),(216,258),(196,267),(188,280), stroke_color="#e1ad45", fill_color="#e1ad45")
draw_circle(210,281,12, "black", "black")
draw_circle(206,277, 2, "white", "white")
draw_line((196,267),(201,253),(216,258), stroke_color="#908b91", fill_color="#908b91")
draw_line((216,259),(227,266),(223,279), stroke_color="#b292aa", fill_color="#b292aa")
draw_line((223,280),(232,285),(224,304), stroke_color="#b8b3c2", fill_color="#b8b3c2")
draw_line((196,266),(160,240),(188,240),(203,228),(201,253), stroke_color="#807479", fill_color="#807479")
draw_line((159,240),(203,227),(188,240), stroke_color="#a69397", fill_color="#a69397")
draw_line((203,228),(224,243),(254,249),(216,258),(201,253), stroke_color="#866972", fill_color="#866972")
draw_line((203,228),(254,249),(224,243), stroke_color="#b09ca1", fill_color="#b09ca1")
draw_line((254,250),(271,275),(254,294),(232,285),(223,279),(227,266),(215,259), stroke_color="#6e5b67", fill_color="#6e5b67")
draw_line((254,294),(245,304),(248,316),(224,304),(232,284), stroke_color="#978f9a", fill_color="#978f9a")
draw_line((224,304),(226,321),(189,306),(197,294), stroke_color="#f69700", fill_color="#f69700")
draw_line((226,321),(233,310),(224,304), stroke_color="#cc4f00", fill_color="#cc4f00")
draw_line((164,332),(202,335),(213,316),(189,306),(177,310), stroke_color="#e46d02", fill_color="#e46d02")
draw_line((130,305),(117,341),(110,341), stroke_color="#e76309", fill_color="#e76309")
draw_line((119,339),(150,319),(130,305), stroke_color="#c35100", fill_color="#c35100")
draw_line((117,340),(141,352),(164,331),(150,319), stroke_color="#e66d00", fill_color="#e66d00")
draw_line((141,353),(175,379),(202,335),(164,332), stroke_color="#f17b00", fill_color="#f17b00")
draw_line((175,379),(229,372),(236,342),(226,321),(213,316),(202,336), stroke_color="#f78400", fill_color="#f78400")
draw_line((226,321),(232,309),(248,316),(259,322),(261,334),(236,342), stroke_color="#e86f00", fill_color="#e86f00")
draw_line((261,334),(259,323),(248,317),(245,303),(271,276),(282,327), stroke_color="#827981", fill_color="#827981")
draw_line((254,249),(271,275),(301,300), stroke_color="#898389", fill_color="#898389")
draw_line((271,276),(300,299),(282,327), stroke_color="#6c5c66", fill_color="#6c5c66")
draw_line((300,299),(312,355),(282,326), stroke_color="#64484a", fill_color="#64484a")
draw_line((300,300),(340,364),(344,409),(304,324), stroke_color="#4e3136", fill_color="#4e3136")
draw_line((331,391),(322,393),(344,409),(305,329),(314,367),(299,371), stroke_color="#6d504a", fill_color="#6d504a")
draw_line((282,327),(310,354),(314,367),(297,371),(267,352),(261,333), stroke_color="#9f8685", fill_color="#9f8685")
draw_line((229,371),(244,378),(283,388),(267,353),(261,335),(236,341), stroke_color="#b6b2c0", fill_color="#b6b2c0")
draw_line((228,373),(170,420),(175,379), stroke_color="#f79004", fill_color="#f79004")
draw_line((175,378),(126,378),(141,352), stroke_color="#e56700", fill_color="#e56700")
draw_line((141,353),(126,378),(117,340), stroke_color="#f07c00", fill_color="#f07c00")
draw_line((117,341),(106,381),(110,341), stroke_color="#eb7214", fill_color="#eb7214")
draw_line((106,380),(126,379),(117,340), stroke_color="#ca4c14", fill_color="#ca4c14")
draw_line((107,380),(133,405),(126,378), stroke_color="#d15c00", fill_color="#d15c00")
draw_line((126,379),(175,379),(133,405), stroke_color="#de5d01", fill_color="#de5d01")
draw_line((133,405),(170,422),(175,379), stroke_color="#e56901", fill_color="#e56901")
draw_line((133,405),(111,410),(106,380), stroke_color="#e06602", fill_color="#e06602")
draw_line((111,410),(125,443),(134,434),(133,405), stroke_color="#cc5400", fill_color="#cc5400")
draw_line((134,434),(133,405),(170,422), stroke_color="#c95d09", fill_color="#c95d09")
draw_line((170,421),(196,430),(196,400),(226,413),(229,373), stroke_color="#d86803", fill_color="#d86803")
draw_line((196,430),(196,400),(226,413), stroke_color="#e97000", fill_color="#e97000")
draw_line((229,372),(243,379),(226,413), stroke_color="#e27004", fill_color="#e27004")
draw_line((170,421),(180,441),(196,429), stroke_color="#ca5f0b", fill_color="#ca5f0b")
draw_line((170,421),(156,426),(180,441), stroke_color="#ae490a", fill_color="#ae490a")
draw_line((125,443),(147,454),(156,426),(134,433), stroke_color="#e5dddb", fill_color="#e5dddb")
draw_line((149,453),(180,440),(156,426), stroke_color="#cfc5c3", fill_color="#cfc5c3")
draw_line((124,443),(176,490),(147,454), stroke_color="#bfb4b8", fill_color="#bfb4b8")
draw_line((147,454),(179,441),(176,488), stroke_color="#ded4d2", fill_color="#ded4d2")
draw_line((180,440),(179,453),(198,460),(207,453),(226,413),(196,429), stroke_color="#cb5212", fill_color="#cb5212")
draw_line((243,378),(283,386),(276,425), stroke_color="#a1a4b1", fill_color="#a1a4b1")
draw_line((243,379),(224,412),(249,441),(283,432),(276,425), stroke_color="#9593ab", fill_color="#9593ab")
draw_line((207,453),(249,440),(224,413), stroke_color="#9c9ea2", fill_color="#9c9ea2")
draw_line((283,388),(301,398),(296,437),(283,432),(276,425), stroke_color="#ccc8ca", fill_color="#ccc8ca")
draw_line((198,459),(256,485),(266,461), stroke_color="#a6a0ad", fill_color="#a6a0ad")
draw_line((198,459),(266,461),(249,440),(207,453), stroke_color="#968c97", fill_color="#968c97")
draw_line((249,441),(266,460),(305,465),(283,432), stroke_color="#a9a3b3", fill_color="#a9a3b3")
draw_line((283,431),(314,446),(305,465), stroke_color="#b5abb1", fill_color="#b5abb1")
draw_line((295,436),(314,446),(305,465),(331,456),(318,441), stroke_color="#b9afbb", fill_color="#b9afbb")
draw_line((267,353),(299,371),(317,441),(296,438),(301,398),(283,388), stroke_color="#402c3a", fill_color="#402c3a")
draw_line((331,391),(305,397),(297,371), stroke_color="#503e4c", fill_color="#503e4c")
draw_line((322,393),(330,398),(326,410),(339,427),(322,427),(336,444),(316,441),(305,397), stroke_color="#4c3643", fill_color="#4c3643")
draw_line((330,399),(343,408),(359,433),(344,416),(326,411), stroke_color="#634b57", fill_color="#634b57")
draw_line((326,411),(359,435),(336,427), stroke_color="#624956", fill_color="#624956")
draw_line((321,426),(359,446),(335,443), stroke_color="#614856", fill_color="#614856")
draw_line((318,442),(359,459),(331,455), stroke_color="#5f4553", fill_color="#5f4553")
draw_line((340,367),(348,367),(381,373),(340,373), stroke_color="#907978", fill_color="#907978")
draw_line((341,374),(380,374),(423,387),(418,389),(396,385),(343,384), stroke_color="#32212e", fill_color="#32212e")
draw_line((342,384),(396,385),(343,394), stroke_color="#50393d", fill_color="#50393d")
draw_line((326,411),(343,416),(359,433), stroke_color="#45313c", fill_color="#45313c")
draw_line((323,427),(338,427),(357,436),(355,439),(360,446), stroke_color="#4e3b47", fill_color="#4e3b47")
draw_line((359,459),(354,452),(359,445),(333,442),(316,440),(321,445), stroke_color="#3f2d38", fill_color="#3f2d38")
draw_line((177,453),(197,460),(214,477),(177,489), stroke_color="#ccbec9", fill_color="#ccbec9")
draw_line((267,460),(304,465),(299,481),(257,486), stroke_color="#9d90a1", fill_color="#9d90a1")
draw_line((195,459),(255,484),(245,503), stroke_color="#beb2bb", fill_color="#beb2bb")
draw_line((177,488),(245,504),(214,476), stroke_color="#dcd2d1", fill_color="#dcd2d1")
draw_line((160,587),(151,594),(124,604),(146,600),(126,624),(161,595),(156,621),(170,595), stroke_color="#967b71", fill_color="#967b71")
draw_line((275,601),(250,616),(265,614),(252,638),(280,607),(291,624),(287,594),(306,584),(289,589), stroke_color="#957971", fill_color="#957971")
draw_line((253,485),(297,481),(304,464),(316,479),(246,503), stroke_color="#aba6ab", fill_color="#aba6ab")
draw_line((172,584),(199,582),(170,592), stroke_color="#967b71", fill_color="#967b71")
draw_line((304,465),(331,455),(338,456),(316,480), stroke_color="#cabdbc", fill_color="#cabdbc")
draw_line((202,495),(160,586),(170,595),(175,568),(209,496), stroke_color="#2e212b", fill_color="#2e212b")
draw_line((284,491),(277,601),(282,605),(287,594),(286,577),(291,489), stroke_color="#35242f", fill_color="#35242f")

# Hide the turtle
ht()

# Close the window on click
exitonclick()
