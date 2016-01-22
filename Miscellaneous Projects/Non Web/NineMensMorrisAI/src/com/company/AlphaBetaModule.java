package com.company;

import java.util.List;

/**
           _      _____  _    _               ____  ______ _______            _____  _____  _    _ _   _ _____ _   _  _____
     /\   | |    |  __ \| |  | |   /\        |  _ \|  ____|__   __|/\        |  __ \|  __ \| |  | | \ | |_   _| \ | |/ ____|
    /  \  | |    | |__) | |__| |  /  \ ______| |_) | |__     | |  /  \ ______| |__) | |__) | |  | |  \| | | | |  \| | |  __
   / /\ \ | |    |  ___/|  __  | / /\ \______|  _ <|  __|    | | / /\ \______|  ___/|  _  /| |  | | . ` | | | | . ` | | |_ |
  / ____ \| |____| |    | |  | |/ ____ \     | |_) | |____   | |/ ____ \     | |    | | \ \| |__| | |\  |_| |_| |\  | |__| |
 /_/    \_\______|_|    |_|  |_/_/    \_\    |____/|______|  |_/_/    \_\    |_|    |_|  \_\\____/|_| \_|_____|_| \_|\_____|
  ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______
 |______|______|______|______|______|______|______|______|______|______|______|______|______|______|______|______|______|______|

 **/
public class AlphaBetaModule {

    static int numberOfNodesEvaluated = 0;
    static PossibleStatesGenerator generator = new PossibleStatesGenerator();


    public static Triable[] evaluateOpeningForWhite(Triable[] t, int depth)
    {
        List<StateNode> firstExpansion = generator.openGameGenerateNextStates(new StateNode(t, false), true);

        Triable[] bestBoard = new Triable[t.length];
        Double bestScore = Double.NEGATIVE_INFINITY;

        for(StateNode state : firstExpansion)
        {
            double currentBestScoreForState = minOpening(new StateNode(t,false), depth, Double.NEGATIVE_INFINITY, Double.POSITIVE_INFINITY);
            if(bestScore < currentBestScoreForState)
            {
                bestScore = currentBestScoreForState;
                bestBoard = state.theBoard;
            }
        }
        System.out.println("Positions evaluated by static estimation: " + numberOfNodesEvaluated);
        numberOfNodesEvaluated = 0;
        System.out.println("Alpha-Beta estimate: "+ bestScore);

        return bestBoard;
    }
    public static Triable[] evaluateMidForWhite(Triable[] t, int depth)
    {
        List<StateNode> firstExpansion = generator.midGameGenerateNextStates(new StateNode(t,false),true);

        Triable[] bestBoard = new Triable[t.length];
        Double bestScore = Double.NEGATIVE_INFINITY;

        for(StateNode state : firstExpansion)
        {
            double currentBestScoreForState = minOpening(new StateNode(t,false), depth, Double.NEGATIVE_INFINITY, Double.POSITIVE_INFINITY);
            if(bestScore < currentBestScoreForState)
            {
                bestScore = currentBestScoreForState;
                bestBoard = state.theBoard;
            }
        }
        System.out.println("Positions evaluated by static estimation: " + numberOfNodesEvaluated);
        numberOfNodesEvaluated = 0;
        System.out.println("Alpha-Beta estimate: "+ bestScore);

        return bestBoard;
    }




    public static  Triable[] evaluateOpeningForBlack(Triable[] t, int depth)
    {
        List<StateNode> firstExpansion = generator.openGameGenerateNextStates(new StateNode(t, true), false);

        Triable[] bestBoard = new Triable[t.length];
        Double bestScore = Double.POSITIVE_INFINITY;

        for(StateNode state : firstExpansion)
        {
            double currentBestScoreForState = maxOpening(new StateNode(t, false), depth, Double.NEGATIVE_INFINITY, Double.POSITIVE_INFINITY);
            if(bestScore > currentBestScoreForState)
            {
                bestScore = currentBestScoreForState;
                bestBoard = state.theBoard;
            }
        }
        System.out.println("Positions evaluated by static estimation: " + numberOfNodesEvaluated);
        numberOfNodesEvaluated = 0;
        System.out.println("Alpha-Beta estimate: "+ bestScore);

        return bestBoard;
    }


    public static  Triable[] evaluateMidForBlack(Triable[] t, int depth)
    {
        List<StateNode> firstExpansion = generator.midGameGenerateNextStates(new StateNode(t,true),false);

        Triable[] bestBoard = new Triable[t.length];
        Double bestScore = Double.POSITIVE_INFINITY;

        for(StateNode state : firstExpansion)
        {
            double currentBestScoreForState = maxOpening(new StateNode(t, false), depth, Double.NEGATIVE_INFINITY, Double.POSITIVE_INFINITY);
            if(bestScore > currentBestScoreForState)
            {
                bestScore = currentBestScoreForState;
                bestBoard = state.theBoard;
            }
        }
        System.out.println("Positions evaluated by static estimation: " + numberOfNodesEvaluated);
        numberOfNodesEvaluated = 0;
        System.out.println("Alpha-Beta estimate: "+ bestScore);

        return bestBoard;
    }
    //@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    //                              ↓↓↓OPENING MOVES↓↓↓
    //@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


