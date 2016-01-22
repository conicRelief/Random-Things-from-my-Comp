package com.company;

import java.awt.*;
import java.awt.datatransfer.Transferable;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Created by otto on 10/24/15.
 */
public class PossibleStatesGenerator {
    public StateSieves sieve = new StateSieves();
    public void print(String s)
    {
//        System.out.print(s);
    }


    public List<StateNode> midGameGenerateNextStates(StateNode s, boolean whitesTurn)
    {
        List<Triable[]> t = midGameGenerateNextStates(s.theBoard, whitesTurn);
        List<StateNode> stateNodes = new ArrayList<StateNode>();
        for(Triable[] triable : t)
        {
            stateNodes.add(new StateNode(triable,true));
        }
        return stateNodes;
    }

    public List<StateNode> openGameGenerateNextStates(StateNode s, boolean whitesTurn)
    {
        List<Triable[]> t = openGameGenerateNextStates(s.theBoard, whitesTurn, 0, 0);
        List<StateNode> stateNodes = new ArrayList<StateNode>();
        for(Triable[] triable : t)
        {
            stateNodes.add(new StateNode(triable,false));
        }
        return stateNodes;
    }

    public List<Triable[]> midGameGenerateNextStates(Triable [] theBoard, boolean whitesTurn)
    {
        /*
        * The logic. If whites turn. Look for empty spaces. Look for white peices that can fill up the currnet area/
        * Create a new board state for each possible white movement to that empty space.
        * Check to see if that new state warrants a white mill completion. If it does then generate all black removal states.
        *
        * Apply same logic for black.
        *
        * This algorithm in the previous two sections build up our states.
        * */
        List<Triable[]> listOfNextBoards = new ArrayList<Triable[]>();
        print("Size:  " + listOfNextBoards.size());
        if(whitesTurn)
        {
            print("\n");
            if(StateSieves.countWhite(theBoard) > 3) {
                for (int i = 0; i < theBoard.length; i++) {

                    if (theBoard[i].isNone()) {
                        for (Integer n : sieve.whitePeiceIsMovableHere(theBoard, i)) {
//                        print("White Peice is movable here|");
                            Triable[] newState = MorrisTernary.copyMe(theBoard);
                            print("--------------------" + n + "->" + i + " \n");
                            if (sieve.whiteMillFormedOnWhitePlaceMent(newState, n)) {
                                print("| black peice removal pending");
//                            print("White Peice movement eliminates Black Peice|");
                                newState[i].makeWhite();
                                newState[n].makeNone();
                                listOfNextBoards.addAll(blackPieceRemovalStateGenerator(newState));

                            } else {
                                newState[i].makeWhite();
                                newState[n].makeNone();
                                listOfNextBoards.add(newState);
                            }
                            print("\n");

                        }
//                    print("Size after "+ (i) +":  " + listOfNextBoards.size());

                    }
                }
            }
            else if(StateSieves.countWhite(theBoard) == 3)
            {
                List<Integer> whitePositions = new ArrayList<Integer>();
                for(int l = 0 ; l<theBoard.length; l++)
                {
                  if(theBoard[l].isWhite())
                  {
                      whitePositions.add(l);
                  }
                }
                for(Integer i : whitePositions)
                {
                    for(int n = 0; n < theBoard.length; n++)
                    {
                        if(n!=i && theBoard[n].isNone())
                        {
                            Triable[] newState = MorrisTernary.copyMe(theBoard);
                            newState[n].makeWhite();
                            newState[i].makeNone();
                            listOfNextBoards.add(newState);
                        }
                    }
                }


            }
        }
        else if (!whitesTurn) {


            print("\n");
            if (StateSieves.countBlack(theBoard) > 3) {
                for (int i = 0; i < theBoard.length; i++) {

                    if (theBoard[i].isNone()) {
                        for (Integer n : sieve.blackPeiceIsMovableHere(theBoard, i)) {
//                        print("White Peice is movable here|");
                            Triable[] newState = MorrisTernary.copyMe(theBoard);
                            print("--------------------" + n + "->" + i + " \n");
                            if (sieve.whiteMillFormedOnWhitePlaceMent(newState, n)) {
                                print("| black peice removal pending");
//                            print("White Peice movement eliminates Black Peice|");
                                newState[i].makeWhite();
                                newState[n].makeNone();
                                listOfNextBoards.addAll(blackPieceRemovalStateGenerator(newState));

                            } else {
                                newState[i].makeWhite();
                                newState[n].makeNone();
                                listOfNextBoards.add(newState);
                            }
                            print("\n");

                        }
//                    print("Size after "+ (i) +":  " + listOfNextBoards.size());

                    }
                }
            }
        }
        else if(StateSieves.countBlack(theBoard) == 3)
        {
            List<Integer> blackPositions = new ArrayList<Integer>();
            for(int l = 0 ; l<theBoard.length; l++)
            {
                if(theBoard[l].isBlack())
                {
                    blackPositions.add(l);
                }
            }
            for(Integer i : blackPositions)
            {
                for(int n = 0; n < theBoard.length; n++)
                {
                    if(n!=i && theBoard[n].isNone())
                    {
                        Triable[] newState = MorrisTernary.copyMe(theBoard);
                        newState[n].makeBlack();
                        newState[i].makeNone();
                        listOfNextBoards.add(newState);
                    }
                }
            }

        }
        return listOfNextBoards;
    }


