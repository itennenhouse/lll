# lll
LLL algorithm
Note: I added this readme just to make things clearer, but all of the code was committed and pushed before the deadline as can be seen on the timestamp.    

Note 2: I realized I forgot to mention on page 5 of my writeup that Oded's matrix there is not of a full-rank basis, but since we only spoke of full-rank matrices we can get the determinant as the product of the diagonals which ends up being what is listed. Also I belive I stated this in the writeup, but just in case the diagrams are from Oded's paper.  

Note 3: Slight typo on page 2, "Schorr's algorithm" should be "Schnorr's algorithm", and by completely differently I mean it viewed lattice reduction differently (i.e. in blocks instead of all at a time)  
  
Alright, so the fucntion lll() in lll.py takes three arguments: a full-rank integer basis written as a numpy array of vectors with each vector as a row, a constant delta which you can read about in my paper, and the number of vectors (should be equal to dimension of space each vector is in).    

Finally, note in our example lll problem we used a delta value of 3/4 as this appears to be a sort of standard value, likely because it is the largest rational in [1/4,1) with a denominator of 4.  

In terms of grading, I understand our project was in sort of a weird area in terms of what category it fell under; all I can say is we spent a humongous amount of time on this project, mainly trying to wrap our heads around the proofs. We also learned a huge deal from this project, which I assume was the purpose. There seemed to be a good deal of flexibility in the assignment description, so I hope our project was ok.
  
  Unrelated note: Is there anyway to learn more about how lattices can be used in computer science or to get involved in some related research? For right now, I'm just slowly working my way through Oded's notes, and then I'll move onto some more recent literature, but it would be great if there was a way to actually do something with that knowledge.
