package com.company;

import java.util.*;

/**
 * Created by otto on 10/24/15.
 */
public class BoardWorker {

public static List<Heuristic> addedHeuristics = new ArrayList<Heuristic>();


public List<Heuristic> generateAListOfHeuristics(boolean midGame)
{

    List<Heuristic> heuristics =  new ArrayList<Heuristic>();

    final Heuristic whitePerTotal;
    final Heuristic originalHeuristic;
    final Heuristic endGameHeuristic;



    // Proposed Heuristic
    originalHeuristic = new Heuristic() {
        @Override
        double generateHeuristic(Triable[] t) {
            double b = StateSieves.countBlack(t);
            double w = StateSieves.countWhite(t);
            return w-b;
        }
    };
    // EndGame Heuristic
    endGameHeuristic = new Heuristic() {
        @Override
        double generateHeuristic(Triable[] t) {
            if (StateSieves.countBlack(t) < 3)
            {
                return 999;
            }
            else if( StateSieves.countWhite(t) < 3)
            {
                return -999;
            }

            return 0;
        }
    };


    // My heuristic
    whitePerTotal = new Heuristic() {
        @Override
        double generateHeuristic(Triable[] t) {

            double b = StateSieves.countBlack(t);
            double w = StateSieves.countWhite(t);
            return w/(b+w);
        }
    };


    heuristics.add(originalHeuristic);
    if (midGame)
    {
//        heuristics.add(endGameHeuristic);
    }
    heuristics.addAll(addedHeuristics);
    return heuristics;
}
}
