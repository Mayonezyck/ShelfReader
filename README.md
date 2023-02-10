# ShelfReader  

#book finding logic 2.X  
Say: we are looking for Book A.  
Book should be in the ABCDEFGHI order  
Actually, Books are in AFEBDCHI order, meaning, a total mess  
-Construct a tree  
-Display on the screen the first book, and looking for the first book, A  
-A is in place, move to the second book  
-Display on the screen, looking for the book, B  
-F is in the place of B's  
-B and F doesn't match, throw both in the tree with their next nodes  
-raise the flag of F's 'hasNote', making it notify when reached  
-instruct the user to take out the book F from shelf.  
+tree{  
[B-C]  
[F-G]  
}  
+shelf{AEBDCHI}  
-move forward, looking for the book, C  
-C and E doesn't match, throw both in the tree with their next nodes  
-raise the flag of E's 'hasNote', making it notify when reached  
-instruct the user to take out the book E from shelf.  
add the C into tree, the first level, and add D to every C node  
+tree{  
[B-C-D]  
[F-G]  
[C-D]  
}  
add the E into tree, the first level, and add F to every E node  
+tree{  
[B-C-D]  
[F-G]  
[C-D]  
[E-F]  
}  
+shelf{ABDCHI}  
-move forward, looking for the book, D  
-next book on the shelf is B, which is in the tree, and doesn't appear in any node after D,  
-We first take a look at B branch in the tree, the bottom node is D, D doesn't appear in the tree's first row,  
-Meaning we can leave B at where it is and its position should be right  
+shelf{ABDCHI}  
-update the tree by deleting every children of every B node  
+tree{  
[B]  
[F-G]  
[C-D]  
[E-F]  
}  
-and add D to the tree's first row, add child E to every D node  
+tree{  
[B]  
[F-G]  
[C-D-E]  
[E-F]  
[D-E]  
}  
-still check for D  
-next book on the shelf is D  
-D is D  
-update the tree by deleting every children of every D node  
+tree{  
[B]  
[F-G]  
[C-D]  
[E-F]  
[D]  
}  
+shelf{ABDCHI}  
-move forward, looking for the book, E  
-E has a 'hasNote' flag and it will show a alert window on the screen  
-The user is required to take E and put it back on current location on the shelf.  
-update the tree by deleting every children of every E node  
+tree{  
[B]  
[F-G]  
[C-D]  
[E]  
[D]  
}  
+shelf{ABDECHI}  
-move forward, looking for the book, F    
-F has a 'hasNote' flag and it will show  a alert window on the screen  
-The user is required to take F and put it back on current location on the shelf.  
-update the tree by deleting every children of every F node  
+tree{  
[B]  
[F]  
[C-D]  
[E]  
[D]  
}  
+shelf{ABDEFCHI}  
-move forward, looking for the book, G  
-next book on the shelf is C, which is in the tree, and doesn't appear in any node after G,  
-We first take a look at C branch in the tree, the bottom node is D, D appears in the tree's first row,  
-Meaning we can instruct the user to place C before D  
+shelf{ABCDEFHI}  
-update the tree by deleting every children of every C node  
-and add G and its child to the tree  
+tree{  
[B]  
[F]  
[C]  
[E]  
[D]  
[G-H]  
}  
-still check for G  
-next book on the shelf is H  
-throw both into the tree, update evey G/H node with their child if they don't already have one  
+tree{  
[B]  
[F]  
[C]  
[E]  
[D]  
[G-H-I]  
[H-I]  
}  
+shelf{ABCDEFI}  
-move forward, looking for the book, H  
-H has a 'hasNote' flag and it will show a alert window on the screen  
-The user is required to take H and put it back on current location on the shelf.  
-update the tree by deleting every children of every H node  
+tree{  
[B]  
[F]  
[C]  
[E]  
[D]  
[G-H]  
[H]  
}  
+shelf{ABCDEFHI}  
+move forward, looking for the book, I  
-I is I   
  
  
  
Generate a report by the tree contents  
every node in the first level that doesn't have a child is misplaced  
every node in the first level that do have one+ child is missing  
every node that doesn't appear in the first level of the tree is correctly placed  
The number of misplaced item seems can be compensated by removing the number of missing items' depth in tree(needs more experiment)  




-----------------------------------------

Spring semester notes:

***!! New Thought!!*** 

okkkkkkk

SSH in from office computer for file transfer.
Per launching of the program, load the booklist.csv and start right away.

Switch gear to using the "Shelf-Reading Tool" 
Download the file from shelf-reading tool and pre-process the file, load all data into book classes.




