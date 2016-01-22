package com.company;

import java.util.List;

/**
  __  __ _____ _   _ _____ __  __          __   __
 |  \/  |_   _| \ | |_   _|  \/  |   /\    \ \ / /
 | \  / | | | |  \| | | | | \  / |  /  \    \ V /
 | |\/| | | | | . ` | | | | |\/| | / /\ \    > <
 | |  | |_| |_| |\  |_| |_| |  | |/ ____ \  / . \
 |_|  |_|_____|_| \_|_____|_|  |_/_/    \_\/_/ \_\
  ______ ______ ______ ______ ______ ______ ______ ______
 |______|______|______|______|______|______|______|______|

 */
public class MiniMaxModule{
    static final boolean MUTE_DEBUGGER = false;
   static PossibleStatesGenerator generator = new PossibleStatesGenerator();
   static int numberOfNodesEvaluated = 0;

    public static Triable[] evaluateOpeningForWhite(Triable[] theBoard, int depth)
    {
        StateNode bestMove = new StateNode();
        bestMove.heuristicScore = Double.NEGATIVE_INFINITY;

        List<StateNode> expansionStates = generator.openGameGenerateNextStates(new StateNode(theBoard,false), true);
        for(StateNode state : expansionStates)
        {
            double bestAnswerForState = minOpening(state, depth);
            printBoard(state.theBoard);
            if(bestAnswerForState > bestMove.heuristicScore)
            {
                dPrint("                " + bestAnswerForState);

                bestMove.heuristicScore = bestAnswerForState;
                bestMove.theBoard = state.theBoard;
            }
            else
            {
                dPrint(bestAnswerForState+"");
            }
        }

        System.out.println("Positions evaluated by static estimation: " + numberOfNodesEvaluated);
        numberOfNodesEvaluated = 0;
        System.out.println("MINIMAX estimate: "+ bestMove.heuristicScore);
        return bestMove.theBoard;
    }
    //===========================================================================
    public static Triable[] evaluateOpeningForBlack(Triable[] theBoard, int depth)
    {
        StateNode bestMove = new StateNode();
        bestMove.heuristicScore = Double.POSITIVE_INFINITY;

        List<StateNode> expansionStates = generator.openGameGenerateNextStates(new StateNode(theBoard,false), false);
        for(StateNode state : expansionStates)
        {
            double bestAnswerForState = maxOpening(state, depth);

            if(bestAnswerForState > bestMove.heuristicScore)
            {
                bestMove.heuristicScore = state.heuristicScore;
                bestMove.theBoard = state.theBoard;
            }
            else
            {

            }
        }
        System.out.println("Positions evaluated by static estimation: " + numberOfNodesEvaluated);
        numberOfNodesEvaluated = 0;
        System.out.println("MINIMAX estimate: "+ bestMove.heuristicScore);
        return bestMove.theBoard;
    }

    public static Triable[] evaluateMidGameForWhite(Triable[] theBoard, int depth)
    {
        StateNode bestMove = new StateNode();
        bestMove.heuristicScore = Double.NEGATIVE_INFINITY;

        List<StateNode> expansionStates = generator.midGameGenerateNextStates(new StateNode(theBoard, false), false);
        for(StateNode state : expansionStates)
        {
            double bestAnswerForState = minOpening(state, depth);

            if(bestAnswerForState < bestMove.heuristicScore)
            {
                bestMove.heuristicScore = state.heuristicScore;
                bestMove.theBoard = state.theBoard;
            }
            else
            {

            }
        }

        //        = maxOpening(new StateNode(t,false), depth).theBoard;
        System.out.println("Positions evaluated by static estimation: " + numberOfNodesEvaluated);
        numberOfNodesEvaluated = 0;

        System.out.println("MINIMAX estimate: "+ bestMove.heuristicScore);
        return bestMove.theBoard;

    }
    public static Triable[] evaluateMidGameForBlack(Triable[] theBoard, int depth)
    {
        StateNode bestMove = new StateNode();
        bestMove.heuristicScore = Double.POSITIVE_INFINITY;

        List<StateNode> expansionStates = generator.midGameGenerateNextStates(new StateNode(theBoard,false), false);
        for(StateNode state : expansionStates)
        {
            double bestAnswerForState = maxOpening(state, depth);

            if(bestAnswerForState > bestMove.heuristicScore)
            {
                bestMove.heuristicScore = state.heuristicScore;
                bestMove.theBoard = state.theBoard;
            }
            else
            {

            }
        }

        System.out.println("Positions evaluated by static estimation: " + numberOfNodesEvaluated);
        numberOfNodesEvaluated = 0;
        System.out.println("MINIMAX estimate: "+ bestMove.heuristicScore);
        return bestMove.theBoard;

    }

