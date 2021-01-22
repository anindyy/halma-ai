# halma-ai
So I'm rechallenging myself to revise my assignment last semester: making an AI for playing Halma. This is the log of what changes I'm making to track how I think.

The main problem of the assignment is:
1.	It's painfully slow. Takes more than half an hour to complete a game. Tortures my team to run the tests because we needed to run it all night long.
2.	Gets stuck pretty often. The tests conclude that this AI has 50% chances finding no solution. 
3.	Even though it uses minimax algorithm, which they say is “unbeatable”, we beat this AI pretty easily. Even though we're playing against it half asleep, we had 90% win rate.

There are other problems that can be addressed at, but those three are the main problem which I think the core reasons why this AI isn't top tier. I will focus fixing those problems first. To spice things up, I'll name this AI: Sera.

## #1: Why are you so slow, Sera???
As mentioned above, Sera takes nearly half an hour to complete a game. It's even size-based. For larger sizes, she took one freaking hour. That annoys and saddens me the most because I see my friend's AI can solve the puzzle pretty quickly—it only took them few miliseconds to decide on a move, while Sera used up all three-second time limit just to run up to the third layer of the minimax tree.

I suspected this happened because of the structure of the board. We had the board implemented with a class—so it's a custom type? And the board holds another custom type: the pawns. This board will be instantiated as nodes, so you can imagine for an 8x8 board with 3-level game tree, it can take up to hundreds of board instances and millions of pawn instances. Very resource heavy.

I blame my not-thinking-too-far planning method for this mess.

So first, I changed my board structure. I eliminated the pawn class and had it implemented in simple numbers instead. Because the original board class is massive and pretty messy, I decided that I rewrite the board structure into a brand new file: board2.py. I implemented crucial features first like moving the pawns, checking for a valid move, checking wins. 

I realized by changing the board structure, I'm changing my whole AI project :clown: But it's okay, let's have some improvements, Sera! Oh I wanted to test the changes but I can't because the whole structure changes ... well, let's just push back the tests to the end then.

From editing the file, I also realized that we forget the useful Python predicate 'in' and by using it, the code becomes much simpler. I regret not realizing this faster. Anyway, the brand new board is done, let's move on to the next problem.

## #2: Let's think better!
