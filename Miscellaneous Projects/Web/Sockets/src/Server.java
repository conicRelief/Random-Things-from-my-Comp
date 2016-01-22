import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.InetAddress;
import java.net.Socket;

/**
 * Created by otto on 11/24/15.
 */
public class Server{
   static int portNumber;


    public static void main (String[] args) {
        EasyPrint.disableOutputAnnotations();
        startUpMessage(args);
        portNumber = Integer.parseInt(args[0]);

        //Start accepting connections.
        while(true) {
            // For each succesful connection  I statup a new thread that deals with client server communications.
            try {
                    Socket echoSocket = new Socket(InetAddress.getLocalHost(),portNumber);
                    PrintWriter out =
                            new PrintWriter(echoSocket.getOutputStream(), true);
                    BufferedReader in =
                            new BufferedReader(
                                    new InputStreamReader(echoSocket.getInputStream()));
                    BufferedReader stdIn =
                            new BufferedReader(
                                    new InputStreamReader(System.in));

                }
            catch(Exception e)
            {
                EasyPrint.println("Bummer");
            }




            break;
        }
        EasyPrint.println(
                "The server is no longer looking to make connections to clients.  " + "\n" +
                "The server is shutting down now", "shutdown");
    }


    private static void startUpMessage(String[] args)
    {
        String ouputTag = "startup";
        EasyPrint.print("Server.java is starting up with the following arguments: ",ouputTag);
        for (String s : args)
        {
            EasyPrint.print(s + " ", ouputTag);
        }
        EasyPrint.print("\n", ouputTag);
    }

    public class ServerConnection
    {


    }
    //Accepts port number as command line command

    //The server will maintain a list of simulated files and allow the clients to perform operations on them.
    //Accept connections from clients.
    // Create a simulated list of files,
    //each one having a name and associated contents, which can be plain text or an image.
    // The server can read these in initially, but will not interact with the real file system thereafter.
    // Create a new thread for each 	client.


    /*
    *
    * The server thread will:

        Accept and process requests from 	the client.

        Provide mutual exclusion 	protection for the simulated file system.

        Send only the minimal data needed 	to the client, not the menu or other UI text.

    *
    *
    *
    *
    * */
}