    public List<Triable[]> openGameGenerateNextStates(Triable[] theBoard, boolean whitesTurn, int whitePeicesLeft, int blackPeicesLeft)
    {
        for(Triable x : theBoard)
        {print(x.isNone() + " ");
        }
        print("\n");
        List<Triable[]> listOfNextBoards = new ArrayList<Triable[]>();

        if(whitesTurn)
        {
            print("Whites turn \n");
            for (int i = 0; i < theBoard.length; i++) {
                print("" + i);
                Triable candidateForPlacement = theBoard[i];
                if (candidateForPlacement.isNone())
                {
                    print("  Is candidate|");

                    Triable[] pending = MorrisTernary.copyMe(theBoard);



                    // Is a mill formed with placement?
                    if(sieve.whiteMillFormedOnWhitePlaceMent(pending,i))
                    {
                        // Generate all states
                        print("  Should be replacing black peices|");
                        pending[i].makeWhite();
                        print("{" + listOfNextBoards.size() + "}");
                        listOfNextBoards.addAll(blackPieceRemovalStateGenerator(pending));
                        print("{" + listOfNextBoards.size() + "}");

                    }
                    else
                    {
                        // if not, lets add it
                        print("  adding to empty|");
                        pending[i].makeWhite();
                        listOfNextBoards.add(pending);
                    }
                }
                else
                {
                    if(theBoard[i].isWhite())
                    {print("  This part of the board is White");}
                    else
                    {print("  This part of the board is Black");}
                }
                print("\n");
            }
        }
        else
        {

            print("Black's turn \n");
            for (int i = 0; i < theBoard.length; i++) {
                print("" + i);
                Triable candidateForPlacement = theBoard[i];
                if (candidateForPlacement.isNone())
                {
                    print("  Is candidate|");

                    Triable[] pending = MorrisTernary.copyMe(theBoard);



                    // Is a mill formed with placement?
                    if(sieve.blackMillFormedOnBlackPlacement(pending, i))
                    {
                        // Generate all states
                        print("  Should be replacing black peices|");
                        pending[i].makeBlack();
                        print("{" + listOfNextBoards.size() + "}");
                        listOfNextBoards.addAll(whitePieceRemovalStateGenerator(pending));
                        print("{" + listOfNextBoards.size() + "}");

                    }
                    else
                    {
                        // if not, lets add it
                        print("  adding to empty|");
                        pending[i].makeBlack();
                        listOfNextBoards.add(pending);
                    }
                }
                else
                {
                    if(theBoard[i].isWhite())
                    {print("  This part of the board is White");}
                    else
                    {print("  This part of the board is Black");}
                }
                print("\n");
            }
        }
        return listOfNextBoards;
    }
    private List<Triable[]> blackPieceRemovalStateGenerator(Triable[] theBoard)
    {
        List<Triable[]> returnList = new ArrayList<Triable[]>();
        for(int i = 0 ; i < theBoard.length; i++)
        {
            if(theBoard[i].isBlack())
            {
                print("==Replacing black Piece==|");
                Triable[] newState = MorrisTernary.copyMe(theBoard);
                newState[i].makeNone();
                returnList.add(newState);
            }
        }
        print( "" + returnList.size());
        return returnList;
    }
    private List<Triable[]> whitePieceRemovalStateGenerator(Triable[] theBoard)
    {
        List<Triable[]> returnList = new ArrayList<Triable[]>();
        for(int i = 0 ; i < theBoard.length; i++)
        {
            if(theBoard[i].isWhite())
            {
                print("==Replacing white Piece==|");
                Triable[] newState = MorrisTernary.copyMe(theBoard);
                newState[i].makeNone();
                returnList.add(newState);
            }
        }
        print( "" + returnList.size());
        return returnList;
    }
}
