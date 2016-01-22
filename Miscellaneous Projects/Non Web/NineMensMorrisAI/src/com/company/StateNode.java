package com.company;

import apple.laf.JRSUIConstants;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by otto on 10/24/15.
 */
public class StateNode implements Comparable<StateNode>{

    static final BoardWorker boardWorker = new BoardWorker();

    public double heuristicScore;
    public Triable[] theBoard;
    public Triable[] endStateMetaData; // This is data that we pass up all the way through min-max. Its a way of analyzing end game results.

        public List<StateNode> chilldren = new ArrayList<StateNode>();

    public StateNode()
    {}
    public StateNode(Triable[] t, boolean midGame)
    {
        this.theBoard = t;
        heuristicScore = calculateScore(t,0,midGame);
    }
    public double calculateScore(Triable[] triables  , Integer depth, boolean isMidGame)
    {
        double sum = 0;
        for(Heuristic h : boardWorker.generateAListOfHeuristics(isMidGame))
        {
            sum+= h.generateHeuristic(triables);
        }
        return sum;
    }


    @Override
    public int compareTo(StateNode stateNode) {
        return ((Double)(this.heuristicScore - stateNode.heuristicScore)).intValue();
    }
}