    public static Double maxOpening(StateNode stateNode, int depth, Double alpha1, Double beta1)
    {

        List<StateNode> possibleStatesExpansion = generator.openGameGenerateNextStates(stateNode,true);
        Double max =  Double.NEGATIVE_INFINITY;

        if(depth == 0)
        {
            for(StateNode s : possibleStatesExpansion)
            {
                if(s.heuristicScore > max)
                {
                    numberOfNodesEvaluated++;
                    max = s.heuristicScore;
                }
            }
            return max;
        }
        else
        {
            for(StateNode s : possibleStatesExpansion)
            {
                numberOfNodesEvaluated++;

                Double minOfS = minOpening(s, depth - 1, alpha1, beta1);

                if(minOfS > max)
                {
                    max = s.heuristicScore;
                    if(minOfS >= beta1)
                    {
                        return max;
                    }
                    else
                    {
                        if(alpha1 <= minOfS)
                        {
                            alpha1 = minOfS;
                        }
                    }
                }
            }

            return max;

        }
    }



//    public static StateNode maxOpening(StateNode stateNode, int depth, Double alpha1, Double beta1)
//    {
////        System.out.println("Tier: " + depth + "|Alpha: " + alpha1 + "|Beta: " + beta1);
//
//
//        List<StateNode> possibleStatesExpansion = generator.openGameGenerateNextStates(stateNode,true);
//        StateNode max =  new StateNode();
//
//        if(possibleStatesExpansion.size() == 0)
//        {
//            stateNode.heuristicScore = -999;
//            return stateNode;
//        }
//
//        max.heuristicScore = Double.NEGATIVE_INFINITY;
//
//        if(depth == 0)
//        {
//            for(StateNode s : possibleStatesExpansion)
//            {
//                if(s.heuristicScore > max.heuristicScore)
//                {
//                    numberOfNodesEvaluated++;
//                    max = s;
//                }
//            }
//            return max;
//        }
//        else
//        {
//            for(StateNode s : possibleStatesExpansion)
//            {
//                numberOfNodesEvaluated++;
//                StateNode minOfS = minOpening(s, depth - 1, alpha1, beta1);
//
//                if(minOfS.heuristicScore > max.heuristicScore)
//                {
//                    max = s;
//                    if(minOfS.heuristicScore >= beta1)
//                    {
//                        return s;
//                    }
//                    else
//                    {
//                        if(alpha1 <= minOfS.heuristicScore)
//                        {
//                            alpha1 = minOfS.heuristicScore;
//                        }
//                    }
//                }
//            }
//
//            return max;
//
//        }
//    }
    public static Double minOpening(StateNode stateNode, int depth, Double alpha2, Double beta2)
    {
//        System.out.println("Tier: " + depth + "|Alpha: " + alpha2 + "|Beta: " + beta2);
        List<StateNode> possibleStatesExpansion = generator.openGameGenerateNextStates(stateNode,false);

        Double min = Double.POSITIVE_INFINITY;


        if(depth == 0)
        {
            for(StateNode s : possibleStatesExpansion)
            {
                numberOfNodesEvaluated++;
                if(s.heuristicScore < min)
                {
                    min = s.heuristicScore;
                }
            }
            return min;
        }
        else
        {
            for(StateNode s : possibleStatesExpansion)
            {
                Double minOfS = maxOpening(s, depth - 1, alpha2, beta2);
                numberOfNodesEvaluated++;

                if(minOfS < min)
                {
                    min = minOfS;
                    if(minOfS <= alpha2)
                    {
                        return min;
                    }
                    else
                    {
                        if( minOfS <= beta2)
                        {
                            beta2 = minOfS;
                        }
                    }
                }
            }

            return min;

        }
    }



//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
//                                ↓↓↓MIDGAME MOVES↓↓↓
//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    public static Double maxMidgame(StateNode stateNode, int depth, Double alpha1, Double beta1)
    {


        List<StateNode> possibleStatesExpansion = generator.openGameGenerateNextStates(stateNode,true);

        if(possibleStatesExpansion.size() == 0)
        {
            numberOfNodesEvaluated++;
            return -999.0;
        }

        Double max = Double.NEGATIVE_INFINITY;

        if(depth == 0)
        {
            for(StateNode s : possibleStatesExpansion)
            {
                if(s.heuristicScore > max)
                {
                    numberOfNodesEvaluated++;
                    max = s.heuristicScore;
                }
            }
            return max;
        }
        else
        {
            for(StateNode s : possibleStatesExpansion)
            {
                numberOfNodesEvaluated++;

                Double minOfS = minMidGame(s, depth - 1, alpha1, beta1);

                if(minOfS > max)
                {
                    max = minOfS;
                    if(max >= beta1)
                    {
                        return max;
                    }
                    else
                    {
                        if(alpha1 <= max)
                        {
                            alpha1 = max;
                        }
                    }
                }
            }

            return max;

        }
    }
    public static Double minMidGame(StateNode stateNode, int depth, Double alpha2, Double beta2)
    {
//        System.out.println("Tier: " + depth + "|Alpha: " + alpha2 + "|Beta: " + beta2);
        List<StateNode> possibleStatesExpansion = generator.openGameGenerateNextStates(stateNode,false);
        if(possibleStatesExpansion.size() == 0)
        {
            numberOfNodesEvaluated++;
            return 999.00;
        }

        Double min = Double.POSITIVE_INFINITY;

        if(depth == 0)
        {
            for(StateNode s : possibleStatesExpansion)
            {
                numberOfNodesEvaluated++;
                if(s.heuristicScore < min)
                {
                    min = s.heuristicScore;
                }
            }
            return min;
        }
        else
        {
            for(StateNode s : possibleStatesExpansion)
            {
                Double maxOfS = maxMidgame(s, depth - 1, alpha2, beta2);
                numberOfNodesEvaluated++;

                if(maxOfS < min)
                {
                    min = maxOfS;
                    if(min <= alpha2)
                    {
                        return min;
                    }
                    else
                    {
                        if( maxOfS <= beta2)
                        {
                            beta2 = maxOfS;
                        }
                    }
                }
            }
            return min;
        }
    }}