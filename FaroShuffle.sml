(*
Uriel Ulloa
Program that calculates the number of faro shuffles needed to return a deck to its original order.
Assumes all decks are of even length.
Coded in Standard ML
*)

(*
Creates a deck of card of length n
*)
fun idlist(n) =
  let fun iterList(n, i) =
    if i < n
      then i::iterList(n, i+1)
      else [i]
  in iterList(n, 1)
  end;

(*
Helper function that splits a list in half. Assumes all list are of even length.
*)
fun split(L) =
  let fun iterSplit([], len, i, list1, list2) = (list1, list2)
  | iterSplit(x::list, len, i, list1, list2) =
    if i < (len div 2)
      then iterSplit(list, len, i+1, list1@[x], list2)
      else iterSplit(list, len, i+1, list1, list2@[x])
    in
    iterSplit(L, length L, 0, [], [])
    end;
(*
Function that performs a single Faro shuffle.
*)
fun shuffle(L) =
  let fun iterShuffle([], [], newDeck, i) = newDeck
  | iterShuffle(deck1, deck2, newDeck, i) =
    if i = 1
      then iterShuffle(tl deck1, deck2, newDeck@[hd deck1], 2)
      else iterShuffle(deck1, tl deck2, newDeck@[hd deck2], 1)
  in
  let val deck = split(L)
      val deck1 = #1 deck
      val deck2 = #2 deck
    in
  iterShuffle(deck1, deck2, [], 1)
  end
  end;

(*
Number of faro shuffles needed to return a deck of n number of cards back to its original order 
*)
fun shuffleperiod(n) =
  let fun compareDeck(oDeck, newDeck, count) =
    if oDeck = newDeck
      then count
      else compareDeck(oDeck, shuffle newDeck, count+1)
    in
    compareDeck(idlist n, shuffle(idlist n), 1)
    end;
