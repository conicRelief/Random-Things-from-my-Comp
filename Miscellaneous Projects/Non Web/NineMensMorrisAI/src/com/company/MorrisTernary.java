package com.company;

/**
 * Created by otto on 10/24/15.
 */
public class MorrisTernary implements Triable{
    boolean booleanWhite = false;
    boolean booleanBlack = false;
    public MorrisTernary(){}
    public MorrisTernary(Triable t)
    {
        if(t.isNone())
        {
            this.makeEmpty();
        }
        else
        {
            if(t.isWhite())
            {this.makeWhite();}
            if(t.isBlack())
            {this.makeBlack();}
        }
    }
    public boolean isBlack() { return booleanBlack;       }
    public boolean isWhite() { return booleanWhite;       }
    public boolean isNone()  { return !booleanBlack && !booleanWhite; }
    public void makeWhite()  { booleanWhite = true; booleanBlack = false;}
    public void makeNone()   { makeEmpty();}
    public static Triable[] copyMe(Triable[] triables)
    {
        Triable[] pending = new Triable[triables.length];
        for(int k=0; k <pending.length; k++)
        {
            Triable a = triables[k];
            pending[k] = new MorrisTernary(a);
        }
        return pending;
    }
    public void makeBlack()  { booleanWhite = false; booleanBlack = true;}
    public void makeEmpty()  { booleanWhite = booleanBlack = false;}
}