    /*
    //@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    //                              ↓↓↓OPENING MOVES↓↓↓
    //@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    */



    private static Double maxOpening(StateNode stateNode, int depth)
    {
        List<StateNode> expansionStates = generator.openGameGenerateNextStates(new StateNode(stateNode.theBoard,false), true);
        Double max = Double.NEGATIVE_INFINITY;

        if (depth == 0) {
            for (StateNode s : expansionStates) {
                numberOfNodesEvaluated++;
                if (s.heuristicScore > max) {
                    max = s.heuristicScore;
                }
            }
        }
        else
        {
            for (StateNode s : expansionStates) {
                numberOfNodesEvaluated++;

                Double b = minOpening(s, depth - 1);
                if ( b > max) {
                    max = b;
                }
            }
        }
        return max;
    }

    private static Double minOpening(StateNode stateNode, int depth)
    {
        List<StateNode> expansionStates = generator.openGameGenerateNextStates(new StateNode(stateNode.theBoard,false), false);
        Double min = Double.POSITIVE_INFINITY;
        if (depth == 0) {
            for (StateNode s : expansionStates) {
                numberOfNodesEvaluated++;
                if (s.heuristicScore < min) {
                    min = s.heuristicScore;
                }
            }
        }
        else
        {
            for (StateNode s : expansionStates) {
                numberOfNodesEvaluated++;
                Double c = maxOpening(s, depth - 1);
                if (c < min) {
                    min = c;
                }
            }
        }

        return min;


    }


/*
//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
//                              ↓↓↓MIDGAME MOVES↓↓↓
//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
 */
private static Double maxMidGame(StateNode stateNode, int depth)
{

    List<StateNode> expansionStates = generator.midGameGenerateNextStates(new StateNode(stateNode.theBoard,true), true);
    Double max = Double.NEGATIVE_INFINITY;

    if ( expansionStates.size() == 0)
    {
        numberOfNodesEvaluated++;
        return -999.0;
    }
    if (depth == 0) {
        for (StateNode s : expansionStates) {
            numberOfNodesEvaluated++;
            if (s.heuristicScore > max) {
                max = s.heuristicScore;
            }
        }
    }
    else
    {
        for (StateNode s : expansionStates) {
            numberOfNodesEvaluated++;
            Double miniValue =  minMidGame(s, depth - 1);
            if (miniValue > max) {
                max = miniValue;
            }
        }
    }
    return max;
}
    private static Double minMidGame(StateNode stateNode, int depth)
    {

        List<StateNode> expansionStates = generator.midGameGenerateNextStates(new StateNode(stateNode.theBoard,true), false);
        Double min =  Double.POSITIVE_INFINITY;

        if ( expansionStates.size() == 0)
        {
            numberOfNodesEvaluated++;
            return 999.0;
        }

        if (depth == 0) {
            for (StateNode s : expansionStates) {
                numberOfNodesEvaluated++;
                if (s.heuristicScore < min) {
                    min = s.heuristicScore;
                }
            }

        }
        else
        {
            for (StateNode s : expansionStates)
            {
                numberOfNodesEvaluated++;
                Double maxiValue = maxMidGame(s, depth - 1);
                if (maxiValue < min) {
                    min = maxiValue;
                }
            }
        }
        return min;

    }    public static void printBoard(Triable[] t)
    {
        if(!MUTE_DEBUGGER) {
            for (Triable x : t) {
                if (x.isBlack()) {
                    System.out.print("b");
                } else if (x.isWhite()) {
                    System.out.print("w");
                } else if (x.isNone()) {
                    System.out.print("x");
                }
            }
            System.out.println("");
        }
    }
    public static void dPrint(String s)
    {
        if (!MUTE_DEBUGGER)
        {
            System.out.println(s);
        }
    }

}
